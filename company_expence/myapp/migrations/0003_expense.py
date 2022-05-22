# Generated by Django 4.0.4 on 2022-05-22 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_delete_expense'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_comment', models.CharField(max_length=100)),
                ('expense_done_on', models.DateTimeField()),
                ('expense_amount', models.IntegerField()),
                ('employee_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.employee')),
                ('vendor_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.vendor')),
            ],
        ),
    ]
