# Generated by Django 4.2.5 on 2023-09-20 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_student_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='accesstechnology',
            field=models.CharField(choices=[('Screen Reader', 'Screen Reader'), ('Braille Display', 'Braille Display'), ('Hearing Aids', 'Hearing Aids'), ('Voice Recognition', 'Voice Recognition')], default='Screen Reader', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='disability',
            field=models.CharField(choices=[('Physical', 'Physical'), ('Visual', 'Visual'), ('Hearing', 'Hearing'), ('Cognitive', 'Cognitive')], default='Physical', max_length=100),
        ),
    ]
