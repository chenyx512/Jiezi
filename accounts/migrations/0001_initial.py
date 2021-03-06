# Generated by Django 2.1.7 on 2019-06-17 02:12

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(max_length=255)),
                ('cn_level', models.CharField(default='Beginner', max_length=15)),
                ('last_study_date', models.DateField(null=True)),
                ('study_streak', models.IntegerField(default=0)),
                ('last_study_duration', models.DurationField(default=datetime.timedelta(0))),
                ('last_study_vocab_count', models.IntegerField(default=0, null=True)),
                ('total_study_duration', models.DurationField(default=datetime.timedelta(0))),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserCharacter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_added', models.DateField(auto_now_add=True)),
                ('time_last_learned', models.DateTimeField(null=True)),
                ('times_learned', models.IntegerField(default=0)),
                ('EF', models.FloatField(default=2.5)),
                ('interval', models.DecimalField(decimal_places=2, default=1, max_digits=7)),
            ],
            options={
                'ordering': ['interval', 'time_added', 'character__pk'],
            },
        ),
        migrations.CreateModel(
            name='UserCharacterTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_character_tags', related_query_name='user_character_tag', to=settings.AUTH_USER_MODEL)),
                ('user_characters', models.ManyToManyField(related_name='tags', related_query_name='tag', to='accounts.UserCharacter')),
            ],
        ),
    ]
