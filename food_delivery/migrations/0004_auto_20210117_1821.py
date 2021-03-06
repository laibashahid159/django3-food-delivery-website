# Generated by Django 3.1.3 on 2021-01-17 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_delivery', '0003_auto_20210117_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('digital', models.BooleanField(blank=True, default=False, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='owner',
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='food_delivery.customer'),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='food_delivery.customer'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='food_delivery.product'),
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]
