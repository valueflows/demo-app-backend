#
# Agent relationship role schema
#

import graphene
from graphene_django.types import DjangoObjectType

from valuenetwork.valueaccounting.models import VocabAgentRelationshipRole
from valuenetwork.api.types.AgentRelationship import AgentRelationshipRole


class Query(graphene.AbstractType):

    agent_relationship_role = graphene.Field(AgentRelationshipRole,
                                            id=graphene.Int())

    agent_relationship_roles = graphene.List(AgentRelationshipRole)


    def resolve_agent_relationship_role(self, args, *rargs):
        id = args.get('id')
        if id is not None:
            arr = VocabAgentRelationshipRole.objects.get(pk=id)
            if arr:
                return arr
        return None

    def resolve_agent_relationship_roles(self, args, context, info):
        return VocabAgentRelationshipRole.objects.all()
