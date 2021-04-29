from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from rent.forms import RentForm
from rent.models import RentBook
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class RentHistory(ListView):
    template_name = 'rent/rentview.html'
    model = RentBook
    context_object_name = 'rent'

    def get_queryset(self):
        return RentBook.objects.all()


@method_decorator(login_required, name='dispatch')
class AddRent(SuccessMessageMixin, CreateView):
    model = RentBook
    template_name = 'rent/addrent.html'
    success_url = reverse_lazy('add_rent')
    form_class = RentForm

    def get_success_message(self, cleaned_data):
        return 'Your order has been successfully registered!'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


