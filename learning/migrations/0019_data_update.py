# Generated by Django 3.1.1 on 2020-10-29 17:04

from django.db import migrations


def update(apps, schema_editor):
    StudentCharacter = apps.get_model('learning', 'StudentCharacter')
    SCAbility = apps.get_model('learning', 'SCAbility')
    Ability = apps.get_model('learning', 'Ability')
    ReviewManager = apps.get_model('learning', 'ReviewManager')
    LearningProcess = apps.get_model('learning', 'LearningProcess')
    # reset Ability
    good_pks = []
    for ability in [0, 1, 2]:
        good_pks.append(Ability.objects.get_or_create(code=ability)[0].pk)
    Ability.objects.exclude(pk__in=good_pks).delete()
    for sc in StudentCharacter.objects.all():
        if sc.state == 20:
            sc.state = 10
            sc.save()
        for ability in Ability.objects.all():
            # signal not active during migration so have to manually set
            sca = SCAbility.objects.create(student_character=sc,
                ability=ability, student=sc.student, character=sc.character)
            if sc.state == 30: # MASTERED
                sca.state = 30 # MASTERED
                sca.save()
    LearningProcess.objects.all().delete()
    ReviewManager.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0018_auto_20201028_0837_squashed_0027_learningprocess_review_tested_abilities'),
    ]

    operations = [
        migrations.RunPython(update)
    ]
