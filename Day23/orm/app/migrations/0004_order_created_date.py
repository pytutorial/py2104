# Generated by Django 3.2 on 2021-08-11 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
