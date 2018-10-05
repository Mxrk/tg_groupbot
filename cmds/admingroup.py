from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from telegram.ext import ConversationHandler


class Admin:
    def init(bot, update):
        chat_id = update.message.chat_id
        keyboard = [[InlineKeyboardButton("1️⃣", callback_data='connect'),
        InlineKeyboardButton("2️⃣", callback_data='rules')],
        [InlineKeyboardButton("3️⃣", callback_data='log'),
        InlineKeyboardButton("4️⃣", callback_data='test')]]
              
        reply_markup = InlineKeyboardMarkup(keyboard)
        msg = "1️⃣: Connect\n2️⃣: Rules\n3️⃣: Log (activate/deactivate)\n4️⃣: test"
        bot.send_message(chat_id, text=msg, reply_markup=reply_markup)
        return 1
       

    def rules(bot, update):
        chat_id = update.message.chat_id
        keyboard = [[InlineKeyboardButton("Show rules", callback_data='showRules'),
                     InlineKeyboardButton("Change rules", callback_data='changeRules')],
                    [InlineKeyboardButton("Exit", callback_data='exit')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        #update.message.reply_text('What do you want to do?', reply_markup=reply_markup)
        bot.send_message(chat_id, text="test", reply_markup=reply_markup)
        
    def button(bot, update):
        query = update.callback_query
        #rules = Rules.get()

        if query.data == "connect":
            Admin.connect(bot,query)
            #return 1
            #complete connect -> create collection with id
        elif query.data == "rules":
            Admin.rules(bot, query)

        elif query.data == "log":
            bot.edit_message_text(chat_id=query.message.chat_id,
                                  message_id=query.message.message_id, text='2')
        elif query.data == "test":
            bot.edit_message_text(chat_id=query.message.chat_id,
                                  message_id=query.message.message_id, text='3')
            
        elif query.data == "showRules":
            Admin.rules(bot, query)

        elif query.data == "changeRules":
            Admin.rules(bot, query)

        elif query.data == "exit":
            Admin.rules(bot, query)

#todo
    def connect(bot, update):
        chat_id = update.message.chat_id
        bot.send_message(chat_id, text="ID -> maingroup -> /id", reply_markup=ForceReply(force_reply=True))
       #return 1
    
    def cancel(bot, update):
        print("Test")
        return -1



