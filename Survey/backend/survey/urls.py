"""
- url처리 담당
"""

from django.urls import path, include, re_path
from rest_framework import routers
from . import views
from django.views.generic import TemplateView


router = routers.DefaultRouter()
router.register(r"survey", views.SurveyViewSet)
router.register(r"detail", views.DetailViewSet)
router.register(r"response", views.ResponseViewSet)

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="add"),
    re_path(r"^.*", TemplateView.as_view(template_name="index.html")),
    path("list/", views.SurveyViewSet.as_view({"get": "list_view"}), name="list"),
    path("response/<int:pk>/", views.ResponseViewSet.as_view({"get": "response_view"}), name="response"),
    path("detail/<int:pk>/", views.DetailViewSet.as_view({"get": "detail_view"}), name="detail"),
    # api/내에 router에 등록된 경로들을 모두 등록
    path("api/", include(router.urls)),
]
