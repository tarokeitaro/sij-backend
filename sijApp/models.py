import uuid
import os
from decimal import Decimal
from io import BytesIO
from django.db import models
from django.core.files.base import ContentFile
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image

def get_random_filename():
    return uuid.uuid4().hex

class Country(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Language(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Currency(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=50)
    alpha_code = models.CharField(
        "ISO 4217 alpha code",
        max_length=4,
        unique=True
    )
    symbol = models.CharField(
        max_length=5,
        blank=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        sym = f" {self.symbol}" if self.symbol else ""
        return f"{self.name}{sym} ({self.alpha_code})"


class Institution(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=255)
    desc = models.TextField(blank=True)
    slug = models.SlugField(
        unique=True,
        max_length=255
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Track(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=30)
    desc = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "tracks"
        ordering = ["name"]

    def __str__(self):
        return self.name


class PublishPeriod(models.Model):
    month = models.CharField(
        max_length=10,
        unique=True
    )

    class Meta:
        verbose_name = "publish period"
        verbose_name_plural = "publish periods"
        ordering = ["month"]

    def __str__(self):
        return self.month


class ColStyle(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=50)
    desc = models.TextField(blank=True)
    slug = models.SlugField(
        unique=True,
        max_length=255
    )

    class Meta:
        verbose_name = "column/style"
        verbose_name_plural = "columns/styles"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Rank(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=30)
    desc = models.TextField(blank=True)
    slug = models.SlugField(
        unique=True,
        max_length=255
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Journal(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    institution = models.ForeignKey(
        Institution,
        on_delete=models.CASCADE,
        related_name="journals"
    )
    rank = models.ForeignKey(
        Rank,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="journals"
    )
    cover = models.ImageField(
        upload_to="journal_covers/",
        blank=True,
        null=True
    )
    def save(self, *args, **kwargs):
        if self.cover and not self.cover.name.endswith(".webp"):
            img = Image.open(self.cover)

            # Konversi ke RGB kalau mode bukan RGB/RGBA (WebP tidak dukung CMYK dll)
            if img.mode not in ("RGB", "RGBA"):
                img = img.convert("RGB")

            img_io = BytesIO()
            img.save(img_io, format='WEBP', quality=85)

            # Buat nama file random
            random_name = get_random_filename() + ".webp"
            full_path = os.path.join("journal_covers", random_name)

            # Simpan file webp ke ImageField
            self.cover.save(full_path, ContentFile(img_io.getvalue()), save=False)

        super().save(*args, **kwargs)

    name = models.CharField(max_length=255)
    url = models.URLField()
    publish_period = models.ManyToManyField(
        PublishPeriod,
        related_name="journals",
        blank=True
    )
    track = models.ManyToManyField(
        Track,
        related_name="journals",
        blank=True
    )
    currency = models.ForeignKey(
        Currency,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    apc = models.DecimalField(
        "article-processing charge",
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    rating_avg = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=Decimal("0.00"),
        validators=[
            MinValueValidator(Decimal("0.00")),
            MaxValueValidator(Decimal("5.00")),
        ],
        help_text="Average rating (0.00 – 5.00)",
    )
    contact = models.CharField(
        max_length=12,
        blank=True
    )
    email = models.EmailField(blank=True)
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="journals"
    )
    language = models.ForeignKey(
        Language,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="journals",
    )
    col_style = models.ForeignKey(
        ColStyle,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="journals",
    )
    desc = models.TextField(blank=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["rating_avg"]),
        ]

    def __str__(self):
        return self.name