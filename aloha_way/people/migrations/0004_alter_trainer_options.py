# Generated by Django 4.0.3 on 2022-04-10 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_alter_consent_options_alter_student_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trainer',
            options={'verbose_name_plural': 'Instruktorzy'},
        ),
    ]
