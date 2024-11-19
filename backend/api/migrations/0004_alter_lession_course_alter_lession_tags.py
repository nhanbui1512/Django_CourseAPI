# Generated by Django 4.0.10 on 2024-11-19 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_tag_lession_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lession',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessions', to='api.course'),
        ),
        migrations.AlterField(
            model_name='lession',
            name='tags',
            field=models.ManyToManyField(blank=True, to='api.tag'),
        ),
    ]
