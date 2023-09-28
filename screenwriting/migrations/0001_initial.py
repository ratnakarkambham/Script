# Generated by Django 4.2.5 on 2023-09-27 03:55

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Screenplay",
            fields=[
                (
                    "screenplay_uid",
                    models.BigAutoField(primary_key=True, serialize=False),
                ),
                ("title", models.TextField()),
                ("success_percentage", models.FloatField()),
                ("ip_address", models.TextField()),
                ("geo_location", models.TextField()),
                ("status", models.TextField()),
                ("file_path", models.TextField()),
                ("file_size", models.IntegerField()),
                ("user_uid", models.BigIntegerField()),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("modified_on", models.DateTimeField(auto_now_add=True)),
                ("created_by", models.BigIntegerField()),
                ("modified_by", models.BigIntegerField()),
                ("language_uid", models.SmallIntegerField()),
                ("process_time", models.BigIntegerField()),
                ("failure_reason", models.TextField()),
            ],
            options={
                "db_table": "screenplay",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Test",
            fields=[
                ("test_uid", models.AutoField(primary_key=True, serialize=False)),
                ("data", models.TextField()),
            ],
            options={
                "db_table": "test",
                "managed": True,
            },
        ),
    ]
