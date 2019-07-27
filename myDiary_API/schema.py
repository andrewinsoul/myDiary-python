import graphene, graphql_jwt
import myDiary_API.apps.authentication.schema as user_schema
import myDiary_API.apps.diary.schema as diary_schema

mutations = (
    user_schema.Mutation,
    diary_schema.Mutation,
)
queries = (
    user_schema.Query,
    diary_schema.Query
)
class Mutation(*mutations, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.relay.Verify.Field()
    referesh_token = graphql_jwt.relay.Refresh.Field()

class Query(*queries, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
