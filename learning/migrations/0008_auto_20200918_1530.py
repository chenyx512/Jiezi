# Generated by Django 2.1.7 on 2020-09-18 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0007_remove_character_color_coded_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='example_1_character',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='character',
            name='example_1_meaning',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='character',
            name='example_1_word',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='character',
            name='example_2_character',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='example_2_meaning',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='example_2_word',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='mnemonic_explanation',
            field=models.CharField(max_length=800),
        ),
    ]
