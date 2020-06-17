from django.views.generic import TemplateView
from storage_problem.tasks.tasks import load_direct_from_csv, load_data
from django.http import HttpResponse

class LoadTrigerFacade(TemplateView):
    def get(self, request, *args, **kwargs):
        load_data.delay()
        return HttpResponse("ok")