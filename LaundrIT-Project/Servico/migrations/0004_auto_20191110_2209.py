# Generated by Django 2.2.7 on 2019-11-11 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servico', '0003_auto_20191110_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]