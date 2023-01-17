# Generated by Django 4.1.4 on 2023-01-17 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("roster", "0097_remove_registrationcontainer_num_preps"),
    ]

    operations = [
        migrations.AlterField(
            model_name="unitinquiry",
            name="action_type",
            field=models.CharField(
                choices=[
                    ("INQ_ACT_UNLOCK", "Unlock now"),
                    ("INQ_ACT_APPEND", "Add for later"),
                    ("INQ_ACT_DROP", "Drop"),
                    ("INQ_ACT_LOCK", "Lock (Drop + Add for later)"),
                ],
                help_text="Describe the action you want to make.",
                max_length=15,
            ),
        ),
    ]
