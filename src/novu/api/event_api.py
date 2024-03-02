import logging
from typing import List,Dict
from .novu_client import NovuClient
from novu.dto.event import InputEventDto


logger = logging.getLogger(__name__)

class NovuNotification(NovuClient):
    """
    A class for managing notifications in the Novu system.
    """

    def novu_send_notification(self, name:str, recipients:List[str], payload:Dict, overrides:Dict):
        """
        Send a notification to one or more recipients.

        Args:
            name (str): The name of the workflow.
            recipients (list): List of recipient details.
            payload (dict): The notification payload.
            overrides (dict): Overrides for the notification.

        Returns:
            bool: True if the notification is sent successfully.
        """
        resp = self.event_api.trigger(
            name=name,
            recipients=recipients,
            payload=payload,
            overrides=overrides
        )
        logger.info(f"Notification Sent Response -> {resp}")
        return True

    def novu_send_bulk_notification(self, name_list:List[str], recipients:list[str]):
        """
        Send bulk notifications to multiple recipients.

        Args:
            name_list (list): List of workflow names.
            recipients (list): List of recipient details.

        Returns:
            bool: True if the bulk notification is sent successfully.
        """
        event1 = InputEventDto(
            name=name_list[0],
            recipients=recipients,
            payload={}
        )
        event2 = InputEventDto(
            name=name_list[1],
            recipients=recipients,
            payload={}
        )

        novu = self.event_api.trigger_bulk(
            events=[event1, event2]
        )
        logger.info(novu)
        return True

    def novu_send_to_topic(self, name, topic_key:str, payload:Dict, overrides:Dict):
        """
        Send a notification to a topic.

        Args:
            name (str): The name of the workflow.
            topic_key (str): The key of the topic.
            payload (dict): The notification payload.
            overrides (dict): Overrides for the notification.

        Returns:
            bool: True if the notification is sent successfully.
        """
        resp = self.event_api.trigger(
            name=name,
            recipients=[{"type": "Topic", "topicKey": topic_key}],
            payload=payload,
            overrides=overrides
        )
        logger.info(f"Notification Sent Response -> {resp}")
        return True
