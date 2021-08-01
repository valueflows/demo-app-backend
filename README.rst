Valueflows Demo App Backend
============================

This is a temporary hack to provide a backend that supports the Valueflows graphql api that groups immediately want for UI and other app work or experiments.  It is not meant to evolve into anything permanent!  It is based on old code, old unsupported libraries, and still has a huge amount of code not used for this effort sitting around in it.

Status
---------

In process.  Locally, there are working basic queries for all implemented types, including:

- Action, ResourceSpecification, AgentRelationshipRole
- Plan, Process, Commitment
- EconomicEvent, Fulfillment, EconomicResource, Agent, AgentRelationship

We installed this here http://vfdemo.pythonanywhere.com/.  We are working through problems specific to this environment, in place, so that version has deviated from this git version.  We will continue there for now.

API
------

This supports the VF graphql api.  Sample queries and mutations that will work are `here <https://lab.allmende.io/valueflows/vf-code-experiments/demo-app-backend/-/blob/master/valuenetwork/api/tests.py>`_.

Installation
------------

TBD soon.
