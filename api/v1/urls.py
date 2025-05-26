from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    UserViewSet, ProfileViewSet, CountryViewSet, LanguageViewSet,
    CurrencyViewSet, InstitutionViewSet, TrackViewSet, PublishPeriodViewSet,
    ColStyleViewSet, RankViewSet, JournalViewSet
)

router = DefaultRouter()
# Auth
router.register('users',           UserViewSet,           basename='user')
router.register('profiles',        ProfileViewSet,        basename='profile')
# Master data
router.register('countries',       CountryViewSet)
router.register('languages',       LanguageViewSet)
router.register('currencies',      CurrencyViewSet)
router.register('institutions',    InstitutionViewSet)
router.register('tracks',          TrackViewSet)
router.register('publish-periods', PublishPeriodViewSet,  basename='publishperiod')
router.register('col-styles',      ColStyleViewSet)
router.register('ranks',           RankViewSet)
# Journals
router.register('journals',        JournalViewSet)

urlpatterns = [
    # JWT endpoints
    path('token/',         TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(),    name='token_refresh'),
    # semua ViewSet di-atas
    path('', include(router.urls)),
]