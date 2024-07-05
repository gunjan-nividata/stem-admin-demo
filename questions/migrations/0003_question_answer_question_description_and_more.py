# Generated by Django 4.2.13 on 2024-07-05 10:41

from django.db import migrations, models
import django.db.models.deletion
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0001_initial'),
        ('questions', '0002_alter_question_explanation'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='description',
            field=froala_editor.fields.FroalaField(null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_id',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='configuration.subject'),
        ),
    ]
