# Generated by Django 4.0.2 on 2022-05-04 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uweflix', '0007_prices_transaction_request_to_cancel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='image',
            field=models.ImageField(default='placeholder.png', upload_to=''),
        ),
    ]
