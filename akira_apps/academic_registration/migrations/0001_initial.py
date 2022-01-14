# Generated by Django 3.2.5 on 2022-01-14 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('specialization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecEnrollStudent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('enrolledSpec', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='specialization.specializationsmc')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'enrolledSpec')},
            },
        ),
    ]
