# Generated by Django 5.1 on 2024-09-01 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0002_remove_price_coin_price_currency_alter_price_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='pi_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('value', models.IntegerField()),
                ('currency', models.TextField(max_length=3)),
            ],
        ),
        migrations.DeleteModel(
            name='price',
        ),
    ]
