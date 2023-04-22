import logging
import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

#from slack_bot.app.listeners.actions import initialize_actions
from slack_bot.app.listeners.commands import initialize_commands
#from slack_bot.app.listeners.events import initialize_events
#from slack_bot.app.listeners.messages import initialize_messages
#from slack_bot.app.listeners.options import initialize_options
#from slack_bot.app.listeners.shortcuts import initialize_shortcuts
#from slack_bot.app.listeners.views import initialize_views
#from slack_bot.app.view_handlers.view_handler_factory import ViewHandlerFactory
#from slack_bot.app.views.view_factory import ViewFactory
#from slack_bot.settings import get_settings


#slack_token, signing_secret = get_settings()
_logger = logging.getLogger(__name__)

def start_app():
    """
    Start the application and initialize listeners.
    """

    _logger.debug("Starting app")

    # An instance of a Slack Bolt App
    app: App = App(token="xoxb-4070239670581-5127802763281-sqy3XGtmO4zfUXB34A8aLtUb")

    if not app:
        _logger.error("App could not be started")

    initialize_commands(app)
    #initialize_events(app)
    #initialize_messages(app)
    #initialize_actions(app)
    #initialize_shortcuts(app)
    #initialize_views(app)
    #initialize_options(app)

    #_logger.debug(f"Views: {ViewFactory.view_registry}")
    #_logger.debug(f"View Handlers: {ViewHandlerFactory.view_handler_registry}")

    # Use the built-in Socket Mode Handler
    handler: SocketModeHandler = SocketModeHandler(app, "xapp-1-A053A6VDJJ1-5127824116689-04516f307c24577b6a29ed32b9b7e062d67bf4b0c2d350bfc21403b68ffdedca")
    handler.start()

    _logger.debug("Handler started")
