# Generated by Django 4.1.2 on 2022-11-20 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resumes', '0015_chat'),
        ('vacancies', '0003_auto_20221115_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='VacancyResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hello_message', models.TextField(blank=True, default='Здравствуйте. Меня заинтересовала ваша вакансия!', max_length=3000, verbose_name='Приветственное сообщение')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('changed_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancy_responses', to=settings.AUTH_USER_MODEL, verbose_name='Автор отклика')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancy_responses', to='resumes.resume', verbose_name='Резюме')),
                ('vacancy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vacancy_responses', to='vacancies.vacancy', verbose_name='Вакансия')),
            ],
        ),
    ]
