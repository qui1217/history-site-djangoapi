# Generated by Django 3.1 on 2021-03-04 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_api', '0002_remove_content_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tag', to='school_api.tag'),
        ),
    ]
