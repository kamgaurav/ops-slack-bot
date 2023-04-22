import logging

import requests

from slack_bot.constants import(
    api_host
)

_logger = logging.getLogger(__name__)

class healthcheck_data:
    def __init__(self):
        self.server = api_host

    def get_healthcheck_data(self):
        try:
            url = f"http://{self.server}/GCP_Updates/us-west1"
            req = requests.get(url)
            response_data = req.json() if req.status_code == 200 else {}
            return response_data
        except Exception as e:
            _logger.error(f"Exception raised while connecting url: {e}")
            raise ("Error")
        