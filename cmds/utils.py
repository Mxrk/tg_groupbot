class Utils:

    def id(bot, update):
        chat_id = update.message.chat_id
        bot.send_message(chat_id, text=chat_id)
