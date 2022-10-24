from twilio.rest import Client

TWILIO_SID = "AC4d924864212383a8ddb4499b43aef02f"
TWILIO_AUTH_TOKEN = "a5e349374f0548b5bfb185e8fb6dc03d"
TWILIO_VIRTUAL_NUMBER = "+12135893147"
TWILIO_VERIFIED_NUMBER = "+237672944309"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
