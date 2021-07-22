#
# Graphene schema for exposing Fulfillment
#

import graphene
from valuenetwork.valueaccounting.models import VocabFulfillment
from valuenetwork.api.types.EconomicEvent import Fulfillment


class Query(graphene.AbstractType):

    # define input query params

    fulfillment = graphene.Field(Fulfillment,
                                id=graphene.Int())

    # resolvers

    def resolve_fulfillment(self, args, *rargs):
        id = args.get('id')
        if id is not None:
            ff = VocabFulfillment.objects.get(pk=id)
            if ff:
                return ff
        return None

