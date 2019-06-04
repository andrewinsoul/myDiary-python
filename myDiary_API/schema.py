import graphene

import apps.authentication.schema as user_schema

class Query(user_schema.Query, graphene.ObjectType):
    pass

class Mutation(user_schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
