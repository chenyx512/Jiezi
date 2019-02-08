# Generated by Django 2.1.5 on 2019-02-05 01:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('learning', '0001_initial'),
        ('auth', '0009_alter_user_last_name_max_length'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercharacter',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning.Character'),
        ),
        migrations.AddField(
            model_name='usercharacter',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_characters', related_query_name='user_character', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterUniqueTogether(
            name='usercharactertag',
            unique_together={('user', 'name')},
        ),
        migrations.AlterUniqueTogether(
            name='usercharacter',
            unique_together={('user', 'character')},
        ),
    ]
