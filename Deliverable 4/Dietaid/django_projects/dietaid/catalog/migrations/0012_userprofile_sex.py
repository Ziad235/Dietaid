# Generated by Django 4.2 on 2023-05-04 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0011_userprofile"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="sex",
            field=models.CharField(default="Male", max_length=10),
            preserve_default=False,
        ),
    ]
