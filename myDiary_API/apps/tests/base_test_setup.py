from django.test import TestCase, RequestFactory
from mixer.backend.django import mixer
from graphene.test import Client


class BaseSetup(TestCase):
    def setUp(self):
        # mixer adds 6 to the argument specified in the cycle function
        self.users = mixer.cycle(3).blend('authentication.User')
        self.diaries = mixer.cycle(3).blend('diary.Diary')
        self.entries = mixer.cycle(3).blend('entry.Entry')

    @staticmethod
    def helper_test_function(api_query, schema, user=None, variable_values=None, **kwargs):
        """
        Returns the results of executing a graphQL query using the graphene test client. 
        This is a helper method for our tests
        """
        request_factory = RequestFactory()
        context_value = request_factory.post('graphql/')
        context_value.user = user
        client = Client(schema)
        executed = client.execute(
            api_query,
            context_value=context_value, 
            variable_values=variable_values,
            **kwargs
        )
        return executed

    @staticmethod
    def helper_test_function_without_auth(api_query, schema, user=None, variable_values=None, **kwargs):
        """
        Returns the results of executing a graphQL query using the graphene test client. 
        This is a helper method for our tests
        """
        request_factory = RequestFactory()
        context_value = request_factory.post('graphql/')
        context_value.user = user
        client = Client(schema)
        executed = client.execute(
            api_query,
            context_value={'user': user}, 
            variable_values=variable_values,
            **kwargs
        )
        return executed
