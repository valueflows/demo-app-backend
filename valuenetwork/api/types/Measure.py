#
# Measure: A numeric amount and a unit, bundled.
#

import graphene
from graphene_django.types import DjangoObjectType
from valuenetwork.valueaccounting.models import VocabMeasure, VocabUnit


class Unit(DjangoObjectType):

    class Meta:
        model = VocabUnit
        only_fields = ('id', 'label', 'symbol')


class Measure(DjangoObjectType):

    #has_numerical_value = graphene.Float(source='has_numerical_value')
    has_unit = graphene.Field(Unit)

    class Meta:
        model = VocabMeasure
        only_fields = ('id', 'has_numerical_value')

    def resolve_unit(self, args, *rargs):
        return self.unit
