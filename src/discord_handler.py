import requests
import json

class MessengerHandler :

    def __init__ (self, page_access_token) :

        self.page_acces_token = page_access_token


    def send_message (self, recipient_id, message_text) : 

        message_data = {
            'recipient' :  {'id' : recipient_id},
            'message' : {'text' : message_text}
        }

        headers = {'Content-Type' : 'application/json'}
        params = 
