from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler, \
    RegexHandler
import logging

import Config as cfg
from cmds.admingroup import Admin
from cmds.utils import Utils
from filters.welcomeMessage import WelcomeMessage
from cmds.maingroup import Maingroup
from filters.adminAlert import Admin_Alert, AdminAlert

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater = Updater(token=cfg.token)
dispatcher = updater.dispatcher

print("Running")

dispatcher.add_handler(CommandHandler('arules', Admin.aRules))
dispatcher.add_handler(CommandHandler('id', Utils.id))
dispatcher.add_handler(CallbackQueryHandler(Admin.button))
dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, WelcomeMessage.greeting))
dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler('init', Admin.init)],
    states={1: [RegexHandler(r'-?\d+', Admin.link)]},
    fallbacks=[]
))

dispatcher.add_handler(MessageHandler(Admin_Alert, AdminAlert.admAlert))
dispatcher.add_handler(CommandHandler('rules', Maingroup.rules))

updater.start_polling()
updater.idle()
