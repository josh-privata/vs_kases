"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from case.forms import CaseCreateForm, CaseEditForm, CaseNoteCreateForm
from case.models import Case, CaseNote
from django.http import JsonResponse
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView, TemplateView
from django.urls import reverse_lazy
from case.tables import CaseTable, FullCaseTable
from django_tables2 import RequestConfig, SingleTableView
from django.urls import reverse


class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response
        
# Case Main
class CaseHome(TemplateView):
    template_name = 'case/case_index.html'

    #def dispatch(self, request, *args, **kwargs):
    #    if not request.user.is_authenticated:
    #        return render(request, 'templates/registration/login.html')
    #    else:
    #        return super(CaseHome, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CaseHome, self).get_context_data(**kwargs)
        cases = Case.objects.all()
        context['cases'] = cases
        case_history = []
        history_count = 0
        for case in cases:
            case_history.append(case.history.most_recent())
            history_count += 1
        context['case_history'] = case_history
        context['history_count'] = history_count
        context['active_count'] = Case.objects.filter(status__title__icontains='active').count()
        context['all_count'] = Case.objects.count()
        return context


class CaseDetail(DetailView):

    model = Case
    template_name_suffix = '_detail'

    def get_context_data(self, **kwargs):
        context = super(CaseDetail, self).get_context_data(**kwargs)
        return context


class CaseCreate(CreateView):
    model = Case
    template_name_suffix = '_create'
    form_class=CaseCreateForm

    def get_success_url(self, **kwargs):
        return reverse('case_detail', kwargs={'pk': self.object.pk})


class CaseUpdate(UpdateView):
    model = Case
    form_class=CaseEditForm
    #fields = ['title', 'reference', 'background', 'location', 'description', 'brief', 'comment', 'private', 'type', 'status',
    #             'classification', 'priority', 'authorisation', 'image_upload']
    template_name_suffix = '_update'


class CaseDelete(DeleteView):
    model = Case
    success_url = reverse_lazy('case_list')


# Case Notes
class CaseNoteCreate(CreateView):
    model = CaseNote
    template_name_suffix = 'note_create'
    form_class=CaseNoteCreateForm

    def get_success_url(self, **kwargs):
        return reverse("case_detail", kwargs={'pk': self.object.pk})

    def get(self, request, *args, **kwargs):
        self.object = None
        case_pk = kwargs.get('casepk')
        case = get_object_or_404(Case, pk=case_pk)
        context_data = self.get_context_data()
        context_data.update(case=case)
        return self.render_to_response(context_data)  


#class CaseNoteUpdate(UpdateView):
#    model = CaseNote
#    form_class=CaseNoteEditForm
#    #fields = ['title', 'reference', 'background', 'location', 'description', 'brief', 'comment', 'private', 'type', 'status',
#    #             'classification', 'priority', 'authorisation', 'image_upload']
#    template_name_suffix = 'note_update'


#class CaseNoteDelete(DeleteView):
#    model = CaseNote
#    success_url = reverse_lazy('casenote_list')


# Case Tasks


# Case Displays
class CaseTable(SingleTableView):

    model = Case
    table_class = CaseTable
    table_data=Case.objects.all()


class CaseList(ListView):
    
    def get(self, request):
            try:
                case_ids = []
                cases = []
                for case in Case.objects.all():
                    case_ids.append(case.pk)
                    cases = Case.objects.filter(pk__in=case_ids)
            except Case.DoesNotExist:
                cases = []
            return render(request, 'case/case_list.html', {
                'cases_list': cases,
            })
