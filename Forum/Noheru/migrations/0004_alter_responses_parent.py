# Generated by Django 5.0.1 on 2024-02-11 18:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Noheru', '0003_alter_posts_post_publish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responses',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Noheru.responses'),
        ),
    ]
