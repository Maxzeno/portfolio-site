# Generated by Django 4.1.3 on 2022-12-11 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_languagetoolsmodel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmodel',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
