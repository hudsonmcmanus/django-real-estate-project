# Generated by Django 3.0.7 on 2020-06-16 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='realtor_email',
            field=models.CharField(default='null', max_length=60),
            preserve_default=False,
        ),
    ]
