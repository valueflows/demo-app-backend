#
# Economic Event: An inflow or outflow of an economic resource in relation to a process and/or exchange. This could reflect a change in the quantity of a EconomicResource. It is also defined by its behavior in relation to the EconomicResource and a Process (consume, use, produce, etc.)" .
#

from django.core.exceptions import PermissionDenied

import graphene
from graphene_django.types import DjangoObjectType
import valuenetwork.api.types as types
from valuenetwork.api.schemas.Auth import _authUser
from api.types.Measure import Unit, Measure
from valuenetwork.valueaccounting.models import VocabEconomicEvent, VocabEconomicResource, VocabMeasure, VocabAction, VocabAgentUser, VocabFulfillment
from valuenetwork.api.models import formatAgent, Person, Organization


class Action(DjangoObjectType):
    label = graphene.String(source='label')
    note = graphene.String(source='note')
    resource_effect = graphene.String(source='resource_effect')
    onhand_effect = graphene.String(source='onhand_effect')
    input_output = graphene.String(source='input_output')
    pairs_with = graphene.String(source='pairs_with')
    
    class Meta:
        model = VocabAction
        only_fields = ('id')    


class EconomicEvent(DjangoObjectType):
    action = graphene.Field(Action)
    input_of = graphene.Field(lambda: types.Process)
    output_of = graphene.Field(lambda: types.Process)
    provider = graphene.Field(lambda: types.Agent)
    receiver = graphene.Field(lambda: types.Agent)
    in_scope_of = graphene.Field(lambda: types.Agent)
    resource_inventoried_as = graphene.Field(lambda: types.EconomicResource)
    to_resource_inventoried_as = graphene.Field(lambda: types.EconomicResource)
    resource_quantity = graphene.Field(lambda: types.Measure)
    effort_quantity = graphene.Field(lambda: types.Measure)
    has_point_in_time = graphene.String(source='has_point_in_time')
    has_beginning = graphene.String(source='has_beginning')
    has_end = graphene.String(source='has_end')
    #url = graphene.String(source='url')
    #request_distribution = graphene.Boolean(source='is_contribution')
    note = graphene.String(source='note')

    class Meta:
        model = VocabEconomicEvent
        only_fields = ('id')

    #fulfills = graphene.List(lambda: types.Fulfillment)
    
    #validations = graphene.List(lambda: types.Validation)

    #is_validated = graphene.Boolean()

    #user_is_authorized_to_update = graphene.Boolean()

    #user_is_authorized_to_delete = graphene.Boolean()

    def resolve_input_of(self, args, *rargs):
        return self.input_of

    def resolve_output_of(self, args, *rargs):
        return self.output_of

    def resolve_provider(self, args, *rargs):
        return formatAgent(self.provider)

    def resolve_receiver(self, args, *rargs):
        return formatAgent(self.receiver)

    def resolve_in_scope_of(self, args, *rargs):
        return formatAgent(self.in_scope_of)

    #def resolve_affected_taxonomy_item(self, args, *rargs):
    #    return self.affected_taxonomy_item

    def resolve_resource_inventoried_as(self, args, *rargs):
        res = self.resource_inventoried_as
        #if res == None:
        #    res = EconomicResourceProxy(resource_type=self.affected_resource_classified_as)
        return res

    def resolve_resource_quantity(self, args, *rargs):
        return self.resource_quantity #MeasureProxy(has_numerical_value=self.quantity, unit=self.unit_of_quantity)
        
    def resolve_effort_quantity(self, args, *rargs):
        return self.effort_quantity
        
    def resolve_action(self, args, *rargs):
        return self.action

    # This is valid only for process related events, may need to re-look at when doing exchanges
    #def resolve_fulfills(self, args, context, info):
    #    commitment = self.commitment
    #    if commitment:
    #        fulfillment = Fulfillment(
    #            fulfilled_by=self,
    #            fulfills=commitment,
    #            fulfilled_quantity=QuantityValueProxy(numeric_value=self.quantity, unit=self.unit_of_quantity),
    #            )
    #        ff_list = []
    #        ff_list.append(fulfillment)
    #        return ff_list
    #    return []

    #def resolve_validations(self, args, context, info):
    #    return self.validations.all()
    
    #def resolve_is_validated(self, args, *rargs):
    #    return self.is_double_validated()

    #def resolve_user_is_authorized_to_update(self, args, context, *rargs):
    #    token = rargs[0].variable_values['token']
    #    context.user = _authUser(token)
    #    user_agent = AgentUser.objects.get(user=context.user).agent
    #    return user_agent.is_authorized(object_to_mutate=self)

    #def resolve_user_is_authorized_to_delete(self, args, context, *rargs):
    #    token = rargs[0].variable_values['token']
    #    context.user = _authUser(token)
    #    user_agent = AgentUser.objects.get(user=context.user).agent
    #    return user_agent.is_authorized(object_to_mutate=self)


class Fulfillment(DjangoObjectType):

    class Meta:
        model = VocabFulfillment
        only_fields = ('id', 'fulfilled_by', 'fulfills', 'resource_quantity', 'effort_quantity', 'note')

