import logging
import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from slack_bot.app.listeners.commands import initialize_commands

_logger = logging.getLogger(__name__)

def start_app():
    """
    Start the application and initialize listeners.
    """

    _logger.debug("Starting app")

    # An instance of a Slack Bolt App
    app: App = App(token="")

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
    handler: SocketModeHandler = SocketModeHandler(app, "")
    handler.start()

    _logger.debug("Handler started")
