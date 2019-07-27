import json
from ...schema import schema
from graphene_django.utils.testing import GraphQLTestCase
from ..tests.base_test_setup import BaseSetup
from graphql_relay import to_global_id
from ..authentication.models import UserManager

class UserTestCase(BaseSetup, GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    def test_query_all_users(self):
        response = self.query(
            '''
            query {
                users {
                    edges {
                        node {
                            id
                            username
                            fname
                        }
                    }
                }
            }
            ''',
            op_name='all users'
        )
        content = json.loads(response.content)
        data = content['data']['users']['edges']
        self.assertResponseNoErrors(response)
        self.assertEqual(response.status_code, 200)

    def test_query_a_user(self):
        response = self.query(
            f'''
            query {{
                user(id: "{to_global_id("UserNode", self.users[0].id)}") {{
                    username
                    email
                    fname
                }}
            }}
            ''',
            op_name='single user'
        )
        content = json.loads(response.content)
        data = content['data']
        self.assertResponseNoErrors(response)
        self.assertEqual(len(data), 1)
        self.assertEqual(response.status_code, 200)

    def test_create_user_mutation(self):
        response = self.query(
            '''
            mutation createUser($input: CreateUserInput!) {
                createUser(input: $input) {
                    newUser {
                        username
                        email
                        fname
                        lname
                    }
                }
            }
            ''',
            op_name='add user',
            input_data={
                "user": {
                    'username': 'username1',
                    'email': 'andrewinsoul@gmail.com',
                    'fname': 'Andrew',
                    'lname': 'Okoye',
                    'password': 'password1'
                }
            }
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['data']['createUser']['newUser']['username'], 'username1')
        self.assertEqual(content['data']['createUser']['newUser']['email'], 'andrewinsoul@gmail.com')
        self.assertEqual(content['data']['createUser']['newUser']['fname'], 'Andrew')
        self.assertEqual(content['data']['createUser']['newUser']['lname'], 'Okoye')

    def test_create_user(self):
        user = UserManager()
        with self.assertRaises(TypeError) as error:
            user.create_user(None, 'andrewinsoul@gmail.com')
        exception = error.exception
        self.assertEqual(exception.args[0], 'Users must have a username')

        with self.assertRaises(TypeError) as error:
            user.create_user('andyjs', None)
        exception = error.exception
        self.assertEqual(exception.args[0], 'Users must have an email address')

    def test_create_superuser(self):
        user = UserManager()
        with self.assertRaises(TypeError) as error:
            user.create_superuser('andy', 'andrewinsoul@gmail.com', None)
        exception = error.exception
        self.assertEqual(exception.args[0], 'Superusers must have a password.')
