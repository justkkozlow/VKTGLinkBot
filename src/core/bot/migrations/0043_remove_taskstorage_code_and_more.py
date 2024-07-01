# Generated by Django 4.2.2 on 2024-06-18 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0042_alter_botsettings_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskstorage',
            name='code',
        ),
        migrations.RemoveField(
            model_name='taskstorage',
            name='message_text',
        ),
        migrations.AddField(
            model_name='taskstorage',
            name='link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='link', to='bot.linksqueue', verbose_name='Ссылка'),
        ),
    ]
