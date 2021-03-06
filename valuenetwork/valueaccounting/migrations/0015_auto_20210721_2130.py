# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2021-07-21 21:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('valueaccounting', '0014_auto_20210720_2221'),
    ]

    operations = [
        migrations.CreateModel(
            name='VocabAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('changed_date', models.DateField(auto_now=True, null=True)),
                ('label', models.CharField(blank=True, max_length=255, null=True, verbose_name='label')),
                ('note', models.TextField(blank=True, null=True, verbose_name='note')),
                ('resource_effect', models.CharField(blank=True, choices=[(b'increment', 'Increment'), (b'decrement', 'Decrement'), (b'decr_incr', 'Decrement Increment'), (b'no_effect', 'No Effect')], max_length=16, null=True, verbose_name='resource effect')),
                ('onhand_effect', models.CharField(blank=True, choices=[(b'increment', 'Increment'), (b'decrement', 'Decrement'), (b'decr_incr', 'Decrement Increment'), (b'no_effect', 'No Effect')], max_length=16, null=True, verbose_name='onhand effect')),
                ('input_output', models.CharField(blank=True, choices=[(b'input', 'Input'), (b'output', 'Output'), (b'not_applicable', 'N/A')], max_length=16, null=True, verbose_name='input output')),
                ('pairs_with', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='action_paired_with', to='valueaccounting.VocabAction', verbose_name='pairs with')),
            ],
            options={
                'ordering': ('label',),
            },
        ),
        migrations.CreateModel(
            name='VocabAgentUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='valueaccounting.VocabAgent', verbose_name='agent')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vocab_agent', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.CreateModel(
            name='VocabCommitment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('changed_date', models.DateField(auto_now=True, null=True)),
                ('resource_classified_as', models.TextField(blank=True, null=True, verbose_name='resource classified as')),
                ('url', models.URLField(blank=True, verbose_name='url')),
                ('note', models.TextField(blank=True, null=True, verbose_name='note')),
                ('has_point_in_time', models.DateTimeField(blank=True, null=True, verbose_name='has point in time')),
                ('has_beginning', models.DateTimeField(blank=True, null=True, verbose_name='beginning')),
                ('has_end', models.DateTimeField(blank=True, null=True, verbose_name='end')),
                ('image', models.URLField(blank=True, null=True, verbose_name='image')),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commitments', to='valueaccounting.VocabAction', verbose_name='action')),
                ('changed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vocab_commitments_changed', to=settings.AUTH_USER_MODEL, verbose_name='changed by')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vocab_commitments_created', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('effort_quantity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commitments_effort', to='valueaccounting.VocabMeasure', verbose_name='effort quantity')),
                ('in_scope_of', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commitments', to='valueaccounting.VocabAgent', verbose_name='scope')),
                ('input_of', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='planned_inputs_of', to='valueaccounting.VocabProcess', verbose_name='planned input of')),
                ('output_of', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='planned_outputs_of', to='valueaccounting.VocabProcess', verbose_name='planned output of')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provided_commitments', to='valueaccounting.VocabAgent', verbose_name='provider')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_commitments', to='valueaccounting.VocabAgent', verbose_name='receiver')),
            ],
            options={
                'ordering': ('-has_point_in_time',),
            },
        ),
        migrations.CreateModel(
            name='VocabEconomicEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('changed_date', models.DateField(auto_now=True, null=True)),
                ('resource_classified_as', models.TextField(blank=True, null=True, verbose_name='resource classified as')),
                ('url', models.URLField(blank=True, verbose_name='url')),
                ('note', models.TextField(blank=True, null=True, verbose_name='note')),
                ('has_point_in_time', models.DateTimeField(blank=True, null=True, verbose_name='has point in time')),
                ('has_beginning', models.DateTimeField(blank=True, null=True, verbose_name='beginning')),
                ('has_end', models.DateTimeField(blank=True, null=True, verbose_name='end')),
                ('image', models.URLField(blank=True, null=True, verbose_name='image')),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='valueaccounting.VocabAction', verbose_name='action')),
                ('changed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vocab_events_changed', to=settings.AUTH_USER_MODEL, verbose_name='changed by')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vocab_events_created', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('effort_quantity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events_effort', to='valueaccounting.VocabMeasure', verbose_name='effort quantity')),
                ('in_scope_of', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='valueaccounting.VocabAgent', verbose_name='scope')),
                ('input_of', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inputs_of', to='valueaccounting.VocabProcess', verbose_name='input of')),
                ('output_of', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='outputs_of', to='valueaccounting.VocabProcess', verbose_name='output of')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provided_events', to='valueaccounting.VocabAgent', verbose_name='provider')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_events', to='valueaccounting.VocabAgent', verbose_name='receiver')),
            ],
            options={
                'ordering': ('-has_point_in_time',),
            },
        ),
        migrations.CreateModel(
            name='VocabEconomicResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('changed_date', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('url', models.URLField(blank=True, verbose_name='url')),
                ('tracking_identifier', models.CharField(blank=True, max_length=255, null=True, verbose_name='tracking identifier')),
                ('classified_as', models.TextField(blank=True, null=True, verbose_name='classified as')),
                ('image', models.URLField(blank=True, null=True, verbose_name='image')),
                ('state', models.CharField(blank=True, max_length=255, null=True, verbose_name='state')),
                ('note', models.TextField(blank=True, null=True, verbose_name='note')),
                ('accounting_quantity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resource_accounting_quantity', to='valueaccounting.VocabMeasure', verbose_name='accounting quantity')),
                ('changed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vocab_resources_changed', to=settings.AUTH_USER_MODEL, verbose_name='changed by')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='VocabFulfillment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('changed_date', models.DateField(auto_now=True, null=True)),
                ('note', models.TextField(blank=True, null=True, verbose_name='note')),
                ('changed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fulfillments_changed', to=settings.AUTH_USER_MODEL, verbose_name='changed by')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fulfillments_created', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('effort_quantity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fulfillments_effort', to='valueaccounting.VocabMeasure', verbose_name='effort quantity')),
                ('fulfilled_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fulfills', to='valueaccounting.VocabEconomicEvent', verbose_name='fulfilled by')),
                ('fulfills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fulfilled_by', to='valueaccounting.VocabCommitment', verbose_name='fulfills')),
                ('resource_quantity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fulfillments_resource', to='valueaccounting.VocabMeasure', verbose_name='resource quantity')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VocabResourceSpecification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('changed_date', models.DateField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('image', models.URLField(blank=True, verbose_name='image')),
                ('resourceClassifiedAs', models.URLField(blank=True, verbose_name='classified as')),
                ('note', models.TextField(blank=True, null=True, verbose_name='note')),
                ('changed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resource_specifications_changed', to=settings.AUTH_USER_MODEL, verbose_name='changed by')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resource_specifications_created', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('defaultUnitOfEffort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resource_specifications_effort', to='valueaccounting.VocabUnit', verbose_name='default unit of effort')),
                ('defaultUnitOfResource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resource_specifications_resource', to='valueaccounting.VocabUnit', verbose_name='default unit of resource')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='vocabeconomicresource',
            name='conforms_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='valueaccounting.VocabResourceSpecification', verbose_name='conforms to'),
        ),
        migrations.AddField(
            model_name='vocabeconomicresource',
            name='contained_in',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contains', to='valueaccounting.VocabEconomicResource', verbose_name='contained in'),
        ),
        migrations.AddField(
            model_name='vocabeconomicresource',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vocab_resources_created', to=settings.AUTH_USER_MODEL, verbose_name='created by'),
        ),
        migrations.AddField(
            model_name='vocabeconomicresource',
            name='onhand_quantity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resource_onhand_quantity', to='valueaccounting.VocabMeasure', verbose_name='onhand quantity'),
        ),
        migrations.AddField(
            model_name='vocabeconomicresource',
            name='primary_accountable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accountable_for_resources', to='valueaccounting.VocabAgent', verbose_name='primary accountable'),
        ),
        migrations.AddField(
            model_name='vocabeconomicresource',
            name='unit_of_effort',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='effort_unit_resources', to='valueaccounting.VocabUnit', verbose_name='unit of effort'),
        ),
        migrations.AddField(
            model_name='vocabeconomicevent',
            name='resource_conforms_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='economic_events', to='valueaccounting.VocabResourceSpecification', verbose_name='conforms to'),
        ),
        migrations.AddField(
            model_name='vocabeconomicevent',
            name='resource_inventoried_as',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='valueaccounting.VocabEconomicResource', verbose_name='resource inventoried as'),
        ),
        migrations.AddField(
            model_name='vocabeconomicevent',
            name='resource_quantity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events_resource', to='valueaccounting.VocabMeasure', verbose_name='resource quantity'),
        ),
        migrations.AddField(
            model_name='vocabeconomicevent',
            name='to_resource_inventoried_as',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events_to', to='valueaccounting.VocabEconomicResource', verbose_name='to resource inventoried as'),
        ),
        migrations.AddField(
            model_name='vocabcommitment',
            name='resource_conforms_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commitments', to='valueaccounting.VocabResourceSpecification', verbose_name='conforms to'),
        ),
        migrations.AddField(
            model_name='vocabcommitment',
            name='resource_inventoried_as',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commitments', to='valueaccounting.VocabEconomicResource', verbose_name='resource inventoried as'),
        ),
        migrations.AddField(
            model_name='vocabcommitment',
            name='resource_quantity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commitments_resource', to='valueaccounting.VocabMeasure', verbose_name='resource quantity'),
        ),
    ]
