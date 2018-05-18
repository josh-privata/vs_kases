# Generated by Django 2.0.3 on 2018-04-22 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_format', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('default_location', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('case_names', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('c_leading_date', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('c_list_name', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('task_names', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('t_list_name', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('company', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('department', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('date_created', models.DateTimeField(auto_now=True, null=True)),
                ('over_limit_case', models.BooleanField(default=False)),
                ('over_limit_task', models.BooleanField(default=False)),
                ('auth_view_tasks', models.BooleanField(default=False)),
                ('auth_view_evidence', models.BooleanField(default=False)),
                ('manager_inherit', models.BooleanField(default=False)),
                ('evidence_retention', models.BooleanField(default=False)),
                ('email_alert_all_inv_task_queued', models.BooleanField(default=False)),
                ('email_alert_inv_assigned_task', models.BooleanField(default=False)),
                ('email_alert_qa_assigned_task', models.BooleanField(default=False)),
                ('email_alert_caseman_inv_self_assigned', models.BooleanField(default=False)),
                ('email_alert_caseman_qa_self_assigned', models.BooleanField(default=False)),
                ('email_alert_req_task_completed', models.BooleanField(default=False)),
                ('email_alert_case_man_task_completed', models.BooleanField(default=False)),
                ('email_alert_all_caseman_new_case', models.BooleanField(default=False)),
                ('email_alert_all_caseman_case_auth', models.BooleanField(default=False)),
                ('email_alert_req_case_caseman_assigned', models.BooleanField(default=False)),
                ('email_alert_req_case_opened', models.BooleanField(default=False)),
                ('email_alert_req_case_closed', models.BooleanField(default=False)),
                ('email_alert_req_case_archived', models.BooleanField(default=False)),
                ('email_alert_caseman_requester_add_task', models.BooleanField(default=False)),
            ],
        ),
    ]
