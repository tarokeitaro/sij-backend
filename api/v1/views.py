from rest_framework import viewsets, permissions
from baseApp.models import User, Profile
from sijApp.models import (
    Country, Language, Currency, Institution, Track,
    PublishPeriod, ColStyle, Rank, Journal
)
from .serializers import (
    UserSerializer, ProfileSerializer, CountrySerializer, LanguageSerializer,
    CurrencySerializer, InstitutionSerializer, TrackSerializer,
    PublishPeriodSerializer, ColStyleSerializer, RankSerializer,
    JournalSerializer
)

# User & Profile
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.select_related('user').all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


# Master data sederhana
class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PublishPeriodViewSet(viewsets.ModelViewSet):
    queryset = PublishPeriod.objects.all()
    serializer_class = PublishPeriodSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ColStyleViewSet(viewsets.ModelViewSet):
    queryset = ColStyle.objects.all()
    serializer_class = ColStyleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RankViewSet(viewsets.ModelViewSet):
    queryset = Rank.objects.all()
    serializer_class = RankSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Journal
class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.select_related(
        'institution','rank','currency','country','language','col_style'
    ).prefetch_related('publish_period','track').all()
    serializer_class = JournalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]