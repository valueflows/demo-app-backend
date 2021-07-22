#
# Agent Relationship: An ongoing voluntary association between 2 Agents of any kind.
#

import graphene
from graphene_django.types import DjangoObjectType
import valuenetwork.api.types as types
#from api.types.Agent import Agent
#from api.types.AgentRelationship import AgentRelationship, AgentRelationshipRole
from valuenetwork.valueaccounting.models import VocabAgentRelationship, VocabAgentRelationshipRole
from valuenetwork.api.models import formatAgent, Person, Organization


class RoleBehavior(graphene.Enum):
    NONE = None
    MEMBER = "member"
    PART = "part"
    PEER = "peer"
    TRADINGPARTNER = "trading partner"
    LEGALPARTNER = "legal partner"


class AgentRelationshipRole(DjangoObjectType):
    role_behavior = graphene.Field(lambda: RoleBehavior)

    class Meta:
        model = VocabAgentRelationshipRole
        only_fields = ('id', 'role_label', 'inverse_role_label')

    def resolve_role_behavior(self, args, *rargs):
        return self.role_behavior


class AgentRelationship(DjangoObjectType):
    subject = graphene.Field(lambda: types.Agent)
    object = graphene.Field(lambda: types.Agent)
    relationship = graphene.Field(AgentRelationshipRole)
    in_scope_of = graphene.Field(lambda: types.Agent)

    class Meta:
        model = VocabAgentRelationship
        only_fields = ('id')

    def resolve_subject(self, args, *rargs):
        return formatAgent(self.subject)

    def resolve_object(self, args, *rargs):
        return formatAgent(self.object)

    def resolve_relationship(self, args, *rargs):
        return self.relationship
        
    def resolve_in_scope_of(self, args, *rargs):
        return formatAgent(self.in_scope_of)

