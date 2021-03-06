# Generated by Django 4.0.3 on 2022-03-04 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('seller_id', models.AutoField(primary_key=True, serialize=False)),
                ('seller_name', models.CharField(max_length=20)),
                ('email_id', models.CharField(max_length=50)),
                ('acc_holedr', models.CharField(max_length=30)),
                ('acc_no', models.CharField(max_length=30)),
                ('ifsc', models.CharField(max_length=20)),
                ('phone_no', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'seller_tb',
            },
        ),
    ]
