import os
import requests
from novu.api import EventApi

class NovuClient:
    def __init__(self, url:str, api_key:str, requests_session = None) -> None:
        self.url = url
        self.api_key = api_key
        self.event_api = EventApi(url, api_key)
        self.headers = {"Content-Type": "application/json", "Authorization": f"ApiKey {self.api_key}"}
        self.requests_session = requests_session
        super().__init__()
