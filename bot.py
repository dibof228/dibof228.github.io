from slixmpp import ClientXMPP


class Bot(ClientXMPP):
    def __init__(self, jid, password):
        ClientXMPP.__init__(self, jid, password)

        self.add_event_handler("session_start", self.start)
        self.add_event_handler("message", self.message)


    def start(self, event):
        self.send_presence()
        self.get_roster()

    def message(self, msg):
        if msg['type'] in ('chat', 'normal'):
            message_text = msg['body']
            if "/info" in message_text.lower():
                reply = "Бот написан dibil228@xmpp.jp для Jabber, сам бот создан чтобы ты пообщаться со мной."
                msg.reply(reply).send()
            else:
                reply = "Ждите когда вам ответят :)"
                msg.reply(reply).send()      

if __name__ == '__main__':
    xmpp = Bot("dibofbot@xmpp.jp", "Не дам пароль")
    xmpp.connect()
    xmpp.process()

