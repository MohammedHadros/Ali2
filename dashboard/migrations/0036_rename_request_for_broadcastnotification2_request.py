# Generated by Django 4.2.5 on 2023-09-12 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0035_broadcastnotification2"),
    ]

    operations = [
        migrations.RenameField(
            model_name="broadcastnotification2",
            old_name="request_for",
            new_name="request",
        ),
    ]
