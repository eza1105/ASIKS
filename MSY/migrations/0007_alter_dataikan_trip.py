# Generated by Django 4.1.2 on 2022-12-15 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MSY", "0006_alter_dataikan_ton_alter_dataikan_trip"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dataikan",
            name="trip",
            field=models.DecimalField(decimal_places=10, max_digits=10, null=True),
        ),
    ]
