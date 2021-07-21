#
# Graphene schema for exposing Action model
#   
"""
import graphene
from graphene_django.types import DjangoObjectType

from valuenetwork.valueaccounting.models import VocabAction
from api.types.EconomicEvent import Action


class Query(graphene.AbstractType):

    # define input query params

    action = graphene.Field(Action,
                            id=graphene.Int())

    actions = graphene.List(Action)

    # resolve methods

    def resolve_action(self, args, *rargs):
        id = args.get('id')
        if id is not None:
            action = ActionProxy.objects.get(pk=id)
            if action:
                return action
        return None

    def resolve_actions(self, args, context, info):
        return ActionProxy.objects.all()
"""
