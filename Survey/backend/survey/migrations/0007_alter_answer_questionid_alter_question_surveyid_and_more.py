# Generated by Django 4.2 on 2023-04-25 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("survey", "0006_remove_response_ischeck_answer_ischeck"),
    ]

    operations = [
        migrations.AlterField(
            model_name="answer",
            name="questionId",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="answer",
                to="survey.question",
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="surveyId",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="question",
                to="survey.survey",
            ),
        ),
        migrations.AlterField(
            model_name="respondent",
            name="surveyId",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="respondent",
                to="survey.survey",
            ),
        ),
        migrations.AlterField(
            model_name="response",
            name="answerId",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="response",
                to="survey.answer",
            ),
        ),
        migrations.AlterField(
            model_name="response",
            name="questionId",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="response",
                to="survey.question",
            ),
        ),
        migrations.AlterField(
            model_name="response",
            name="respondentId",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="response",
                to="survey.respondent",
            ),
        ),
        migrations.AlterField(
            model_name="response",
            name="surveyId",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="response",
                to="survey.survey",
            ),
        ),
    ]
