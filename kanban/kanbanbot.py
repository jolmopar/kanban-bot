# Kanban Bot - A Telegram bot to create and manage Kanban boards
# Copyright (C) 2017  jolmopar jose@bytx.ie

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""This module contains the base object that setups the Kanban Bot."""

import logging
import re
import json

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import RegexHandler

class KanbanBot(object):
    """ KanbanBot setups the Handler methods for the Kanban bot and starts polling """

    def __init__(self):
        """ Initialiaze the bot operations:
            - Logging
            - Event Handler
            - Dispatcher
            - Command Handlers
        """
        # Initialize logging
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        # Load config
        self.logger.info("Reading config: <config.json>")
        with open("config.json", "r") as f:
            config = json.loads(f.read())

        # Create the EventHandler and pass it the bot's token.
        self.updater = Updater(token=config.get("token"))

        # Get the dispatcher to register handlers
        self.dp = self.updater.dispatcher

        # Command Handlers
        self.dp.add_handler(CommandHandler('start', self.start))

        # log all errors
        self.dp.add_error_handler(self.log_error)

    def log_error(self, bot, update, error):
        """ Log any errors on the default logger """
        self.logger.error('Update "%s" caused error "%s"' % (update, error))

    def start(self, bot, update):
        """ Display greeting message and bot commands """
        reply = ("Welcome to the Personal Kanban bot.\n"
                 "I'm still being built, but come back in a few days.\n")

        update.message.reply_text(reply, quote=False)

    def start_polling(self):
        """ Start polling for Telegram events """
        self.updater.start_polling()

        # Run the bot until you press Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        self.updater.idle()


def main():
    """ Get the handler bot and start it """
    bot = KanbanBot()
    bot.start_polling()


if __name__ == '__main__':
    main()
