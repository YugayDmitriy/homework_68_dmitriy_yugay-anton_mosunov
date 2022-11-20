# Generated by Django 4.1.2 on 2022-11-19 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0003_auto_20221115_1907'),
        ('resumes', '0012_remove_response_vacancy'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='vacancy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='response', to='vacancies.vacancy', verbose_name='Вакансия'),
        ),
    ]