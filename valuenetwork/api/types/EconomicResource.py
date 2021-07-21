#
# EconomicResource:
#
"""
import graphene
from graphene_django.types import DjangoObjectType

import api.types as types
from vocab.models import EconomicResource as EconomicResourceProxy, Measure as MeasureProxy, ResourceSpecification #, Facet as FacetProxy, FacetValue as FacetValueProxy
from api.models import formatAgentList
from api.types.Measure import Unit, Measure


class EconomicResourceCategory(graphene.Enum):
    NONE = None
    CURRENCY = "currency"
    INVENTORY = "inventory"
    WORK = "work"
    #SERVICE = "service" TODO: work this in, might need a new event type in VF


class EconomicResourceProcessCategory(graphene.Enum):
    NONE = None
    CONSUMED = "consumed"
    USED = "used"
    CITED = "cited"
    PRODUCED = "produced"


class Facet(DjangoObjectType):

    class Meta:
        model = FacetProxy
        only_fields = ('id', 'name', 'description')

    facet_values = graphene.List(lambda: FacetValue)
    
    def resolve_facet_values(self, args, context, info):
        return self.values.all()

class FacetValue(DjangoObjectType):
    facet = graphene.List(lambda: types.Facet)

    class Meta:
        model = FacetValueProxy
        only_fields = ('id', 'value', 'description')


class ResourceSpecification(DjangoObjectType):
    image = graphene.String(source='image')
    note = graphene.String(source='note')
    resourceClassifiedAs = graphene.String(source='resource_classified_as')
    #process_category = graphene.String(source='process_category')
    default_unit_of_resource = graphene.Field(Unit)
    default_unit_of_effort = graphene.Field(Unit)

    class Meta:
        model = ResourceSpecification
        only_fields = ('id', 'name', 'unit')

    #classification_resources = graphene.List(lambda: EconomicResource)

    #classification_facet_values = graphene.List(lambda: FacetValue)

    #def resolve_classification_resources(self, args, context, info):
    #    return self.resources.all()

    #def resolve_classification_facet_values(self, args, context, info):
    #    return self.facets.all() #TODO in process, not working yet

class EconomicResource(DjangoObjectType):
    name = graphene.String(source='name')
    #conforms_to = graphene.Field(ResourceSpecification)
    classified_as = graphene.String(source='classified_as')
    conforms_to = graphene.Field(ResourceSpecification)
    tracking_identifier = graphene.String(source='tracking_identifier')
    #lot = 
    image = graphene.String(source='image')
    accounting_quantity = graphene.Field(Measure)
    onhand_quantity = graphene.Field(Measure)
    note = graphene.String(source='note')
    #current_location = graphene.Field(lambda: types.Place)
    unit_of_effort = graphene.Field(Unit)
    #primary_accountable = graphene.Field(lambda: types.Agent)
    #contained_in = graphene.Field(lambda: types.EconomicResource)
    created_date = graphene.String(source='created_date')

    class Meta:
        model = EconomicResourceProxy
        only_fields = ('id')

    #transfers = graphene.List(lambda: types.Transfer)

    #resource_contacts = graphene.List(lambda: types.Agent)
    
    #owners = graphene.List(lambda: types.Agent)

    def resolve_accounting_quantity(self, args, *rargs):
        return self.accounting_quantity #QuantityValueProxy(numeric_value=self.quantity, unit=self.unit)

    def resolve_onhand_quantity(self, args, *rargs):
        return self.onhand_quantity #QuantityValueProxy(numeric_value=self.quantity, unit=self.unit)

    def resolve_conforms_to(self, args, *rargs):
        return self.conforms_to

    #def resolve_current_location(self, args, *rargs):
    #    return self.current_location

    #def resolve_transfers(self, args, context, info):
    #    return self.transfers()

    #def resolve_resource_contacts(self, args, context, info):
    #    return formatAgentList(self.all_contact_agents())

    #def resolve_owners(self, args, context, info):
    #    return formatAgentList(self.owners())
"""
