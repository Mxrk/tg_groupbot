from telegram.ext import BaseFilter

from database.database import Database


class AdminAlert(BaseFilter):

    def filter(self, message):
        if message.text == "@admins":
            return True
        else:
            return False

    @staticmethod
    def admAlert(bot, update):
        chat_id = update.message.chat_id
        x = Database().getAdminGroup(chat_id)
        bot.send_message(x, text="Panic in your group")


Admin_Alert = AdminAlert()
