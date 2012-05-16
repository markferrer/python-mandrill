from .messages import Message

import simplejson as json
import requests


class Mandrill(object):
    """
    Mandrill client object
    """
    
    def __init__(self, api_key, from_email=None):
        self.api_key = api_key
        self.from_email = from_email
        
        # API objects
        self.message = None
        self.template = None
        self.tags = None
        self.users = None

    def users(self):
        if not self.user:
            self.user = User(self.api_key)
        return self.user

    def messages(self):
        if not self.message:
            self.message = Message(self.api_key)
        return self.message

    def tags(self):
        if not self.tag:
            self.tag = Tag(self.api_key)
        return self.tag

    def templates(self):
        if not self.template:
            self.template = Template(self.api_key)
        return self.template

    # Convenience methods
    def send_mail(self, options):  
        """
        Send an e-mail
        """

        api_method_url = self.api_url + 'messages/send.json'
        return

    def send_template(self, options):
        """
        Send an e-mail using a template stored in Mandrill
        """

        api_method_url = self.api_url + 'messages/send_template.json'

        message = Message(api_key, options)
        api_response = message.send_template()

        if api_response == 'true':
            result = True
        else:
            result = False

        return result
