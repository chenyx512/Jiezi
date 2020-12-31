# Generated by Django 3.1.1 on 2020-12-27 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0019_auto_20201226_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='character_type',
            field=models.CharField(blank=True, choices=[(None, 'TODO'), ('pictographic', 'pictographic'), ('Ideographic', 'Ideographic'), ('Compound Ideographic', 'Compound Ideographic'), ('Picto-phonetic', 'Picto-phonetic'), ('Loan', 'Loan')], max_length=30),
        ),
        migrations.AlterField(
            model_name='radicalincharacter',
            name='radical_type',
            field=models.CharField(blank=True, choices=[(None, 'TODO'), ('semantic', 'semantic'), ('phonetic', 'phonetic'), ('both', 'both'), ('neither', 'neither')], max_length=12),
        ),
    ]