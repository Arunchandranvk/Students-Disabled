# Generated by Django 4.2.5 on 2023-09-21 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_remove_studentanswer_answer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentanswer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='studentanswer',
            name='student',
        ),
        migrations.RemoveField(
            model_name='testresultmodel',
            name='Std_id',
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
        migrations.DeleteModel(
            name='StudentAnswer',
        ),
        migrations.DeleteModel(
            name='TestResultModel',
        ),
    ]
