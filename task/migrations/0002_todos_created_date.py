# Generated by Django 3.2.20 on 2023-09-15 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todos',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
