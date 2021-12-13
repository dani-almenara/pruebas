from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from datetime import datetime


class CountryCodes(models.Model):
    code = models.CharField(_('Código de país'), max_length=2)
    country_name = models.CharField(_('Pais'), max_length=100)

    def __str__(self):
        return self.code + " " + self.country_name

class TypeEvent(models.Model):
    event_type = models.CharField(_('Nombre de Evento'), max_length=30)

    def __str__(self):
        return self.event_type

class Event(models.Model):
    STATUS_CHOICES = (
        ('draft', _('Borrador')),
        ('published', _('Publicado')),
    )
    AGES = (
        ('ALL', 'All ages allowed'),
        ('03', '+3 years old'),
        ('10', '+10 years old'),
        ('16', '+16 years old'),
        ('18', '+18 years old'),
        ('21', '+21 years old'),
    )
    title = models.CharField(_('Título del evento'), max_length=200)
    description = models.TextField(_('Descripción'), blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='events')
    type_event = models.ForeignKey(
        TypeEvent, on_delete=models.CASCADE, related_name='type_event')
    place_id = models.CharField(max_length=100)
    country_code = models.ForeignKey(
        CountryCodes, on_delete=models.CASCADE, related_name='country_code')
    admin_area_level_1 = models.CharField(
        _('Comunidad Autónoma'), blank=True, max_length=100)
    admin_area_level_2 = models.CharField(
        _('Provincia'), blank=True, max_length=100)
    locality = models.CharField(_('Localidad'), max_length=50)
    address = models.CharField(_('Dirección'), max_length=100)
    zip_code = models.CharField(_('Código postal'), max_length=10)
    init_date = models.DateTimeField(
        _('Fecha de incio'), null=False, blank=False)
    finish_date = models.DateTimeField(
        _('Fecha de fin'), null=False, blank=False)
    age = models.CharField(
        _('Calificación edad'), null=False, choices=AGES, max_length=3, default='ALL')
    status = models.CharField(
        _('Estado'), max_length=10, choices=STATUS_CHOICES, default='published')
    publish = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=250, unique=True, default='slug')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-init_date',)

    def __str__(self):
        return _('Evento {} en {} el {}').format(
            self.title, self.country_code, self.init_date)

    def get_absolute_url(self):
        return reverse("events:post_detail", args=[self.slug, ])

    # Modifico el slug para apadirle el timestamp dela fecha de creación delante de el slug con el título
    def save(self, *args, **kwargs):
        self.slug = "{created}-{slug}".format(created=str(int(datetime.now().timestamp())), slug=slugify(self.title))
        super(Event, self).save(*args, **kwargs)






