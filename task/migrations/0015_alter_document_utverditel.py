# Generated by Django 5.0.2 on 2024-03-03 13:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0014_alter_document_bin_alter_document_coment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='utverditel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='approvals', to='task.responsible'),
        ),
    ]
