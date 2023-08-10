# Generated by Django 4.1.5 on 2023-01-24 21:08

import datetime
from typing import Any

from django.db import migrations, models
from django.utils.timezone import utc


def set_invoice_created_at_by_student_reg(apps: Any, scheme_editor: Any):
    Invoice = apps.get_model("roster", "Invoice")
    invoices = []
    for invoice in Invoice.objects.filter(student__reg__isnull=False):
        invoice.created_at = invoice.student.reg.created_at
        invoices.append(invoice)
    Invoice.objects.bulk_update(invoices, fields=("created_at",), batch_size=50)


class Migration(migrations.Migration):
    dependencies = [
        ("roster", "0098_alter_unitinquiry_action_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoice",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(1970, 1, 1, 0, 0, tzinfo=utc),
            ),
            preserve_default=False,
        ),
        migrations.RunPython(
            set_invoice_created_at_by_student_reg,
            migrations.RunPython.noop,
            elidable=True,
        ),
    ]
