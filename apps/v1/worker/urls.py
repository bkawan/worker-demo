from django.urls import path

from apps.v1.worker.api import UnitListByWorkerListAPI, VisitCreateAPI

api_urls = [
    path('units-by-worker/', UnitListByWorkerListAPI.as_view()),
    path('visits/create/', VisitCreateAPI.as_view()),
]
urlpatterns = []
urlpatterns += api_urls
