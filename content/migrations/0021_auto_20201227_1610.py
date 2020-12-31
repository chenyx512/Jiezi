# Generated by Django 3.1.1 on 2020-12-27 16:10

import content.models.general_content_model
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0020_auto_20201227_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='chinese',
            field=models.CharField(max_length=1, validators=[content.models.general_content_model.validate_chinese_character_or_x]),
        ),
        migrations.AlterField(
            model_name='radical',
            name='chinese',
            field=models.CharField(max_length=1, validators=[content.models.general_content_model.validate_chinese_character_or_x]),
        ),
        migrations.AlterField(
            model_name='word',
            name='chinese',
            field=models.CharField(max_length=5, validators=[content.models.general_content_model.validate_chinese_character_or_x]),
        ),
    ]