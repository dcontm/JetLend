from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'qualifications', views.QualificationViewSet)
router.register(r'passports', views.PassportViewSet)
router.register(r'documents', views.DocumentViewSet)
router.register(r'investors', views.InvestorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
