# Generated by Django 4.2.4 on 2023-09-08 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authserver', '0008_dissectixuser_solved_challenges'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dissectixuser',
            name='solved_challenges',
            field=models.JSONField(default=dict),
        ),
    ]