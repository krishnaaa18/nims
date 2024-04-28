# Generated by Django 5.0.4 on 2024-04-18 21:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_menu_persons'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_needed', models.IntegerField(choices=[(5, '5 minutes'), (10, '10 minutes'), (15, '15 minutes')], default=5)),
                ('status', models.CharField(choices=[('preparing', 'Preparing'), ('ready', 'Ready'), ('delivered', 'Delivered')], default='preparing', max_length=20)),
                ('order', models.ForeignKey(limit_choices_to={'approved': True, 'complete': True}, on_delete=django.db.models.deletion.CASCADE, related_name='chefs', to='main.order')),
            ],
        ),
    ]
