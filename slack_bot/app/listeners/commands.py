import logging
from slack_bolt import Ack, App, Say
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_sdk.models.blocks import (
    ContextBlock,
    DividerBlock,
    HeaderBlock,
    MarkdownTextObject,
    PlainTextObject,
    SectionBlock,
)

from slack_bot.app.views.healthcheck_status_block import healthcheck_status_block

_logger = logging.getLogger(__name__)

def initialize_commands(app: App): 
    @app.command("/ola")
    def ola(ack: Ack, body, say: Say, logger):
        #A test slash command
        
        ack()
        try:
            user_id = body["user_id"]
            say(f"Test successful :success:\n\nUser Name: <@{user_id}>\n\n")
            
        except Exception as ee:
            _logger.error(
                f"An exception was raised while testing: {ee}"
            )
            say(f"Unable to connect")
    
    @app.command("/hello-socket-mode")
    def hello_command(ack, body):
        user_id = body["user_id"]
        ack(f"Hi, <@{user_id}>!")
    
    @app.event("app_mention")
    def event_test(say):
        say("Hi there!")
    
    @app.command("/gcp_healthcheck")
    def gcp_healthcheck(ack, client, payload, context, respond):
        ack()
    
        channel_id: str = payload["channel_id"]
        user_id: str = payload["user_id"]

        try:

            healthcheck_message = healthcheck_status_block(user_id)
            client.chat_postMessage(
                channel = channel_id,
                blocks = healthcheck_message,
                text = "Could not render message.",
            )
            return

        except Exception as e:
            raise ("Error")
