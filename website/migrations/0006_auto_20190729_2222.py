# Generated by Django 2.2.3 on 2019-07-30 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_ideia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='E-mail'),
        ),
    ]
