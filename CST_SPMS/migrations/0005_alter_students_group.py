# Generated by Django 3.2.9 on 2022-01-07 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CST_SPMS', '0004_rename_student_group_students_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CST_SPMS.studentgroups'),
        ),
    ]