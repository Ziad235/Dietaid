# Generated by Django 4.2 on 2023-04-16 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_diagnosis"),
    ]

    operations = [
        migrations.RenameField(
            model_name="diagnosis",
            old_name="patient_id",
            new_name="patients_id",
        ),
    ]
