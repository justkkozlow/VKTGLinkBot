# Generated by Django 4.2.2 on 2024-02-07 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0007_alter_botuser_state_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskstorage',
            name='task_completed',
            field=models.BooleanField(default=False, verbose_name='Задание выполнено'),
        ),
    ]
