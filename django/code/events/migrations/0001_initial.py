# Generated by Django 3.2 on 2021-08-26 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryCodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2, verbose_name='Código de país')),
                ('country_name', models.CharField(max_length=100, verbose_name='Pais')),
            ],
        ),
        migrations.CreateModel(
            name='TypeEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(max_length=30, verbose_name='Nombre de Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título del evento')),
                ('description', models.TextField(blank=True, verbose_name='Descripción')),
                ('place_id', models.CharField(max_length=100)),
                ('admin_area_level_1', models.CharField(blank=True, max_length=100, verbose_name='Comunidad Autónoma')),
                ('admin_area_level_2', models.CharField(blank=True, max_length=100, verbose_name='Provincia')),
                ('locality', models.CharField(max_length=50, verbose_name='Localidad')),
                ('address', models.CharField(max_length=100, verbose_name='Dirección')),
                ('zip_code', models.CharField(max_length=10, verbose_name='Código postal')),
                ('init_date', models.DateTimeField(verbose_name='Fecha de incio')),
                ('finish_date', models.DateTimeField(verbose_name='Fecha de fin')),
                ('age', models.CharField(choices=[('ALL', 'All ages allowed'), ('03', '+3 years old'), ('10', '+10 years old'), ('16', '+16 years old'), ('18', '+18 years old'), ('21', '+21 years old')], default='ALL', max_length=3, verbose_name='Calificación edad')),
                ('status', models.CharField(choices=[('draft', 'Borrador'), ('published', 'Publicado')], default='published', max_length=10, verbose_name='Estado')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(default='slug', max_length=250, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL)),
                ('country_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_code', to='events.countrycodes')),
                ('type_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type_event', to='events.typeevent')),
            ],
            options={
                'ordering': ('-init_date',),
            },
        ),
    ]
