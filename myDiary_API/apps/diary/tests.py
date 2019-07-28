import json
from ...schema import schema
from graphene_django.utils.testing import GraphQLTestCase
from ..tests.base_test_setup import BaseSetup
from mixer.backend.django import mixer
from graphql.error.located_error import GraphQLLocatedError
from graphql import GraphQLError
from unittest.mock import patch
from graphql_jwt.testcases import JSONWebTokenTestCase
from graphql_relay import to_global_id

class DiaryTestCase(BaseSetup, GraphQLTestCase, JSONWebTokenTestCase):
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

    def test_query_get_public_diaries(self):
        response = self.query(
            '''
            query {
                publicDiaries {
                    edges {
                        node {
                            description
                            name
                            isPrivate
                        }
                    }
                }
            }
            ''',
            op_name='public diaries'
        )
        content = json.loads(response.content)
        data = content['data']['publicDiaries']['edges']
        self.assertResponseNoErrors(response)
        self.assertEqual(
            data[0].get('node').get('isPrivate'),
            False
        )
        self.assertEqual(
            data[-1].get('node').get('isPrivate'),
            False
        )

    def test_query_my_diaries(self):
        query = '''
            query my_diaries{
                myDiaries {
                    edges {
                        node {
                            description
                            name
                            isPrivate
                            user {
                                username
                            }
                        }
                    }
                }
            }
        '''
        self.client.authenticate(self.users[0])
        response = BaseSetup.helper_test_function(query, schema, self.users[0])
        username = self.users[0].username
        self.assertEqual(
            response['data']
            ['myDiaries']
            ['edges'][0]
            ['node']
            ['user']
            ['username'],
            username
        )
        self.assertEqual(
            response['data']
            ['myDiaries']
            ['edges']
            [-1]
            ['node']
            ['user']
            ['username'],
            username
        )

    def test_query_get_a_diary(self):
        query = f'''
            query get_a_diary {{
                diary(id: {self.diaries[0].id}) {{
                    name
                    description
                    isPrivate
                }}
            }}
        '''
        response = BaseSetup.helper_test_function(query, schema, self.users[0])
        self.assertNotIn('edges', response['data'])
        self.assertEqual(
            response['data']['diary']['isPrivate'],
            False
        )
