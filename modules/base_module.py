class BaseModule:
    def __init__(self, ):
        pass

    def send(self, update, context, text: str):
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)
