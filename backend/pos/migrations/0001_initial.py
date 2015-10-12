# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
import common.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('active', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False, help_text=b'Deletes should deactivate not do actual deletes')),
                ('created_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
                ('profile', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductTypes',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('active', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False, help_text=b'Deletes should deactivate not do actual deletes')),
                ('name', models.CharField(max_length=255)),
                ('created_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(to='pos.Organization')),
                ('updated_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('active', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False, help_text=b'Deletes should deactivate not do actual deletes')),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
                ('customer_email', models.EmailField(max_length=254, null=True, blank=True)),
                ('customer_id_number', models.CharField(max_length=128)),
                ('customer_phone', models.CharField(max_length=128)),
                ('customer_first_name', models.CharField(max_length=128)),
                ('customer_last_name', models.CharField(max_length=128)),
                ('customer_address', models.TextField(null=True, blank=True)),
                ('follow_up_date', models.DateTimeField()),
                ('created_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(to='pos.ProductTypes')),
                ('updated_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SalesAgent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('active', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False, help_text=b'Deletes should deactivate not do actual deletes')),
                ('created_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(to='pos.Organization')),
                ('profile', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, default=common.models.get_default_system_user_id, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='producttypes',
            unique_together=set([('name', 'organization')]),
        ),
    ]
