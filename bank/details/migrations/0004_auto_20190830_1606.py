# Generated by Django 2.2.4 on 2019-08-30 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0003_auto_20190830_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branches',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='details.Banks'),
        ),
    ]
