# Generated by Django 2.1.2 on 2019-05-14 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openshift_api', '0008_auto_20190506_0748'),
    ]

    operations = [
        migrations.AddField(
            model_name='openshiftcluster',
            name='storage',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
    ]
