# Generated by Django 3.0.7 on 2020-08-11 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule_name', models.CharField(max_length=50)),
                ('svid', models.CharField(max_length=10)),
                ('language', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('vulnerability', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('match_mode', models.CharField(max_length=50)),
                ('match', models.CharField(max_length=200)),
                ('vul_function', models.CharField(default=None, max_length=30)),
                ('main_function', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ScanResultTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scan_task_id', models.IntegerField()),
                ('result_id', models.IntegerField()),
                ('cvi_id', models.CharField(max_length=20)),
                ('rule_id', models.IntegerField()),
                ('language', models.CharField(max_length=20)),
                ('vulfile_path', models.CharField(max_length=200)),
                ('source_code', models.CharField(max_length=200)),
                ('rule_type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ScanTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=50)),
                ('target_path', models.CharField(max_length=300)),
                ('parameter_config', models.CharField(max_length=100)),
                ('last_scan_time', models.DateTimeField(auto_now=True)),
                ('is_finished', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tampers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tam_name', models.CharField(max_length=30)),
                ('tam_type', models.IntegerField()),
                ('tam_key', models.CharField(max_length=200)),
                ('tam_value', models.CharField(max_length=200)),
            ],
        ),
    ]
