from .api import API


class Message(API):
    
    def __init__(self, options):
        pass

    def send(self, from_email, to_email, subject, body, **kwargs):
        options = {}
        api_response = self.post('messages/send', options)
