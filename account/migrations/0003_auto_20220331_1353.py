# Generated by Django 3.2.7 on 2022-03-31 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_extenduser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='extenduser',
            name='firstname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='extenduser',
            name='lastname',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
