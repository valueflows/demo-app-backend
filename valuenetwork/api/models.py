from django.db import models

from valuenetwork.valueaccounting.models import Unit, EconomicEvent, Commitment, VocabAgent #, Location
from decimal import *

# Helpers for dealing with Agent polymorphism

def formatAgent(agent):
    if agent:
        if agent.agent_subclass == "Person": #agent.agent_type.party_type == "individual":
            return Person(
                id=agent.id,
                name = agent.name,
                note = agent.note,
                #primary_location = agent.primary_location,
                #primary_phone = agent.primary_phone,
                image = agent.image)
                #email = agent.email)
        else:
            return Organization(
                id=agent.id,
                name = agent.name,
                note = agent.note,
                image = agent.image)
                #is_context = agent.is_context,
                #primary_location = agent.primary_location,
                #primary_phone = agent.primary_phone,
                #email = agent.email)

def formatAgentList(agent_list):
    mixed_list = []
    for agent in agent_list:
        mixed_list.append(formatAgent(agent))
    return mixed_list

# Django model extensions for exposing OO type layer in Graphene, where the core doesn't directly support ValueFlows

class Organization(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    note = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True)
    #is_context = models.BooleanField(default=False)
    #type = models.CharField(max_length=255)
    #primary_location = models.ForeignKey(Location,
    #    related_name='orgs_at_location',
    #    blank=True, null=True,
    #    on_delete=models.DO_NOTHING)
    #primary_phone = models.CharField(max_length=32, blank=True, null=True)
    #email = models.EmailField(max_length=96, blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'api' # hack because of error not finding this in the settings.INSTALLED_APPS


class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    note = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True)
    #is_context = models.BooleanField(default=False)
    #type = models.CharField(max_length=255, default="Person")
    #primary_location = models.ForeignKey(Location,
    #    related_name='people_at_location',
    #    blank=True, null=True,
    #    on_delete=models.DO_NOTHING)
    #primary_phone = models.CharField(max_length=32, blank=True, null=True)
    #email = models.EmailField(max_length=96, blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'api' # hack because of error not finding this in the settings.INSTALLED_APPS
