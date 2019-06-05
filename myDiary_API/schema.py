import graphene
import myDiary_API.apps.authentication.schema as user_schema

class Mutation(user_schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(mutation=Mutation)
