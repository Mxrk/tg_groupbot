from database.database import Database


class NewMember:

    @staticmethod
    def joinAlert(bot, update):
        print("Join alert")
        # if new member log activated
        for members in update.message.new_chat_members:
            chat_id = Database().getAdminGroup(update.message.chat_id)
            s = "A new member joined your group:\nID: {id}\nUsername: @{username}"
            bot.send_message(chat_id, text=s.format(id=members.id, username=members.username))

    @staticmethod
    def greeting(bot, update):
        chat_id = update.message.chat_id
        user = update.message.from_user
        msg = "Welcome to the group, {0}!".format(user.first_name)
        bot.send_message(chat_id, text=msg)

