import json
from ...schema import schema
from graphene_django.utils.testing import GraphQLTestCase
from ..tests.base_test_setup import BaseSetup
from mixer.backend.django import mixer
from graphql.error.located_error import GraphQLLocatedError
from graphql import GraphQLError
from unittest.mock import patch
from graphql_relay import to_global_id

class DiaryTestCase(BaseSetup, GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    def test_create_diary_mutation_success(self):
        query = '''
            mutation createDiary {
                createDiary(input: {
                    diary: {
                        name: "Diary name"
                        isPrivate: "False"
                        description: "Diary description goes here"
                    }
                })
                {
                    newDiary {
                        name
                        description
                        isPrivate
                    }
                }
            }

        '''
        response = BaseSetup.helper_test_function(query, schema, self.users[0])
        self.assertEqual('Diary name', response['data']['createDiary']['newDiary']['name'])
        self.assertIn('newDiary', response['data']['createDiary'])
