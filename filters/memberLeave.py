from database.database import Database


class MemberLeave:

    @staticmethod
    def leaveAlert(bot, update):
        member = update.message.left_chat_member
        chat_id = Database().getAdminGroup(update.message.chat_id)
        s = "A member left your group:\nID: {id}\nUsername: @{username}"
        bot.send_message(chat_id, text=s.format(id=member.id, username=member.username))

