# Generated by Django 2.1.5 on 2019-02-05 02:02

from django.db import migrations, models
import learning.models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='color_coded_image',
            field=models.ImageField(default='default.jpg', upload_to=learning.models.PathAndRename('color_coded_characters/C')),
        ),
        migrations.AlterField(
            model_name='character',
            name='pinyin_audio',
            field=models.FileField(default='error.mp3', help_text='it is ok for now to leave blank', upload_to=learning.models.PathAndRename('pinyin_audio/C')),
        ),
        migrations.AlterField(
            model_name='character',
            name='stroke_order_image',
            field=models.ImageField(default='default.jpg', upload_to=learning.models.PathAndRename('animated_stroke_order/C')),
        ),
        migrations.AlterField(
            model_name='radical',
            name='mnemonic_image',
            field=models.ImageField(default='default.jpg', upload_to=learning.models.PathAndRename('radical_mnemonic/R')),
        ),
    ]