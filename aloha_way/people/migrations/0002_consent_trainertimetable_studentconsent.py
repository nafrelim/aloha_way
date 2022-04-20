# Generated by Django 4.0.3 on 2022-04-10 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TrainerTimetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.SmallIntegerField(choices=[(0, 2022), (1, 2023)], default=0, verbose_name='Sezon')),
                ('day', models.DateField(verbose_name='Dzień')),
                ('start_time', models.TimeField(verbose_name='Początek')),
                ('end_time', models.TimeField(verbose_name='Koniec')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.trainer')),
            ],
            options={
                'ordering': ['day', 'start_time'],
            },
        ),
        migrations.CreateModel(
            name='StudentConsent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decision', models.BooleanField(blank=True, default=False, verbose_name='Decyzja o zgodzie')),
                ('consent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.consent', verbose_name='Zgoda')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.student', verbose_name='Student')),
            ],
        ),
    ]