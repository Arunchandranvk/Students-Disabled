# Generated by Django 4.2.5 on 2023-09-20 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_testscore_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testscore',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='testscore',
            name='question',
        ),
        migrations.RemoveField(
            model_name='testscore',
            name='student',
        ),
        migrations.RemoveField(
            model_name='testscore',
            name='subject',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='TestScore',
        ),
    ]
