from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import logging

import Config as cfg
from database.database import Database
from cmds.admingroup import Admin

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token=cfg.token)
dispatcher = updater.dispatcher

db = Database()

print("Running")


updater.dispatcher.add_handler(CommandHandler('init', Admin.init))
updater.dispatcher.add_handler(CommandHandler('rules', Admin.rules))
updater.dispatcher.add_handler(CallbackQueryHandler(Admin.button))

def update(bot, update):
    print("Hey")

update_handler = MessageHandler(Filters.text, update)
dispatcher.add_handler(update_handler)



updater.idle()