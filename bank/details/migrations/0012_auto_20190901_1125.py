# Generated by Django 2.2.4 on 2019-09-01 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0011_auto_20190901_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branches',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='details.Banks'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
