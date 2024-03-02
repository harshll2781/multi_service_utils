import json
import logging
import requests
from typing import List, Dict
from .novu_client import NovuClient
from novu.api.subscriber import SubscriberApi
from ..utils.helpers import device_id_checked

logger = logging.getLogger(__name__)

class NovuSubscriber(NovuClient):
    """
    A class for managing subscribers in the Novu system.
    """

    def create_bulk_subscriber(self, user_detail:List[dict]):
        """
        Create multiple subscribers in bulk.

        Args:
            user_detail (dict): Details of the subscribers.

        Returns:
            bool: True if creation is successful, False otherwise.
        """
        url = f"{self.url}/v1/subscribers/bulk"
        headers = self.headers
        data = {"subscribers": user_detail}

        response = self.requests_session.post(url, headers=headers, json=data)

        if response.status_code == 201:
            logger.info('Subscribers created successfully')
            return True
        else:
            logger.error(f'Failed to create subscribers: {response.text}')
            return False

    def create_subscriber(self, user_detail:Dict):
        """
        Create a single subscriber.

        Args:
            user_detail (dict): Details of the subscriber.

        Returns:
            bool: True if creation is successful, False otherwise.
        """
        try:

            url = f"{self.url}/v1/subscribers"
            headers = self.headers
            data = {
                "firstName": user_detail.get('name', ''),
                "subscriberId": str(user_detail.get('profile_type_id', '')),
                "phone": user_detail.get('mobile_number', ''),
            }
            if user_detail.get('data'):
                data['data'] = user_detail.get('data')
            response = requests.post(url, headers=headers, json=data)
            logger.info(f'Subscriber created: {response.text}')
            return True
        except Exception as e:
            logger.error(f'Error while creating subscriber: {e}', exc_info=True)
            return False

    def get_subscriber(self):
        """
        Retrieve details of a all subscribers.

        Returns:
            str or bool: Subscriber ID if found, True if all subscribers are retrieved, False otherwise.
        """
        subscriber_ids = self.requests_session.get(url=f'{self.url}/v1/subscribers')
        logger.info(len(subscriber_ids))

        for subscriber_id in subscriber_ids.get('data', []):
            logger.info(f"Subscriber ID: {subscriber_id.get('subscriberId')}")

        return True

    def delete_subscriber(self, subscriber_id:str):
        """
        Delete a subscriber.

        Args:
            subscriber_id (str): ID of the subscriber to delete.

        Returns:
            bool: True if deletion is successful.
        """
        novu = SubscriberApi(self.url, self.api_key).delete(subscriber_id)
        logger.info("Novu Subscriber deleted")
        return True


class NovuSubscriberCredentials(NovuClient):
    def update_credentials(self, subscriber_id: str, channel: str, tokens : List[str], provider: str):
        try:
            url = f"{self.url}/v1/subscribers/{subscriber_id}/credentials"
            token = device_id_checked(tokens)
            payload = {
                "credentials": {
                    "channel": channel,
                    "deviceTokens": token,
                },
                "providerId": provider,
            }
            headers = self.headers
            response = requests.request("PUT", url, json=payload, headers=headers)
            logger.info(f"Updated subscriber credentials - {response.text}")
            return True
        except Exception as e:
            logger.error(f'Error while updating subscriber credentials: {e}', exc_info=True)
            return False

    def delete_credentials(self, subscriber_id: str, provider: str):
        url = f"{self.url}/v1/subscribers/{subscriber_id}/credentials/{provider}"
        headers = self.headers
        response = requests.delete(url, headers=headers)
        logger.info(response.text)
        return True
