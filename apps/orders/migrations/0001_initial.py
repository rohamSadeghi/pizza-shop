# Generated by Django 3.2.5 on 2021-07-09 22:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderPizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='updated time')),
                ('price', models.PositiveIntegerField(verbose_name='price')),
                ('is_paid', models.BooleanField(default=False, verbose_name='is paid')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('is_enable', models.BooleanField(default=True, verbose_name='is enable')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='pizzas.pizza', verbose_name='pizza')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
    ]