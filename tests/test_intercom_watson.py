from service_tests.service_test_case import NioServiceTestCase
from nio.signal.base import Signal

from unittest.mock import ANY, MagicMock, patch


class TestIntercomWatson(NioServiceTestCase):

    service_name = 'IntercomWatsonDemo'

    def setUp(self):
        with patch('blocks.slack.slack_block.Slacker') as patched_slack:
            self.mocked_slack = MagicMock()
            patched_slack.return_value.chat.post_message = self.mocked_slack
            super().setUp()

    def env_vars(self):
        return {
            'INTERCOM_ACCESS_TOKEN': 'accessToken',
            'INTERCOM_CALLBACK_URL': 'callbackUrl',
            'BLUEMIX_PASSWORD': 'password',
            'BLUEMIX_USERNAME': 'username',
            'SLACK_API_TOKEN': 'apiToken',
        }

    def mock_blocks(self):
        return {
            "IntercomDemo": lambda signals: None,
            "IntercomAnalysis": lambda signals: self.notify_signals(
                "IntercomAnalysis", [Signal({
                    "document_tone": {
                        "tone_categories": [{
                            "category_id": "emotion_tone",
                            "tones": [{"tone_name": "Anger", "score": 0.51},
                                      {"tone_name": "Disgust", "score": 0.40}]
                        }]
                    }
                })]
            )
        }

    def test_slack_post(self):

        self.notify_signals(
            "IntercomDemo", [Signal({
                "data": {
                    "item": {
                        "conversation_message": {
                            "body": "<p>Hello!</p>"
                        }
                    }
                }
            })]
        )
        self.wait_for_processed_signals("PostIntercomToSlack", 1)

        self.assertEqual(self.mocked_slack.call_count, 1)
        self.assertEqual(self.mocked_slack.call_args_list[0][0],
              ("#intercom_alerts", "Hello!"))


