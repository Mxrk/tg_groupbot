class WelcomeMessage:

    def greeting(bot, update):
        chat_id = update.message.chat_id
        user = update.message.from_user
        msg = "Welcome to the group, {0}!".format(user.first_name)
        bot.send_message(chat_id, text=msg)
