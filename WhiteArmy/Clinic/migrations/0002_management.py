# Generated by Django 3.1.6 on 2021-02-27 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clinic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='management',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatment', models.CharField(max_length=200)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patient', to='Clinic.id')),
            ],
        ),
    ]