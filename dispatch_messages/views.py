from __future__ import print_function
from django.views.generic import ListView
from .models import DispatchMessage
from django.http import HttpResponseBadRequest

#sms 
from telesign.messaging import MessagingClient
import environ
# Initialise environment variables
env = environ.Env()

# Create your views here.

class DispatchMessagesView(ListView):
    template_name = 'dispatch-messages/index.html'
    model = DispatchMessage
    context_object_name = 'dispatch_messages'

def send_dispatch_sms(mobile,message):
    customer_id = env('CUSTOMER_ID')
    api_key = env('API_KEY')
    message_type = env('MESSAGE_TYPE')
    print(customer_id,api_key,message_type)
    messaging = MessagingClient(customer_id, api_key)
    try:
        mobile = '254' + mobile
        response = messaging.message(mobile, message, message_type)
        return response
    except:
        return HttpResponseBadRequest('Something went wrong')
