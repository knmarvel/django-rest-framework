# Generated by Django 3.0.7 on 2020-06-17 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoeinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='shoe_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoeinfo.ShoeType'),
        ),
    ]
