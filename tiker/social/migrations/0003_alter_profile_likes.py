# Generated by Django 4.1.4 on 2022-12-21 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("social", "0002_alter_profile_postdate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile", name="likes", field=models.IntegerField(null=True),
        ),
    ]
