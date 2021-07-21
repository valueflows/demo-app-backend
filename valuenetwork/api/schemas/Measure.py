#
# Graphene schema for exposing Measure model
#   Note: Measure does not stand on its own, it is a bundling of number and unit for handling quantities in other classes
#

import graphene
from graphene_django.types import DjangoObjectType

from valuenetwork.valueaccounting.models import VocabMeasure
from valuenetwork.api.types.Measure import Measure


class Query(graphene.AbstractType):

    # define input query params

    measure = graphene.Field(Measure,
                             id=graphene.Int())

    # resolve methods

    def resolve_measure(self, args, *rargs):
        id = args.get('id')
        if id is not None:
            qv = VocabMeasure.objects.get(pk=id)
            if qv:
                return qv
        return None
