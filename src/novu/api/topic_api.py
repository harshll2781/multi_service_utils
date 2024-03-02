import logging
import requests
from typing import Dict,List
from .novu_client import NovuClient

logger = logging.getLogger(__name__)


class NovuTopic(NovuClient):
    """
    A class for managing topics in the Novu system.
    """

    def get_or_create_topic(self, topic_key: str, name: str):
        """
        Get or create a topic.

        Args:
            topic_key (str): The key of the topic.
            name (str): The name of the topic.

        Returns:
            str: The topic key.
        """
        url = f"{self.url}/v1/topics/{topic_key}"
        headers = self.headers

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            logger.info(f"Topic Key Found --> {topic_key}")
        else:
            logger.info(f"Topic Key Not Found --> {topic_key}")
            payload = {"key": topic_key, "name": name}
            self.create_topic(payload=payload)
            logger.info(f"Topic Key created --> {topic_key}")

        return topic_key

    def create_topic(self, payload:Dict):
        """
        Create a new topic.

        Args:
            payload (dict): The payload containing topic details.
        """
        url = f"{self.url}/v1/topics"
        headers = self.headers

        response = requests.post(url, json=payload, headers=headers)
        logger.info(response.text)

    def add_subscriber_to_topic(self, topic_key:str, subscribers_list:List[str]):
        """
        Add subscribers to a topic.

        Args:
            topic_key (str): The key of the topic.
            subscribers_list (list): List of subscribers to add.
        """
        url = f"{self.url}/v1/topics/{topic_key}/subscribers"
        payload = {"subscribers": subscribers_list}
        headers = self.headers

        response = requests.post(url, json=payload, headers=headers)
        logger.info(response.text)

    def delete_subscriber_in_topic(self, topic_key: str, subscribers_id:str):
        """
        Remove subscribers from a topic.

        Args:
            topic_key (str): The key of the topic.
            subscribers_id (list): List of subscriber IDs to remove.
        """
        url = f"{self.url}/v1/topics/{topic_key}/subscribers/removal"
        payload = {"subscribers": subscribers_id}
        headers = self.headers

        response = requests.post(url, json=payload, headers=headers)
        logger.info(response.text)

    def delete_topic(self, topic_key:str):
        """
        Delete a topic.

        Args:
            topic_key (str): The key of the topic.
        """
        url = f"{self.url}/v1/topics/{topic_key}"
        headers = self.headers

        response = requests.delete(url=url, headers=headers)
        logger.info(response.text)
