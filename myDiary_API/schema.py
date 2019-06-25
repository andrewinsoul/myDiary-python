import graphene, graphql_jwt
import myDiary_API.apps.authentication.schema as user_schema

class Mutation(user_schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.relay.Verify.Field()
    referesh_token = graphql_jwt.relay.Refresh.Field()

class Query(user_schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
