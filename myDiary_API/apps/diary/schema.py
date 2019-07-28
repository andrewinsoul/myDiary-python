from .models import Diary
import graphene, django_filters
from graphene import relay, ObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from graphql_jwt.decorators import login_required

class DiaryType(DjangoObjectType):
    class Meta:
        model = Diary

class DiaryNode(DjangoObjectType):
    class Meta:
        model = Diary
        filter_fields = {
            'name': ['exact', 'icontains'],
            'description': ['exact', 'icontains']
        }
        interfaces = (relay.Node, )

class DiaryInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String(required=True)
    is_private = graphene.String(required=False)
    description = graphene.String(required=True)

class CreateDiary(relay.ClientIDMutation):
    class Input:
        diary = graphene.Argument(DiaryInput)
    new_diary = graphene.Field(DiaryNode)

    @classmethod
    @login_required
    def mutate_and_get_payload(cls, root, info, **input):
        user = info.context.user
        diary_payload = input.get('diary')
        diary_payload['user'] = user
        new_diary = Diary.objects.create(**diary_payload)
        new_diary.save()
        return cls(new_diary=new_diary)

class Mutation(graphene.ObjectType):
    create_diary = CreateDiary.Field()

class Query(graphene.ObjectType):
    diary = graphene.Field(DiaryType, id=graphene.Int())
    public_diaries = DjangoFilterConnectionField(DiaryNode)
    my_diaries = DjangoFilterConnectionField(DiaryNode)

    def resolve_diary(root, info, **kwargs):
        try:
            user = info.context.user
            diary = Diary.objects.filter(id=kwargs.get('id')).first()
            if not diary:
                return GraphQLError('Diary not found')
            if diary.is_private:
                return diary if diary.user == user\
                    else GraphQLError('Access Denied, cannot view diary')
            return diary
        except GraphQLError as error:
            return error

    def resolve_public_diaries(root, info, **kwargs):
        return Diary.objects.filter(is_private=False)

    @login_required
    def resolve_my_diaries(root, info, **kwargs):
        user = info.context.user
        return Diary.objects.filter(user=user)
