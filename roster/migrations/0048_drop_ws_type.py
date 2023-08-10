# Generated by Django 3.0.7 on 2021-01-11 21:17

from django.db import migrations


def remove_winter(apps, scheme_editor):
    Student = apps.get_model("roster", "Student")
    Student.objects.filter(track="CW").update(track="C")
    Student.objects.filter(track="BW").update(track="B")


class Migration(migrations.Migration):
    dependencies = [
        ("roster", "0047_auto_20201114_1551"),
    ]

    operations = [
        migrations.RunPython(remove_winter, migrations.RunPython.noop, elidable=True)
    ]
