# Generated by Django 4.2.7 on 2023-11-20 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_botuser_phone_number_alter_botuser_full_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botuser',
            name='username',
            field=models.CharField(blank=True, db_index=True, error_messages={'unique': 'A user with that username already exists.'}, max_length=50, null=True, verbose_name='Telegram username'),
        ),
    ]
