# Generated by Django 4.2.5 on 2023-10-16 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0045_alter_custuser_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default='question', on_delete=django.db.models.deletion.CASCADE, to='accounts.question'),
        ),
    ]
