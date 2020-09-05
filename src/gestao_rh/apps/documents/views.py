from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from .models import Document

class DocumentsCreate(CreateView):
    model = Document
    fields = ['description', 'filename']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.owner_id = kwargs.get('employment_id')

        if form.is_valid():
            return self.form_valid(form)

        return self.form_invalid(form)


class DocumentsDelete(DeleteView):
    model = Document
    success_url = reverse_lazy('employees-list')
