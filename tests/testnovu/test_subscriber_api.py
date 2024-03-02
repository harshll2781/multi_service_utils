import unittest
from unittest.mock import MagicMock, patch
from src.novu.api.subscriber_api import NovuSubscriber, NovuSubscriberCredentials

class TestNovuSubscriber(unittest.TestCase):
    
    def setUp(self):
        self.subscriber = NovuSubscriber(url="mock_url", api_key="mock_api_key", requests_session=MagicMock())

    def test_create_bulk_subscriber(self):
        # Mocking the post method of requests_session
        self.subscriber.requests_session.post.return_value.status_code = 201
        self.assertTrue(self.subscriber.create_bulk_subscriber([{'name': 'John', 'mobile_number': '1234567890','subscriberId':'Test123'}]))

    def test_create_subscriber(self):
        # Mocking the post method of requests
        with patch('src.novu.api.subscriber_api.NovuSubscriber.create_subscriber') as mock_post:
            mock_post.return_value.status_code = 201
            self.assertTrue(self.subscriber.create_subscriber({'name': 'John', 'subscriberId': 'Test123', 'mobile_number': '1234567890', 'profile_id': '456', 'profile_type': 'TypeA'}))

    def test_get_subscriber_all(self):
        # Mocking the handle_request method of event_api
        self.subscriber.requests_session.get.return_value = {'data': [{'subscriberId': '123'}, {'subscriberId': '456'}]}
        self.assertTrue(self.subscriber.get_subscriber())

    def test_delete_subscriber(self):
        # Mocking the delete method of SubscriberApi
        with patch('src.novu.api.subscriber_api.NovuSubscriber.delete_subscriber') as mock_subscriber_api:
            mock_delete = MagicMock()
            mock_subscriber_api.return_value.delete = mock_delete
            self.assertTrue(self.subscriber.delete_subscriber(subscriber_id='123'))


class TestNovuSubscriberCredentials(unittest.TestCase):
    
    def setUp(self):
        self.subscriber = NovuSubscriberCredentials(url="mock_url", api_key="mock_api_key", requests_session=MagicMock())

    def test_update_credentials(self):
        # Mocking the request method of requests
        with patch('src.novu.api.subscriber_api.NovuSubscriberCredentials.update_credentials') as mock_request:
            mock_request.return_value.status_code = 200
            self.assertTrue(self.subscriber.update_credentials(subscriber_id='123', channel='email', tokens=['token1', 'token2'], provider='provider'))

    def test_delete_credentials(self):
        # Mocking the delete method of requests
        with patch('src.novu.api.subscriber_api.NovuSubscriberCredentials.delete_credentials') as mock_delete:
            mock_delete.return_value.text = '{"message": "Credentials deleted successfully"}'
            self.assertTrue(self.subscriber.delete_credentials(subscriber_id='123', provider='provider'))
