# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-29 17:55
from __future__ import unicode_literals

from django.db import migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sobre', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sobrenos',
            options={'verbose_name': 'Sobre nós', 'verbose_name_plural': 'Sobre nós'},
        ),
        migrations.AlterField(
            model_name='sobrenos',
            name='descricao',
            field=redactor.fields.RedactorField(verbose_name='Descriçao'),
        ),
    ]
