# Generated by Django 3.1.1 on 2020-12-21 03:07

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(help_text='This is for internal use only, feel free to use it for note taking', max_length=500)),
                ('chinese', models.CharField(max_length=1)),
                ('identifier', models.CharField(blank=True, max_length=10)),
                ('pinyin', models.CharField(max_length=6)),
                ('definitions', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=3)),
                ('character_type', models.CharField(max_length=30)),
                ('memory_aid', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='CharacterInWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(help_text='This determines the order of the character in the word.')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.character')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Radical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(help_text='This is for internal use only, feel free to use it for note taking', max_length=500)),
                ('chinese', models.CharField(max_length=1)),
                ('definition', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(help_text='This is for internal use only, feel free to use it for note taking', max_length=500)),
                ('chinese', models.CharField(max_length=5)),
                ('identifier', models.CharField(blank=True, max_length=10)),
                ('pinyin', models.CharField(max_length=36)),
                ('memory_aid', models.TextField(blank=True, max_length=300)),
                ('characters', models.ManyToManyField(related_name='characters', related_query_name='character', through='content.CharacterInWord', to='content.Character')),
            ],
            options={
                'unique_together': {('chinese', 'identifier')},
            },
        ),
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pinyin', models.CharField(max_length=200)),
                ('chinese', models.CharField(max_length=40)),
                ('translation', models.CharField(max_length=200)),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sentences', related_query_name='sentence', to='content.word')),
            ],
        ),
        migrations.CreateModel(
            name='RadicalInCharacter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(help_text='This determines the order of the radical in the character.')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.character')),
                ('radical', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.radical')),
            ],
            options={
                'ordering': ['order'],
                'unique_together': {('character', 'radical', 'order')},
            },
        ),
        migrations.CreateModel(
            name='DefinitionInWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_of_speech', models.CharField(max_length=7)),
                ('definition', models.CharField(max_length=70)),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='definitions', related_query_name='definition', to='content.word')),
            ],
        ),
        migrations.AddField(
            model_name='characterinword',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.word'),
        ),
        migrations.AddField(
            model_name='character',
            name='radicals',
            field=models.ManyToManyField(related_name='radicals', related_query_name='radical', through='content.RadicalInCharacter', to='content.Radical'),
        ),
        migrations.AlterUniqueTogether(
            name='characterinword',
            unique_together={('character', 'word', 'order')},
        ),
        migrations.AlterUniqueTogether(
            name='character',
            unique_together={('chinese', 'identifier')},
        ),
    ]
