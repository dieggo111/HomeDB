# Generated by Django 3.0.3 on 2020-03-26 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_user_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user',
            new_name='name',
        ),
    ]