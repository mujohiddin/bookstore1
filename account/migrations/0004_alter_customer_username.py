# Generated by Django 4.0.1 on 2022-02-02 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_customer_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='username',
            field=models.CharField(max_length=150, null=True, unique=True),
        ),
    ]
