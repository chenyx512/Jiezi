# Generated by Django 3.1.1 on 2020-12-21 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20201221_0427'),
    ]

    operations = [
        migrations.AddField(
            model_name='radical',
            name='identifier',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterUniqueTogether(
            name='radical',
            unique_together={('chinese', 'identifier')},
        ),
    ]
