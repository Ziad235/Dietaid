# Generated by Django 4.2 on 2023-05-04 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0012_userprofile_sex"),
    ]

    operations = [
        migrations.AddField(
            model_name="mealplan",
            name="allergy",
            field=models.CharField(default="None", max_length=50),
            preserve_default=False,
        ),
    ]