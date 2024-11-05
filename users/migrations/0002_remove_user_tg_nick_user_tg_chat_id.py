# Generated by Django 5.1.1 on 2024-11-05 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="tg_nick",
        ),
        migrations.AddField(
            model_name="user",
            name="tg_chat_id",
            field=models.CharField(
                blank=True,
                help_text="Укажите Telegram chat ID",
                max_length=50,
                null=True,
                verbose_name="Телеграм ID",
            ),
        ),
    ]