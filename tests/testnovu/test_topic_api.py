import unittest
from unittest.mock import patch, MagicMock
from src.novu.api.topic_api import NovuTopic

class TestNovuTopic(unittest.TestCase):

    def setUp(self):
        self.novu_client = NovuTopic(url="mock_url", api_key="mock_api_key", requests_session=MagicMock())
        self.topic_key = "test_topic"
        self.topic_name = "Test Topic"
        self.subscribers_list = ["subscriber1", "subscriber2"]

    @patch('requests.get')
    def test_get_or_create_topic_existing(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        topic_key = self.novu_client.get_or_create_topic(self.topic_key, self.topic_name)
        self.assertEqual(topic_key, self.topic_key)

    @patch('requests.get')
    @patch('requests.post')
    def test_get_or_create_topic_not_existing(self, mock_post, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        mock_post_response = MagicMock()
        mock_post_response.status_code = 201
        mock_post.return_value = mock_post_response

        topic_key = self.novu_client.get_or_create_topic(self.topic_key, self.topic_name)
        self.assertEqual(topic_key, self.topic_key)

    @patch('requests.post')
    def test_create_topic(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_post.return_value = mock_response

        self.novu_client.create_topic({"key": self.topic_key, "name": self.topic_name})

        # Add your assertions here if needed

    @patch('requests.post')
    def test_add_subscriber_to_topic(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        self.novu_client.add_subscriber_to_topic(self.topic_key, self.subscribers_list)

        # Add your assertions here if needed

    @patch('requests.post')
    def test_delete_subscriber_in_topic(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        self.novu_client.delete_subscriber_in_topic(self.topic_key, "subscriber_id")

        # Add your assertions here if needed

    @patch('requests.delete')
    def test_delete_topic(self, mock_delete):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_delete.return_value = mock_response

        self.novu_client.delete_topic(self.topic_key)
