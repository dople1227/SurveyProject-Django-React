# Generated by Django 4.2 on 2023-05-02 15:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("survey", "0007_alter_answer_questionid_alter_question_surveyid_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="answer",
            name="isCheck",
        ),
        migrations.AddField(
            model_name="response",
            name="isCheck",
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
