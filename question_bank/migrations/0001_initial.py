# Generated by Django 4.2.13 on 2024-07-05 13:12

from django.db import migrations, models
import django.db.models.deletion
import froala_editor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questions', '0003_question_answer_question_description_and_more'),
        ('configuration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Heading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.course')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.subject')),
            ],
            options={
                'verbose_name': 'heading',
                'verbose_name_plural': 'headings',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('heading', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_bank.heading')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='', verbose_name='module_image')),
                ('key_topics', froala_editor.fields.FroalaField()),
                ('access_type', models.CharField(choices=[(0, 'Free'), (1, 'Pro')], max_length=10)),
                ('questions', models.ManyToManyField(related_name='modules', to='questions.question')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question_bank.topic')),
            ],
        ),
    ]
