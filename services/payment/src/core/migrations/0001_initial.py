# Generated by Django 5.0.2 on 2024-02-10 13:16

from django.db import migrations
from django.db import models
import django.db.models.deletion


class Migration(migrations.Migration):
	initial = True

	dependencies = []

	operations = [
		migrations.CreateModel(
			name='Product',
			fields=[
				(
					'id',
					models.BigAutoField(
						auto_created=True,
						primary_key=True,
						serialize=False,
						verbose_name='ID',
					),
				),
				('name', models.CharField(max_length=100)),
				('description', models.TextField()),
				('price', models.DecimalField(decimal_places=2, max_digits=10)),
				('quantity', models.PositiveIntegerField(default=0)),
			],
		),
		migrations.CreateModel(
			name='Reservation',
			fields=[
				(
					'id',
					models.BigAutoField(
						auto_created=True,
						primary_key=True,
						serialize=False,
						verbose_name='ID',
					),
				),
				('amount', models.DecimalField(decimal_places=2, max_digits=10)),
				('created', models.DateTimeField(auto_now_add=True)),
				(
					'status',
					models.CharField(
						choices=[
							('PENDING', 'Pending'),
							('PENDING', 'Confirmed'),
							('PENDING', 'Cancelled'),
						],
						default='pending',
						max_length=20,
					),
				),
				('modified', models.DateTimeField(auto_now=True)),
				('transaction_id', models.CharField(max_length=100)),
			],
		),
		migrations.CreateModel(
			name='ReservationItem',
			fields=[
				(
					'id',
					models.BigAutoField(
						auto_created=True,
						primary_key=True,
						serialize=False,
						verbose_name='ID',
					),
				),
				('quantity', models.PositiveIntegerField()),
				('price', models.DecimalField(decimal_places=2, max_digits=10)),
				(
					'product',
					models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product'),
				),
				(
					'reservation',
					models.ForeignKey(
						on_delete=django.db.models.deletion.CASCADE,
						to='core.reservation',
					),
				),
			],
		),
	]
