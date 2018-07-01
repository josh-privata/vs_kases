# Generated by Django 2.0.3 on 2018-07-01 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalTask',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('description', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified', models.DateTimeField(editable=False, null=True, verbose_name='Modification date and time')),
                ('title', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Task Title')),
                ('background', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Task Background')),
                ('location', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Task Location')),
                ('private', models.BooleanField(default=False, verbose_name='Private')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='Evidence Slug')),
                ('date_added', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Date Added')),
                ('deadline', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Deadline')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('assigned_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Task',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified', models.DateTimeField(editable=False, null=True, verbose_name='Modification date and time')),
                ('title', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Task Title')),
                ('background', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Task Background')),
                ('location', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Task Location')),
                ('private', models.BooleanField(default=False, verbose_name='Private')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Evidence Slug')),
                ('date_added', models.DateTimeField(auto_now=True, null=True, verbose_name='Date Added')),
                ('deadline', models.DateTimeField(auto_now=True, null=True, verbose_name='Deadline')),
                ('assigned_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_assigned_by', to=settings.AUTH_USER_MODEL, verbose_name='Assigned By')),
                ('assigned_to', models.ManyToManyField(blank=True, related_name='task_assigned_to', to=settings.AUTH_USER_MODEL, verbose_name='Assigned To')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
        migrations.CreateModel(
            name='TaskAuthorisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified', models.DateTimeField(editable=False, null=True, verbose_name='Modification date and time')),
                ('title', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Authorisation')),
            ],
            options={
                'verbose_name': 'Task Authorisation',
                'verbose_name_plural': 'Task Authorisations',
            },
        ),
        migrations.CreateModel(
            name='TaskCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified', models.DateTimeField(editable=False, null=True, verbose_name='Modification date and time')),
                ('title', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Task Category',
                'verbose_name_plural': 'Task Categories',
            },
        ),
        migrations.CreateModel(
            name='TaskClassification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified', models.DateTimeField(editable=False, null=True, verbose_name='Modification date and time')),
                ('title', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Classification')),
            ],
            options={
                'verbose_name': 'Task Classification',
                'verbose_name_plural': 'Task Classifications',
            },
        ),
        migrations.CreateModel(
            name='TaskPriority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified', models.DateTimeField(editable=False, null=True, verbose_name='Modification date and time')),
                ('title', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Priority')),
                ('colour', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Colour')),
            ],
            options={
                'verbose_name': 'Task Priority',
                'verbose_name_plural': 'Task Priorities',
            },
        ),
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified', models.DateTimeField(editable=False, null=True, verbose_name='Modification date and time')),
                ('title', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Task Status',
                'verbose_name_plural': 'Task Status',
            },
        ),
        migrations.CreateModel(
            name='TaskStatusGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified', models.DateTimeField(editable=False, null=True, verbose_name='Modification date and time')),
                ('title', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Status Group')),
                ('status', models.ManyToManyField(blank=True, to='task.TaskStatus', verbose_name='Task Status')),
            ],
            options={
                'verbose_name': 'Task Status Group',
                'verbose_name_plural': 'Task Status Groups',
            },
        ),
        migrations.CreateModel(
            name='TaskType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified', models.DateTimeField(editable=False, null=True, verbose_name='Modification date and time')),
                ('title', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Type')),
            ],
            options={
                'verbose_name': 'Task Type',
                'verbose_name_plural': 'Task Types',
            },
        ),
        migrations.AddField(
            model_name='task',
            name='authorisation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='task.TaskAuthorisation', verbose_name='Task Authorisation'),
        ),
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='task.TaskCategory', verbose_name='Task Category'),
        ),
        migrations.AddField(
            model_name='task',
            name='classification',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='task.TaskClassification', verbose_name='Task Classification'),
        ),
        migrations.AddField(
            model_name='task',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_manager', to=settings.AUTH_USER_MODEL, verbose_name='Case Manager'),
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='task.TaskPriority', verbose_name='Task Priority'),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='task.TaskStatus', verbose_name='Task Status'),
        ),
        migrations.AddField(
            model_name='task',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='task.TaskType', verbose_name='Task Type'),
        ),
        migrations.AddField(
            model_name='historicaltask',
            name='authorisation',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='task.TaskAuthorisation'),
        ),
        migrations.AddField(
            model_name='historicaltask',
            name='category',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='task.TaskCategory'),
        ),
        migrations.AddField(
            model_name='historicaltask',
            name='classification',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='task.TaskClassification'),
        ),
        migrations.AddField(
            model_name='historicaltask',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicaltask',
            name='manager',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicaltask',
            name='priority',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='task.TaskPriority'),
        ),
        migrations.AddField(
            model_name='historicaltask',
            name='status',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='task.TaskStatus'),
        ),
        migrations.AddField(
            model_name='historicaltask',
            name='type',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='task.TaskType'),
        ),
    ]
