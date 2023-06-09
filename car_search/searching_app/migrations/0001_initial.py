# Generated by Django 3.2.4 on 2023-05-25 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zip', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('truck_number', models.CharField(max_length=5, unique=True)),
                ('carrying_capacity', models.IntegerField()),
                ('current_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='searching_app.location')),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('description', models.TextField()),
                ('delivery_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_shipments', to='searching_app.location')),
                ('pick_up_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pick_up_shipments', to='searching_app.location')),
            ],
        ),
    ]
