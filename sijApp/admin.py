from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Country, Language, Currency, Institution, Track, PublishPeriod,
    ColStyle, Rank, Journal
)

# ---------- Mixin & util -------------------------------------------------
class NameSlugAdmin(admin.ModelAdmin):
    """Convenience base: search & pre-populate slug from name."""
    list_display  = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}  # only works if model has `slug`


# ---------- Simple lookup tables ----------------------------------------
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display  = ("name",)
    search_fields = ("name",)
    ordering      = ("name",)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display  = ("name",)
    search_fields = ("name",)
    ordering      = ("name",)


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display  = ("name", "alpha_code", "symbol")
    search_fields = ("name", "alpha_code", "symbol")
    ordering      = ("alpha_code",)


@admin.register(Institution)
class InstitutionAdmin(NameSlugAdmin):
    list_display = ("name", "desc_short")
    def desc_short(self, obj):
        return (obj.desc[:60] + "…") if obj.desc else "-"


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display  = ("name", "desc_short")
    search_fields = ("name",)
    ordering      = ("name",)

    def desc_short(self, obj):
        return (obj.desc[:60] + "…") if obj.desc else "-"


@admin.register(PublishPeriod)
class PublishPeriodAdmin(admin.ModelAdmin):
    list_display  = ("month",)
    search_fields = ("month",)
    ordering      = ("id",)


@admin.register(ColStyle)
class ColStyleAdmin(NameSlugAdmin):
    list_display = ("name", "desc_short")
    def desc_short(self, obj):
        return (obj.desc[:60] + "…") if obj.desc else "-"


@admin.register(Rank)
class RankAdmin(NameSlugAdmin):
    list_display = ("name", "desc_short")
    def desc_short(self, obj):
        return (obj.desc[:60] + "…") if obj.desc else "-"


# ---------- Journal ------------------------------------------------------
@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display   = (
        "name", "institution", "rank", "rating_avg",
        "country", "language", "apc_display", "last_update", "cover_thumb"
    )
    list_filter    = (
        "institution", "rank", "country", "language",
        "publish_period", "track",
    )
    search_fields  = ("name", "url", "institution__name")
    ordering       = ("name",)
    autocomplete_fields = (
        "institution", "rank", "country", "language", "currency", "col_style"
    )
    filter_horizontal = ("publish_period", "track")
    readonly_fields = ("cover_thumb", "last_update")

    fieldsets = (
        ("Identitas", {
            "fields": (
                ("name", "url"),
                ("institution", "rank"),
                ("country", "language"),
                ("publish_period", "track"),
                ("desc"),
            )
        }),
        ("Ekonomi", {
            "fields": (("currency", "apc"),)
        }),
        ("Tampilan", {
            "fields": ("cover", "cover_thumb", "col_style")
        }),
        ("Kontak", {
            "fields": (("contact", "email"),)
        }),
        ("Meta", {
            "fields": ("rating_avg", "last_update")
        }),
    )

    def apc_display(self, obj):
        if obj.apc and obj.currency:
            return f"{obj.currency.symbol}{obj.apc}"
        return "-"
    apc_display.short_description = "APC"

    def cover_thumb(self, obj):
        if obj.cover:
            return format_html(
                '<img src="{}" style="height:80px;width:auto;border-radius:3px;" />',
                obj.cover.url
            )
        return "—"
    cover_thumb.short_description = "Cover"

# ------------------------------------------------------------------------