# Generated by Django 3.1.7 on 2021-04-01 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.CharField(max_length=255)),
                ('upload', models.FileField(upload_to='media/')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='descrição')),
                ('tipo', models.CharField(choices=[('', ''), ('Formulário', 'Formulário'), ('Manual', 'Manual')], max_length=255)),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
            ],
            options={
                'ordering': ['tipo', 'documento'],
            },
        ),
    ]
