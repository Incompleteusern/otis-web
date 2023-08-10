# Generated by Django 4.1.10 on 2023-08-10 20:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("arch", "0001_squashed_0032_alter_problem_puid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hint",
            name="problem",
            field=models.ForeignKey(
                help_text="The container of the current hint.",
                on_delete=django.db.models.deletion.CASCADE,
                to="arch.problem",
            ),
        ),
        migrations.AlterField(
            model_name="vote",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
