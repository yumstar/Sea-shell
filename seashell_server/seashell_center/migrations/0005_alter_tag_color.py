# Generated by Django 4.2 on 2023-09-03 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seashell_center', '0004_alter_dayexperience_options_alter_message_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=models.CharField(default='black', max_length=50),
        ),
    ]
