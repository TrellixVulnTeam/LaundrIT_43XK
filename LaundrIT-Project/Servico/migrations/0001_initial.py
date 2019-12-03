# Generated by Django 2.2.7 on 2019-11-09 01:20

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Preço')),
            ],
            options={
                'verbose_name': 'serviço',
                'verbose_name_plural': 'serviços',
                'ordering': ('-descricao',),
            },
        ),
    ]