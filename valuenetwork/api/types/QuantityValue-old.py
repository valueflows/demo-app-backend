#
# QuantityValue: A numeric amount and a unit, bundled.
#

import graphene
from graphene_django.types import DjangoObjectType
from valuenetwork.api.models import QuantityValue as QuantityValueProxy
from valuenetwork.valueaccounting.models import Unit as UnitProxy


class Unit(DjangoObjectType):

    class Meta:
        model = UnitProxy
        only_fields = ('id', 'name', 'symbol')


class QuantityValue(DjangoObjectType):

    numeric_value = graphene.Float(source='numeric_value')
    unit = graphene.Field(Unit)

    class Meta:
        model = QuantityValueProxy
        only_fields = ('numeric_value', 'unit')

    def resolve_unit(self, args, *rargs):
        return self.unit