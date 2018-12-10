from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from database.database import Database


class Admin(object):
    def init(bot, update):
        chat_id = update.message.chat_id
        if Database().checkIfAdmin(chat_id):
            chat_id = update.message.chat_id
            keyboard = [[InlineKeyboardButton("1️⃣", callback_data='connect'),
                         InlineKeyboardButton("2️⃣", callback_data='rules')],
                        [InlineKeyboardButton("3️⃣", callback_data='log'),
                         InlineKeyboardButton("4️⃣", callback_data='test')]]

            reply_markup = InlineKeyboardMarkup(keyboard)
            msg = "1️⃣: Connect\n2️⃣: Rules\n3️⃣: Log (activate/deactivate)\n4️⃣: test"
            bot.send_message(chat_id, text=msg, reply_markup=reply_markup)
            return 1
        else:
            bot.send_message(chat_id, text="only in admingroup")



    @staticmethod
    def aRules(bot, update):
        chat_id = update.message.chat_id
        if Database().checkIfAdmin(chat_id):
            chat_id = update.message.chat_id
            keyboard = [[InlineKeyboardButton("Show rules", callback_data='showRules'),
                         InlineKeyboardButton("Change rules", callback_data='changeRules')],
                        [InlineKeyboardButton("Exit", callback_data='exit')]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            # update.message.reply_text('What do you want to do?', reply_markup=reply_markup)
            bot.send_message(chat_id, text="test", reply_markup=reply_markup)
        else:
            bot.send_message(chat_id, text="only in admingroup")




    @staticmethod
    def button(bot, update):
        query = update.callback_query
        # rules = Rules.get()

        if query.data == "connect":
            Admin.connect(bot, query)

            # return 1
            # complete connect -> create document with id
        elif query.data == "rules":
            Admin.aRules(bot, query)

        elif query.data == "log":
            bot.edit_message_text(chat_id=query.message.chat_id,
                                  message_id=query.message.message_id, text='2')
        elif query.data == "test":
            bot.edit_message_text(chat_id=query.message.chat_id,
                                  message_id=query.message.message_id, text='3')

        elif query.data == "showRules":
            chat_id = query.message.chat_id
            rules = Database().showRulesAdmin(chat_id)
            if not rules:
                bot.send_message(chat_id, text="No rules yet")
            else:
                bot.send_message(chat_id, text=rules)

        elif query.data == "changeRules":
            Admin.aRules(bot, query)
            Database().createRules(query.message.chat_id, "hi")

        elif query.data == "exit":
            Admin.aRules(bot, query)

    # todo
    @staticmethod
    def connect(bot, update):
        chat_id = update.message.chat_id
        bot.send_message(chat_id, text="ID from maingroup", reply_markup=ForceReply(force_reply=True))

    @staticmethod
    def link(bot, update):
        print(update.message.text)
        # Add ID to database
        if not (Database().connectGroups(update.message.text, update.message.chat_id)):
            bot.send_message(update.message.chat_id, text="already linked")
            return -1
        else:
            bot.send_message(update.message.chat_id, text="linked!")
            return -1

    @staticmethod
    def cancel(bot, update):
        return
