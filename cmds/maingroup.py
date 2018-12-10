from database.database import Database
class Maingroup:

    @staticmethod
    def rules(bot, update):
        chat_id = update.message.chat_id
        if Database().checkIfMain(chat_id):
            rules = Database().showRulesMain(update.message.chat_id)
            if not rules:
                bot.send_message(update.message.chat_id, text="No rules yet")
            else:
                bot.send_message(update.message.chat_id, text=rules)
        else:
            bot.send_message(chat_id, text="Please use /arules instead")



