from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import logging

import Config as cfg
from database.database import Database
from cmds.admingroup import Admin
from cmds.utils import Utils
from filters.welcomeMessage import WelcomeMessage

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token=cfg.token)
dispatcher = updater.dispatcher

db = Database()

print("Running")


dispatcher.add_handler(CommandHandler('init', Admin.init))
dispatcher.add_handler(CommandHandler('rules', Admin.rules))
dispatcher.add_handler(CommandHandler('id', Utils.id))
dispatcher.add_handler(CallbackQueryHandler(Admin.button))
dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, WelcomeMessage.greeting))

updater.start_polling()
updater.idle()