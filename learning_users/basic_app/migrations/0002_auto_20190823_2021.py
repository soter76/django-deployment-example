# Generated by Django 2.2.4 on 2019-08-23 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='portfolio_side',
            new_name='portfolio_site',
        ),
    ]
