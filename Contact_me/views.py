from django.views.generic.edit import CreateView
from Contact_me.forms import messageform

class contact_me_view(CreateView):
    form_class = messageform
    template_name = "Contact_me/contact.html"

    def get_success_url(self):
        return ''