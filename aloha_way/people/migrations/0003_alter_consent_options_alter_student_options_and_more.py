# Generated by Django 4.0.3 on 2022-04-10 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_consent_trainertimetable_studentconsent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consent',
            options={'ordering': ['name'], 'verbose_name_plural': 'Wykaz zgód'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['last_name', 'first_name'], 'verbose_name_plural': 'Kursanci'},
        ),
        migrations.AlterModelOptions(
            name='studentconsent',
            options={'ordering': ['student__last_name', 'student__first_name'], 'verbose_name_plural': 'Zgody kursantów'},
        ),
        migrations.AlterModelOptions(
            name='trainer',
            options={'ordering': ['user__last_name', 'user__first_name'], 'verbose_name_plural': 'Instruktorzy'},
        ),
        migrations.AlterModelOptions(
            name='trainertimetable',
            options={'ordering': ['day', 'start_time'], 'verbose_name_plural': 'Terminy instruktora'},
        ),
        migrations.AlterField(
            model_name='trainertimetable',
            name='season',
            field=models.SmallIntegerField(choices=[(0, 2022), (1, 2024), (1, 2025), (1, 2026)], default=0, verbose_name='Sezon'),
        ),
    ]
