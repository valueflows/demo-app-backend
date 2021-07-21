#
# Graphene schema for exposing organisation Agent relationships
#
# @package: OCP
# @author:  pospi <pospi@spadgos.com>
# @since:   2017-06-05
#

import graphene
from graphene_django.types import DjangoObjectType
from valuenetwork.valueaccounting.models import EconomicAgent, AgentType
from valuenetwork.api.types.Agent import Organization
from valuenetwork.api.models import formatAgent, formatAgentList


# Visibility and Joining Style are from the OCP work app, and at this point include hard-codings for Freedom Coop

class JoiningStyle(graphene.Enum):
    NONE = None
    MODERATED = "moderated"
    AUTOJOIN = "autojoin"


class Visibility(graphene.Enum):
    NONE = None
    PRIVATE = "private"
    FCMEMBERS = "only FC members"
    PUBLIC = "public"


class OrganizationType(DjangoObjectType):

    class Meta:
        model = AgentType
        only_fields = ('id', 'name')


class Query(graphene.AbstractType):

    # define input query params

    organization = graphene.Field(Organization,
                                  id=graphene.Int())

    all_organizations = graphene.List(Organization)

    fc_organizations = graphene.List(Organization,
                                     joining_style=graphene.String(),
                                     visibility=graphene.String())

    # load any organisation

    def resolve_organization(self, args, context, info):
        id = args.get('id')
        if id is not None:
            org = EconomicAgent.objects.get(pk=id)
            if org:
                if org.agent_type.party_type == "individual":
                    return None
                else:
                    return formatAgent(org)
        return None

    # load all organizations

    def resolve_all_organizations(self, args, context, info):
        return formatAgentList(EconomicAgent.objects.exclude(agent_type__party_type="individual"))

    #types of organization

    organization_types = graphene.List(OrganizationType)

    def resolve_organization_types(self, args, context, info):
        return AgentType.objects.exclude(party_type="individual")
