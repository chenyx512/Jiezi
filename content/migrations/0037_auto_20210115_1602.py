# Generated by Django 3.1.1 on 2021-01-15 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0036_auto_20210115_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='definitioninword',
            name='part_of_speech',
            field=models.CharField(blank=True, choices=[(None, 'N/A'), (' ', 'TODO'), ('idiom', 'idiom'), ('adj', 'adjective'), ('adv', 'adverb'), ('conj', 'conjunction'), ('interj', 'interjection'), ('m', 'measure word'), ('mv', 'modal verb'), ('n', 'noun'), ('nu', 'numeral'), ('p', 'particle'), ('pn', 'proper noun'), ('pr', 'pronoun'), ('prefix', 'prefix'), ('prep', 'preposition'), ('qp', 'question particle'), ('qpr', 'question pronoun'), ('t', 'time word'), ('v', 'verb'), ('vc', 'verb plus complement'), ('vo', 'verb plus object')], default=' ', max_length=6),
        ),
    ]