# Generated by Django 4.2 on 2023-04-17 10:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0007_mealplan"),
    ]

    operations = [
        migrations.AddField(
            model_name="mealplan",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="mealplan",
            name="diagnosis_id",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="mealplan",
            name="notes_from_doctor",
            field=models.CharField(default="some notes from doctor", max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="mealplan",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
