# Generated by Django 4.1.2 on 2022-11-20 05:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resumes', '0014_remove_response_message_response_hello_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, max_length=3000, verbose_name='Сообщение')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('changed_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats', to=settings.AUTH_USER_MODEL, verbose_name='Автор сообщения')),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats', to='resumes.response', verbose_name='Отклик')),
            ],
        ),
    ]
