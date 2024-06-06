from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.views import View
from .forms import BookForm

class BookRecordFormView(FormView):
    template_name='book_form.html'
    form_class=BookForm
    success_url='book_management/entry_success'


    def form_valid(self, form):
        form.save()
        return super() .form_valid(form)
    
class FormSuccessView(View):
    def get(self):
        return HttpResponse("Book record save successfully")
    



