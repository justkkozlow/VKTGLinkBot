# Generated by Django 4.2.2 on 2024-03-05 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0018_remove_linkstorage_created_at_linkstorage_chat_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkstorage',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Comment'),
        ),
    ]
