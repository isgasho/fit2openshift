# Generated by Django 2.1.2 on 2019-05-14 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openshift_api', '0009_openshiftcluster_storage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openshiftcluster',
            name='auth',
            field=models.CharField(blank=True, default='Htpasswd', max_length=128, null=True),
        ),
    ]
