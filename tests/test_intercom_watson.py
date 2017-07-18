from service_tests.service_test_case import NioServiceTestCase
from nio.signal.base import Signal

from unittest.mock import ANY, MagicMock, patch


class TestIntercomWatson(NioServiceTestCase):

    service_name = 'IntercomWatson'

    def env_vars(self):
        return {
            'INTERCOM_ACCESS_TOKEN': 'accessToken',
            'INTERCOM_CALLBACK_URL': 'callbackUrl',
            'BLUEMIX_PASSWORD': 'password',
            'BLUEMIX_USERNAME': 'username',
            'SLACK_API_TOKEN': 'apiToken',
        }

    def mock_modules(self):
        pass

    def setUp(self):
        self.mock_modules()
        super().setUp()

    # TEST:
    # Intercom message pings watson
    # Intercom message posts to slack
    # MergeState and Filter blocks work
    def test_function(self):
        self.assertTrue(True)

