# Generated by Django 2.1 on 2020-09-10 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200909_1144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date',
            new_name='updated_at',
        ),
    ]
