# Generated by Django 2.2.3 on 2019-07-21 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('write', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectmind',
            name='end',
            field=models.BooleanField(default=False),
        ),
    ]
