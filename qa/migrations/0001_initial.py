# Generated by Django 2.1.3 on 2018-11-29 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_auto_20181129_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=30000)),
                ('up_votes', models.IntegerField()),
                ('down_votes', models.IntegerField()),
                ('answerer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='answers', to='users.Gucian')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=350)),
                ('code', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('text', models.CharField(max_length=30000)),
                ('up_votes', models.IntegerField()),
                ('down_votes', models.IntegerField()),
                ('asker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='questions', to='users.Gucian')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='questions', to='qa.Course')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='qa.Question'),
        ),
    ]
