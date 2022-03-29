# Generated by Django 4.0.1 on 2022-01-08 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', models.PositiveIntegerField(verbose_name='Numer telefonu')),
                ('level', models.SmallIntegerField(choices=[(0, 'nieokreślony'), (1, 'junior'), (2, 'mid'), (3, 'senior')], default=0, verbose_name='Poziom kompetencji')),
                ('hours_completed', models.PositiveSmallIntegerField(default=0, verbose_name='Zrealizowanych godzin')),
                ('active', models.BooleanField(default=True, verbose_name='Czy pracuje w tym sezonie?')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Dodatkowe informacje')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='Imię')),
                ('last_name', models.CharField(max_length=150, verbose_name='Nazwisko')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('phone', models.PositiveIntegerField(verbose_name='Numer telefonu')),
                ('weight', models.SmallIntegerField(blank=True, null=True, verbose_name='Waga')),
                ('height', models.SmallIntegerField(blank=True, null=True, verbose_name='Wzrost')),
                ('consents', models.BooleanField(default=False, verbose_name='Podpisanie zgód')),
                ('available_hours', models.SmallIntegerField(default=0, verbose_name='Dostępne godziny')),
                ('used_hours', models.PositiveSmallIntegerField(default=0, verbose_name='Godziny wykorzystane')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Dodatkowe informacje')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['last_name'],
            },
        ),
    ]