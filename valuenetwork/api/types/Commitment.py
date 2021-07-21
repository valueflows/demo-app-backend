#
# Commitment: A planned economic event or transfer that has been promised by an agent to another agent.
#
"""
import jwt
import graphene
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied

from graphene_django.types import DjangoObjectType

import valuenetwork.api.types as types
from valuenetwork.api.types.Measure import Unit, Measure
from valuenetwork.api.schemas.Auth import _authUser
from valuenetwork.valueaccounting.models import Commitment as CommitmentProxy, Measure as MeasureProxy #, AgentUser
from valuenetwork.api.models import formatAgent, Person, Organization #, Fulfillment as FulfillmentProxy


class Commitment(DjangoObjectType):
    action = graphene.String(source='action')
    #input_of = graphene.Field(lambda: types.Process)
    #output_of = graphene.Field(lambda: types.Process)
    #provider = graphene.Field(lambda: types.Agent)
    #receiver = graphene.Field(lambda: types.Agent)
    #in_scope_of = graphene.Field(lambda: types.Agent)
    #resource_conforms_to = graphene.Field(lambda: types.ResourceSpecification)
    resource_classified_as = graphene.String(source='resource_classified_as')
    #resource_inventoried_as = graphene.Field(lambda: types.EconomicResource)
    #resource_quantity = graphene.Field(lambda: types.Measure)
    #effort_quantity = graphene.Field(lambda: types.Measure)
    created = graphene.String(source='created')
    has_beginning = graphene.String(source='has_beginning')
    has_end = graphene.String(source='has_end')
    has_point_in_time = graphene.String(source='has_point_in_time')
    due = graphene.String(source='due')
    finished = graphene.Boolean(source='finished')
    #independendent_demand_of = graphene.Field(lambda: types.Plan)
    image = graphene.String(source='image')
    #realization_of =
    #agreed_in =
    #at_location =
    note = graphene.String(source='note')

    class Meta:
        model = VocabCommitment
        only_fields = ('id')

    """
    fulfilled_by = graphene.List(lambda: types.Fulfillment,
                                 request_distribution=graphene.Boolean())

    involved_agents = graphene.List(lambda: types.Agent)
    """
    #deletable = graphene.Boolean()

    #user_is_authorized_to_update = graphene.Boolean()

    #user_is_authorized_to_delete = graphene.Boolean()

    #def resolve_process(self, args, *rargs):
    #    return self.process

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

    def resolve_involves(self, args, *rargs):
        return self.involves

    def resolve_resource_classified_as(self, args, *rargs):
        return self.resource_classified_as

    def resolve_resource_quantity(self, args, *rargs):
        return self.resource_quantity

    def resolve_effort_quantity(self, args, *rargs):
        return self.effort_quantity

    def resolve_plan(self, args, *rargs):
        return self.independent_demand

    def resolve_for_plan_deliverable(self, args, *rargs):
        return self.order_item

    def resolve_fulfilled_by(self, args, context, info):
        events = self.fulfillment_events.all()
        request_distribution = args.get('request_distribution')
        if request_distribution != None:
            events = events.filter(is_contribution=request_distribution)
        fulfillments = []
        for event in events:
            fulfill = FulfillmentProxy(
                fulfilled_by=event,
                fulfills=self,
                fulfilled_quantity=QuantityValueProxy(numeric_value=event.quantity, unit=event.unit_of_quantity),
                )
            fulfillments.append(fulfill)
        return fulfillments

    def resolve_involved_agents(self, args, context, info):
        involved = []
        if self.provider:
            involved.append(formatAgent(self.provider))
        events = self.fulfillment_events.all()
        for event in events:
            if event.provider:
                involved.append(formatAgent(event.provider))
        return list(set(involved))

    def resolve_is_deletable(self, args, *rargs):
        return self.is_deletable()

    def resolve_user_is_authorized_to_update(self, args, context, *rargs):
        token = rargs[0].variable_values['token']
        context.user = _authUser(token)
        user_agent = AgentUser.objects.get(user=context.user).agent
        return user_agent.is_authorized(object_to_mutate=self)

    def resolve_user_is_authorized_to_delete(self, args, context, *rargs):
        token = rargs[0].variable_values['token']
        context.user = _authUser(token)
        user_agent = AgentUser.objects.get(user=context.user).agent
        return user_agent.is_authorized(object_to_mutate=self)
"""
