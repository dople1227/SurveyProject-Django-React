# Generated by Django 4.2 on 2023-05-02 22:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("survey", "0008_remove_answer_ischeck_response_ischeck"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="type",
            field=models.CharField(
                choices=[("checkbox", "Checkbox"), ("radio", "Radio")], max_length=10
            ),
        ),
    ]