from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from utils.rules import Rules


class Admin:
    def init(bot, update):
        print("Hey")

    def rules(bot, update):
        keyboard = [[InlineKeyboardButton("Show rules", callback_data='1'),
                     InlineKeyboardButton("Change rules", callback_data='2')],
                    [InlineKeyboardButton("Exit", callback_data='3')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('What do you want to do?', reply_markup=reply_markup)

    def button(bot, update):
        query = update.callback_query
        rules = Rules.get()

        if query.data == '1':
            bot.edit_message_text(chat_id=query.message.chat_id,
                                  message_id=query.message.message_id, text=rules)
        elif query.data == '2':
            bot.edit_message_text(chat_id=query.message.chat_id,
                                  message_id=query.message.message_id, text='2')
        elif query.data == '3':
            bot.edit_message_text(chat_id=query.message.chat_id,
                                  message_id=query.message.message_id, text='3')
