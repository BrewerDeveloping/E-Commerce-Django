# Generated by Django 4.1.7 on 2023-05-15 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brew_clothing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='title',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='brew_clothing.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='shopping_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brew_clothing.product')),
            ],
        ),
    ]