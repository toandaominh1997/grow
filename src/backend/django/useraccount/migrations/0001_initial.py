# Generated by Django 4.0.6 on 2022-07-22 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_name', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=256, null=True)),
                ('address', models.CharField(max_length=256, null=True)),
            ],
        ),
    ]
