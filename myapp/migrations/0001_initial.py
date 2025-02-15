# Generated by Django 4.2.16 on 2024-11-01 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('ma_kh', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerGroup',
            fields=[
                ('ma_nhom_kh', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('thong_tin_nhom_kh', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('ma_hoa_don', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nam', models.IntegerField(blank=True, null=True)),
                ('thang', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('ma_nhom_hang', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nhom_hang', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('ma_cua_hang', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('doanh_nghiep', models.CharField(blank=True, max_length=255, null=True)),
                ('dia_chi', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('ma_hang', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('mat_hang', models.CharField(blank=True, max_length=255, null=True)),
                ('dvt', models.CharField(blank=True, max_length=50, null=True)),
                ('don_gia', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ma_nhom_hang', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.productcategory')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sl_ban', models.IntegerField(blank=True, null=True)),
                ('tam_tinh', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.invoice')),
                ('ma_hang', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.product')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='ma_cua_hang',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.store'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='ma_kh',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.customer'),
        ),
        migrations.AddField(
            model_name='customer',
            name='ma_nhom_kh',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.customergroup'),
        ),
    ]
