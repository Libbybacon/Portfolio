# Generated by Django 3.1.6 on 2021-02-18 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Checkbook', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='Account',
            new_name='account',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='Amount',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='Type',
            new_name='type',
        ),
    ]
