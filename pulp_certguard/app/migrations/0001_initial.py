# Generated by Django 2.2.3 on 2019-09-04 19:05

from django.db import migrations, models
import django.db.models.deletion
import pulp_certguard.app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0004_add_duplicated_reserved_resources'),
    ]

    operations = [
        migrations.CreateModel(
            name='X509CertGuard',
            fields=[
                ('contentguard_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='certguard_x509certguard', serialize=False, to='core.ContentGuard')),
                ('ca_certificate', models.FileField(max_length=255, upload_to=pulp_certguard.app.models.X509CertGuard._certpath)),
            ],
            options={
                'default_related_name': '%(app_label)s_%(model_name)s',
            },
            bases=('core.contentguard',),
        ),
    ]
