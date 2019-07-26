from .models import Diary
import graphene, django_filters
from graphene import relay, ObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from graphql_jwt.decorators import login_required

class DiaryNode(DjangoObjectType):
    class Meta:
        model = Diary
        filter_fields = ['is_private', 'user__id']
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

