# Generated by Django 2.1.5 on 2019-02-26 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20190226_0536'),
    ]

    operations = [
        migrations.CreateModel(
            name='project_assingment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.department')),
            ],
        ),
        migrations.AlterModelOptions(
            name='time_sheet',
            options={'verbose_name_plural': 'Time Sheet'},
        ),
        migrations.RemoveField(
            model_name='project',
            name='dept',
        ),
        migrations.RemoveField(
            model_name='project',
            name='staff',
        ),
        migrations.AddField(
            model_name='project_assingment',
            name='pip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.project'),
        ),
        migrations.AddField(
            model_name='project_assingment',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.staff'),
        ),
    ]
