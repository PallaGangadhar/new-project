# Generated by Django 2.1.7 on 2019-03-06 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0012_project_inquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_inquiry',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.project'),
        ),
    ]
