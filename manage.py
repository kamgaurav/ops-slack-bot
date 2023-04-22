import logging
from slack_bot.app.app import start_app

_logger = logging.getLogger(__name__)

if __name__ == "__main__":
    start_app()