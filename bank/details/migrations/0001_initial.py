# Generated by Django 2.2.4 on 2019-08-30 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BANKS',
            fields=[
                ('name', models.CharField(max_length=49)),
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]