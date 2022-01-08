# Generated by Django 4.0.1 on 2022-01-05 00:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(verbose_name='Dzień szkolenia')),
                ('start_time', models.TimeField(verbose_name='Godzina rozpoczęcia')),
                ('duration', models.PositiveSmallIntegerField(default=1, verbose_name='Czas trwania(godz)')),
                ('cancellation', models.BooleanField(blank=True, default=False, verbose_name='Anulowanie?')),
                ('was_training', models.BooleanField(blank=True, default=False, null=True, verbose_name='Szkolenie odbyte?')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Dodatkowe informacje')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['day', 'start_time'],
            },
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
        migrations.CreateModel(
            name='StudentTraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.PositiveSmallIntegerField(default=0, verbose_name='Czas trwania')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Dodatkowe informacje')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainings.student', verbose_name='Instruktor')),
            ],
        ),
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
            name='TrainingPacket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nazwa')),
                ('number_of_hours', models.PositiveSmallIntegerField(verbose_name='Liczba godzin')),
                ('price', models.PositiveSmallIntegerField(verbose_name='Cena')),
                ('active', models.BooleanField(default=False, verbose_name='Aktywny')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Dodatkowe informacje')),
            ],
            options={
                'ordering': ['number_of_hours'],
            },
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(auto_now_add=True, verbose_name='Dzień szkolenia')),
                ('start_time', models.TimeField(verbose_name='Godzina rozpoczęcia')),
                ('duration', models.PositiveSmallIntegerField(default=0, verbose_name='Czas trwania(godz)')),
                ('acceptance', models.BooleanField(default=False, verbose_name='Akceptacja')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Dodatkowe informacje')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('booking', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='trainings.booking', verbose_name='Rezerwacja')),
                ('students', models.ManyToManyField(through='trainings.StudentTraining', to='trainings.Student', verbose_name='Kursanci')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainings.trainer', verbose_name='Instruktor')),
            ],
            options={
                'ordering': ['day', 'start_time'],
            },
        ),
        migrations.AddField(
            model_name='studenttraining',
            name='training',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainings.training', verbose_name='Trening'),
        ),
        migrations.AddField(
            model_name='booking',
            name='students',
            field=models.ManyToManyField(to='trainings.Student', verbose_name='Kursanci'),
        ),
        migrations.AddField(
            model_name='booking',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainings.trainer', verbose_name='Instruktor'),
        ),
    ]
