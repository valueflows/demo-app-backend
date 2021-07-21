#
# Graphene schema for exposing individual agent query endpoints ("Person" in VF terms)
#

import graphene
from valuenetwork.valueaccounting.models import VocabAgent
from valuenetwork.api.types.Agent import Person
from valuenetwork.api.models import formatAgent, formatAgentList

class Query(graphene.AbstractType):

    person = graphene.Field(Person,
                           id=graphene.Int())

    people = graphene.List(Person)


    def resolve_person(self, args, context, info):
        id = args.get('id')
        if id is not None:
            person = VocabAgent.objects.get(pk=id)
            if person:
                if person.agent_subclass == "Person":
                    return formatAgent(person)
        return None

    # load all people

    def resolve_people(self, args, context, info):
        people = VocabAgent.objects.filter(agent_subclass="Person")
        return formatAgentList(people)

