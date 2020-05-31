# Generated by Django 3.0.6 on 2020-05-31 00:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nit', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=120, unique=True)),
                ('email', models.EmailField(max_length=100)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Commerce',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=30, null=True)),
                ('address', models.CharField(max_length=120)),
                ('neighborhood', models.CharField(blank=True, max_length=120, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.Organization')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
