# Generated by Django 5.0.2 on 2024-02-12 14:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nxtTransport', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_location', models.CharField(choices=[('Mumbai', 'Mumbai'), ('Delhi', 'Delhi'), ('Bangalore', 'Bangalore'), ('Kolkata', 'Kolkata'), ('Chennai', 'Chennai'), ('Hyderabad', 'Hyderabad'), ('Pune', 'Pune'), ('Ahmedabad', 'Ahmedabad'), ('Surat', 'Surat'), ('Jaipur', 'Jaipur'), ('Lucknow', 'Lucknow'), ('Kanpur', 'Kanpur'), ('Nagpur', 'Nagpur'), ('Visakhapatnam', 'Visakhapatnam'), ('Indore', 'Indore'), ('Thane', 'Thane'), ('Bhopal', 'Bhopal'), ('Patna', 'Patna'), ('Vadodara', 'Vadodara'), ('Ghaziabad', 'Ghaziabad')], max_length=100)),
                ('to_location', models.CharField(choices=[('Mumbai', 'Mumbai'), ('Delhi', 'Delhi'), ('Bangalore', 'Bangalore'), ('Kolkata', 'Kolkata'), ('Chennai', 'Chennai'), ('Hyderabad', 'Hyderabad'), ('Pune', 'Pune'), ('Ahmedabad', 'Ahmedabad'), ('Surat', 'Surat'), ('Jaipur', 'Jaipur'), ('Lucknow', 'Lucknow'), ('Kanpur', 'Kanpur'), ('Nagpur', 'Nagpur'), ('Visakhapatnam', 'Visakhapatnam'), ('Indore', 'Indore'), ('Thane', 'Thane'), ('Bhopal', 'Bhopal'), ('Patna', 'Patna'), ('Vadodara', 'Vadodara'), ('Ghaziabad', 'Ghaziabad')], max_length=100)),
                ('date', models.DateField()),
                ('receiver_mobilenumber', models.CharField(max_length=15)),
                ('quantity', models.PositiveIntegerField()),
                ('asset_type', models.CharField(choices=[('LAPTOP', 'Laptop'), ('TRAVEL_BAG', 'Travel Bag'), ('PACKAGE', 'Package')], max_length=20)),
                ('sensitivity', models.CharField(choices=[('HIGHLY_SENSITIVE', 'Highly Sensitive'), ('SENSITIVE', 'Sensitive'), ('NORMAL', 'Normal')], max_length=20)),
                ('requester_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nxtTransport.user')),
            ],
        ),
    ]
