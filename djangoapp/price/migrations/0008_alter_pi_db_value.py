# Generated by Django 5.1 on 2024-09-01 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0007_alter_pi_db_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pi_db',
            name='value',
            field=models.FloatField(),
        ),
    ]