# Generated by Django 4.2.4 on 2023-09-06 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dissectix', '0006_alter_challenge_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
