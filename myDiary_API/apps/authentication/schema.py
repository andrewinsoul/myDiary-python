from .models import User
import graphene
from graphene_django import DjangoObjectType

class UserType(DjangoObjectType):
    class Meta:
        model = User

class UserInput(graphene.InputObjectType):
    id = graphene.ID()
    username = graphene.String()
    fname = graphene.String()
    lname = graphene.String()
    password = graphene.String()
    email = graphene.String()

class CreateUser(graphene.Mutation):
    class Arguments:
        input = UserInput(required=True)
    user = graphene.Field(UserType)

    def mutate(self, info, **input):
        input = input['input']
        user = User(
            username = input.get('username'),
            fname = input.get('fname'),
            lname = input.get('lname'),
            email = input.get('email')
        )
        user.set_password(input.get('password'))
        user.save()
        return CreateUser(user=user)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

# class Query(graphene.ObjectType):
#     pass
