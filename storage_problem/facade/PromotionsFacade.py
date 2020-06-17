import json

from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, HttpResponseBadRequest

from storage_problem.facade.dtos.PromotionDto import PromotionDto
from storage_problem.services import PromotionRelationService, PromotionService
from django.conf import settings
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT


class PromotionFacade(TemplateView):
    def __init__(self):
        self.promotion_service = PromotionRelationService.PromotionRelationService() if settings.USE_RELATIONAL_DB else PromotionService.PromotionService()
        print(settings.USE_RELATIONAL_DB)
    def get(self, request, id, *args, **kwargs):
        promotion = self.promotion_service.get(id)
        if id in cache: 
            result = cache.get(id)
            HttpResponse(result, content_type='application/json')
        if promotion:
            result = PromotionDto(external_id=promotion.external_id,
                                  price=promotion.price, expiratino_date=promotion.expiration_date)
            cache.set(id,json.dumps(result.to_json()),timeout = DEFAULT_TIMEOUT)
            return HttpResponse(json.dumps(result.to_json()), content_type='application/json')
        else:
            return HttpResponseNotFound('promotion not found')
