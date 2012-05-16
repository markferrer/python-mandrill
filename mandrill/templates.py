from .api import API


class Template(API):
    
    def __init__(self):
        pass

    def send(self, from_email, to_email, subject, template_name, **kwargs):
        options = {}
        api_response = self.post('templates/send-template', options)
