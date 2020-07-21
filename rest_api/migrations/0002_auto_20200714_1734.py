# Generated by Django 3.0.8 on 2020-07-14 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='pub_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='university',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='news', to='rest_api.University'),
        ),
    ]