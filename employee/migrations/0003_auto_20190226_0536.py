# Generated by Django 2.1.5 on 2019-02-26 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20190223_0446'),
    ]

    operations = [
        migrations.CreateModel(
            name='time_sheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.IntegerField()),
                ('description', models.CharField(max_length=128)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='project_status',
            field=models.CharField(choices=[('complete', 'Complete'), ('incomplete', 'Incomplete')], default='incomplete', max_length=128),
        ),
        migrations.AddField(
            model_name='time_sheet',
            name='pid',
            field=models.ForeignKey(on_delete=models.Model, to='employee.project'),
        ),
        migrations.AddField(
            model_name='time_sheet',
            name='staff',
            field=models.ForeignKey(on_delete=models.Model, to='employee.staff'),
        ),
    ]