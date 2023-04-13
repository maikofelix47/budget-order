from django.views.generic import ListView
from .models import DispatchMessage

# Create your views here.

class DispatchMessagesView(ListView):
    template_name = 'dispatch-messages/index.html'
    model = DispatchMessage
    context_object_name = 'dispatch_messages'
