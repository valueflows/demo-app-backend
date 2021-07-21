#
# Graphene schema for exposing Process model
#
#

import graphene
import datetime
from valuenetwork.valueaccounting.models import VocabProcess, VocabAgent, VocabPlan #, AgentUser, Order
from valuenetwork.api.types.Process import Process
from six import with_metaclass
from django.contrib.auth.models import User
from .Auth import AuthedInputMeta, AuthedMutation
from django.core.exceptions import PermissionDenied


class Query(graphene.AbstractType):

    # define input query params

    process = graphene.Field(Process,
                            id=graphene.Int())

    processes = graphene.List(Process)

    # load single item

    def resolve_process(self, args, *rargs):
        id = args.get('id')
        if id is not None:
            process = VocabProcess.objects.get(pk=id)
            if process:
                return process
        return None

    # load all items

    def resolve_processes(self, args, context, info):
        return VocabProcess.objects.all()


class CreateProcess(AuthedMutation):
    class Input(with_metaclass(AuthedInputMeta)):
        name = graphene.String(required=True)
        has_beginning = graphene.String(required=False)
        has_end = graphene.String(required=False)
        scope_id = graphene.Int(required=False)
        note = graphene.String(required=False)
        plan_id = graphene.Int(required=False)
        finished = graphene.Boolean(required=False)
        classifed_as= graphene.String(required=False)

    process = graphene.Field(lambda: Process)

    @classmethod
    def mutate(cls, root, args, context, info):
        name = args.get('name')
        has_beginning = args.get('has_beginning', None)
        has_end = args.get('has_end', None)
        note = args.get('note')
        scope_id = args.get('scope_id')
        plan_id = args.get('plan_id')
        finished = args.get('finished')
        classified_as = args.get('classified_as')

        if not note:
            note = ""
        if has_beginning:
            has_beginning = datetime.datetime.strptime(has_beginning, '%Y-%m-%d').date()
        if has_end:
            has_end = datetime.datetime.strptime(has_end, '%Y-%m-%d').date()
        if scope_id:
            scope = VocabAgent.objects.get(pk=scope_id)
        else:
            scope = None
        plan = None
        if plan_id:
            plan = VocabPlan.objects.get(pk=plan_id)
        process = VocabProcess(
            name=name,
            has_beginning=has_beginning,
            has_end=has_end,
            note=note,
            in_scope_of=scope,
            plan=plan,
            finished=finished,
            classified_as=classified_as,
            #created_by=context.user,
        )

        #user_agent = AgentUser.objects.get(user=context.user).agent
        #is_authorized = user_agent.is_authorized(object_to_mutate=process)
        #if is_authorized:
        process.save()  
        #else:
        #    raise PermissionDenied('User not authorized to perform this action.')

        return CreateProcess(process=process)

"""
class UpdateProcess(AuthedMutation):
    class Input(with_metaclass(AuthedInputMeta)):
        id = graphene.Int(required=True)
        name = graphene.String(required=False)
        planned_start = graphene.String(required=False)
        planned_finish = graphene.String(required=False)
        scope_id = graphene.Int(required=False)
        note = graphene.String(required=False)
        is_finished = graphene.Boolean(required=False)
        plan_id = graphene.Int(required=False)

    process = graphene.Field(lambda: Process)

    @classmethod
    def mutate(cls, root, args, context, info):
        id = args.get('id')
        name = args.get('name')
        planned_start = args.get('planned_start')
        planned_finish = args.get('planned_finish')
        note = args.get('note')
        scope_id = args.get('scope_id')
        is_finished = args.get('is_finished')
        plan_id = args.get('plan_id')

        process = ProcessProxy.objects.get(pk=id)
        if process:
            if name:
                process.name = name
            if note:
                process.notes=note
            if planned_start:
                start_date = datetime.datetime.strptime(planned_start, '%Y-%m-%d').date()
                process.start_date=start_date
            if planned_finish:
                end_date = datetime.datetime.strptime(planned_finish, '%Y-%m-%d').date()
                process.end_date=end_date
            if scope_id:
                scope = EconomicAgent.objects.get(pk=scope_id)
                process.context_agent=scope
            if plan_id:
                plan = Order.objects.get(pk=plan_id)
                process.plan=plan
            if is_finished != None:
                process.finished=is_finished
            process.changed_by=context.user

            user_agent = AgentUser.objects.get(user=context.user).agent
            is_authorized = user_agent.is_authorized(object_to_mutate=process)
            if is_authorized:
                process.save_api()  
            else:
                raise PermissionDenied('User not authorized to perform this action.')


        return UpdateProcess(process=process)


class DeleteProcess(AuthedMutation):
    class Input(with_metaclass(AuthedInputMeta)):
        id = graphene.Int(required=True)

    process = graphene.Field(lambda: Process)

    @classmethod
    def mutate(cls, root, args, context, info):
        id = args.get('id')
        process = ProcessProxy.objects.get(pk=id)
        if process:
            if process.is_deletable():
                user_agent = AgentUser.objects.get(user=context.user).agent
                is_authorized = user_agent.is_authorized(object_to_mutate=process)
                if is_authorized:
                    process.delete() 
                else:
                    raise PermissionDenied('User not authorized to perform this action.')                
                #TODO: add logic for adjusting other processes if workflow plan
            else:
                raise PermissionDenied("Process has economic events so cannot be deleted.")

        return DeleteProcess(process=process)
"""
