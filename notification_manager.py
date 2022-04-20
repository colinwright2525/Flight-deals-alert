from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = 'ACaf9a1e1fe96fe6ee2a1689eef9f6deae'
        self.auth_token = '4ce9b817b585e75015227d315b6b3f7a'

    def send_alert(self, message):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
            .create(
            body=message,
            from_='+17164513178',
            to='+17175377883'
        )
        print(message.status)