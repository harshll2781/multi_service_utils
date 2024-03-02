import unittest
from unittest.mock import patch, MagicMock
from src.novu.api.event_api import NovuNotification

class TestNovuNotification(unittest.TestCase):

    def setUp(self):
        self.novu_client = NovuNotification(url="mock_url", api_key="mock_api_key", requests_session=MagicMock())
        self.name = "test_workflow"
        self.recipients = [{"type": "email", "email": "test@example.com"}]
        self.payload = {"title": "Test Title", "message": "Test Message", "overrides": {"key": "value"}}
        self.topic_key = "test_topic"
        self.subscriber_id = "test_subscriber_id"

    @patch('src.novu.api.event_api.NovuNotification.novu_send_notification')
    def test_novu_send_notification(self, mock_trigger):
        mock_trigger.return_value = MagicMock()

        result = self.novu_client.novu_send_notification(self.name, self.recipients, self.payload, {})
        self.assertTrue(result)

    @patch('src.novu.api.event_api.NovuNotification.novu_send_bulk_notification')
    def test_novu_send_bulk_notification(self, mock_trigger_bulk):
        mock_trigger_bulk.return_value = MagicMock()

        result = self.novu_client.novu_send_bulk_notification(["workflow1", "workflow2"], self.recipients)
        self.assertTrue(result)

    @patch('src.novu.api.event_api.NovuNotification.novu_send_to_topic')
    def test_novu_send_to_topic(self, mock_trigger):
        mock_trigger.return_value = MagicMock()

        result = self.novu_client.novu_send_to_topic(self.name, self.topic_key, self.payload, {})
        self.assertTrue(result)

