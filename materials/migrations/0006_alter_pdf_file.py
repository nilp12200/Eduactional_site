# Generated by Django 4.2.3 on 2024-11-19 11:44

from django.db import migrations, models
import materials.models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0005_delete_educationalmaterial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='file',
            field=models.FileField(upload_to='pdfs/', validators=[materials.models.validate_pdf]),
        ),
    ]
