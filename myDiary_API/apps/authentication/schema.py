from .models import User
import graphene, django_filters
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = []
        interfaces = (relay.Node, )

class UserInput(graphene.InputObjectType):
    id = graphene.ID()
    username = graphene.String(required=True)
    fname = graphene.String(required=False)
    lname = graphene.String(required=False)
    password = graphene.String(required=True)
    email = graphene.String(required=True)


class CreateUser(relay.ClientIDMutation):
    class Input:
        user = graphene.Argument(UserInput)
    new_user = graphene.Field(UserNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        user_data = input.get('user')
        new_user = User.objects.create(**user_data)
        new_user.set_password(user_data.get('password'))
        new_user.save()
        return cls(new_user=new_user)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

class Query(graphene.ObjectType):
    user = relay.Node.Field(UserNode)
    users = DjangoFilterConnectionField(UserNode)
