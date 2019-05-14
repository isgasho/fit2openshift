# Generated by Django 2.1.2 on 2019-05-14 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('ansible_api', '0003_auto_20190412_1030'),
        ('openshift_client', '0003_auto_20190506_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project',
            field=models.ForeignKey(default='787ccb83487a47a6b83fff483b6d0ffd',
                                    on_delete=django.db.models.deletion.CASCADE, to='ansible_api.Project'),
            preserve_default=False,
        ),
    ]
