from rest_framework import serializers
from baseApp.models import User, Profile
from sijApp.models import (
    Country, Language, Currency, Institution, Track,
    PublishPeriod, ColStyle, Rank, Journal
)

# --- User & Profile ---
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'interest', 'birth', 'created_on', 'last_modified']

class UserSerializer(serializers.ModelSerializer):
    user_profile = ProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'user_profile']


# --- Master data sederhana ---
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'name']

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['id', 'name', 'alpha_code', 'symbol']

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ['id', 'name', 'desc', 'slug']

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id', 'name', 'desc']

class PublishPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublishPeriod
        fields = ['id', 'month']

class ColStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColStyle
        fields = ['id', 'name', 'desc', 'slug']

class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rank
        fields = ['id', 'name', 'desc', 'slug']


# --- Journal dengan relasi ---
class JournalSerializer(serializers.ModelSerializer):
    # jika ingin nested representations, uncomment baris berikut:
    institution     = InstitutionSerializer(read_only=True)
    rank            = RankSerializer(read_only=True)
    publish_period  = PublishPeriodSerializer(many=True, read_only=True)
    track           = TrackSerializer(many=True, read_only=True)
    currency        = CurrencySerializer(read_only=True)
    country         = CountrySerializer(read_only=True)
    language        = LanguageSerializer(read_only=True)
    col_style       = ColStyleSerializer(read_only=True)

    class Meta:
        model = Journal
        fields = [
            'id', 'institution', 'rank', 'cover', 'name', 'url',
            'publish_period', 'track', 'currency', 'apc', 'rating_avg',
            'contact', 'email', 'country', 'language', 'col_style',
            'desc', 'last_update'
        ]