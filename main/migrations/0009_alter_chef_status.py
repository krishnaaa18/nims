# Generated by Django 5.0.4 on 2024-04-23 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_chef_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chef',
            name='status',
            field=models.CharField(choices=[('preparing', 'Preparing'), ('ready', 'Ready'), ('delivered', 'Delivered')], default='preparing', max_length=20),
        ),
    ]
