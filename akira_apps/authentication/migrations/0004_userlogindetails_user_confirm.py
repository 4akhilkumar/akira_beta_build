# Generated by Django 3.2.5 on 2021-11-15 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20211112_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlogindetails',
            name='user_confirm',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
