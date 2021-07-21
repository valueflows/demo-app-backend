
######################### SAMPLE QUERIES #####################

'''
# get token for graphiql

mutation {
    createToken(username: "testUser11222", password: "123456") {
        token
    }
}

query($token: String) {
  viewer(token: $token) {
    action(label: "produce") {
      id
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    actions {
      id
      label
      note
      resourceEffect
      onhandEffect
      inputOutput
      pairsWith
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    action (id: 3) {
      id
      label
      note
      resourceEffect
      onhandEffect
      inputOutput
      pairsWith
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    agent(id:1) {
      id
      name
      image
      note
      __typename
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    agentRelationshipRoles {
      id
      roleLabel
      inverseRoleLabel
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    agentRelationshipRole (id: 1) {
      id
      roleLabel
      inverseRoleLabel
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    units {
      id
      label
      symbol
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    unit (id:8) {
      id
      label
      symbol
    }
  }
}

# this would probably never be queried by itself in an app
query($token: String) {
  viewer(token: $token) {
    measure (id: 1){
      id
      hasNumericalValue
      hasUnit {
        label
        symbol
      }
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    economicResources {
      id
      name
      trackingIdentifier
      accountingQuantity {
        hasNumericalValue
        hasUnit {
          label
        }
      }
      onhandQuantity {
        hasNumericalValue
        hasUnit {
          label
        }
      }
      classifiedAs
      conformsTo {
        name
      }
      image
      note
      unitOfEffort {
        label
      }
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    economicResource (id: 13) {
      id
      name
      trackingIdentifier
      accountingQuantity {
        hasNumericalValue
        unit {
          label
        }
      }
      onhandQuantity {
        hasNumericalValue
        unit {
          label
        }
      }
      classifiedAs
      conformsTo {
        name
      }
      image
      note
      unitOfEffort {
        label
      }
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    processes {
      id
      name
      hasBeginning
      hasEnd
      finished
      note
      nestedIn {
        name
      }
      inScopeOf {
        name
      }
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    process (id: 1) {
      id
      name
      hasBeginning
      hasEnd
      finished
      note
    }
  }
}

mutation ($token: String!) {
  createProcess(token: $token, name: "Create big doc", hasBeginning: "2017-10-01", 
    hasEnd: "2017-10-10", note: "testing", finished: false, planId: ) {
    process {
      id
      name
      hasBeginning
      hasEnd
      finished
      note
      }
    }
  }
  
query($token: String) {
  viewer(token: $token) {
    resourceSpecifications {
      id
      name
      image
      resourceClassifiedAs
      defaultUnitOfResource {
        label
      }
      defaultUnitOfEffort {
        label
      }
      note
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    resourceSpecification (id: 1) {
      id
      name
      image
      resourceClassifiedAs
      defaultUnitOfResource {
        label
      }
      defaultUnitOfEffort {
        label
      }
      note
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    plans {
      id
      name
      due
      note
      processes {
        name
      }
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    plan (id: 1) {
      id
      name
      due
      note
    }
  }
}


###################################################################
##################################################################3
# OLD   OLD    OLD    OLD    OLD    OLD    OLD    OLD    OLD    OLD  
###################################################################
              
# agent data

# user agent is authorized to create objects within that scope
query($token: String) {
  viewer(token: $token) {
    userIsAuthorizedToCreate(scopeId:23) 
  }
}

query($token: String) {
  viewer(token: $token) {
    agent(id:39) {
      id
      name
      image
      note
      type
      validatedEventsCount(month:12, year:2017)
      eventsCount(month:12, year:2017)
      eventHoursCount(month:12, year:2017)
      eventPeopleCount(month:12, year:2017)
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    allAgents {
      id
      name
      image
      primaryLocation {
        name
        address
      }
      note
      type
      __typename
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    person(id:6) {
      id
      name
      image
      note
      type
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    myAgent {
      id
      agentSkillRelationships {
        id
        resourceClassification {
          name
        }
      }
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    allPeople {
      id
      name
      image
      note
      type
      __typename
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    organization(id:26) {
      id
      name
      image
      note
      type
      __typename
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    allOrganizations {
      id
      name
      image
      note
      type
      __typename
      agentRecipes {
        name
      }
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    fcOrganizations (visibility:"public", joiningStyle:"moderated") {
      id
      name
      image
      type
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    emailExists(email:"xxx@gmail.com")
  }
}

query($token: String) {
  viewer(token: $token) {
    usernameExists(username:"lynn")
  }
}

query($token: String) {
  viewer(token: $token) {
    createInactiveUser(username:"lynn-xfxzz", email:"qxaw@gmail.com", pswd:"xxdd")
  }
}

query($token: String) {
  viewer(token: $token) {
    activateUserCreatePerson(username:"lynn-xfxzz", 
      userToken:"51s-10ed8117b79f4863e46b", 
      name:"Lynn F", image:"http://images.example.com/jdskdsf", phone:"555-3434")
  }
}

query($token: String) {
  viewer(token: $token) {
    createUserPerson(username:"lynn-xfqxxzzs", email:"qxsxqaw@gmail.com", pswd:"xxdd",
    name:"Lynn Test", image:"http://xxx.image.com", phone:"608-555-1212" )
  }
}

query($token: String) {
  viewer(token: $token) {
    organizationClassification(id:8) {
      id
      name
      note
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    allOrganizationClassifications {
      id
      name
      note
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    person(id:6) {
      name
      commitmentsMatchingSkills(page:1) {
        id
        action
        resourceClassifiedAs {
          name
        }
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    agent(id: 39) {
      name
      agentPlans(month:12, year: 2017) {
        name
        planProcesses(month:12, year: 2017) {
          name
          committedInputs(action: WORK) {
            note
            fulfilledBy(requestDistribution: true) {
              fulfilledBy {
                provider {
                  name
                }
                requestDistribution
                note
                isValidated
              }
            }
          }
        }
      }
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    agent(id:106) {
      name
      searchAgentCommitments(searchString:"Fruit") {
        id
        note
      }
      searchAgentPlans(searchString:"Fruit", isFinished: false) {
        id
        name
        note
      }
      searchAgentProcesses(searchString:"fruit") {
        id
        name
        note
      }
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    organizationTypes {
      name
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    allAgentRelationshipRoles {
      id
      label
      inverseLabel
      category
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    agentRelationship(id:20) {
      subject {
        name
        type
      }
      relationship {
        label
        category
      }
      object {
        name
        type
      }
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    allAgentRelationships {
      id
      subject {
        name
        type
      }
      relationship {
        label
        category
      }
      object {
        name
        type
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    agent(id: 39) {
      name
      agentRelationships {
        id
        subject {
          name
          type
        }
        relationship {
          label
          category
        }
        object {
          name
          type
        }
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    agent(id: 39) {
      name
      agentRelationships(category: MEMBER) {
        id
        subject {
          name
          type
        }
        relationship {
          label
          category
        }
        object {
          name
          type
        }
      }
    }
  }
}

#also ...asSubject works
query ($token: String) {
  viewer(token: $token) {
    agent(id: 39) {
      name
      agentRelationshipsAsObject {
        id
        subject {
          name
          type
        }
        relationship {
          label
          category
        }
        object {
          name
          type
        }
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    agent(id: 6) {
      name
      memberRelationships {
        id
        subject {
          name
          type
        }
        relationship {
          label
          category
        }
        object {
          name
          type
        }
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    agent(id: 7) {
      name
      agentRelationships(category: MEMBER) {
        id
        subject {
          name
          type
          ownedEconomicResources (resourceClassificationId: 28) {
            createdDate
            resourceClassifiedAs {
              name
            }
            currentQuantity {
              numericValue
              unit {
                name
              }
            }
          }
        }
        relationship {
          label
          category
        }
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    agent(id: 39) {
      name
      agentRelationships(roleId: 2) {
        id
        subject {
          name
          type
        }
        relationship {
          label
          category
        }
        object {
          name
          type
        }
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    agent(id: 39) {
      name
      agentRoles {
        label
        category
      }
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    myAgent {
      id
      name
      image
      note
      type
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    agent(id:39) {
      id
      name
      image
      note
      type
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    allAgents {
      id
      name
      image
      note
      email
      type
      __typename
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    person(id:6) {
      id
      name
      image
      note
      type
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    allPeople {
      id
      name
      image
      note
      type
      __typename
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    organization(id:26) {
      id
      name
      image
      note
      type
      __typename
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    allOrganizations {
      id
      name
      image
      note
      type
      __typename
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    allAgentRelationshipRoles {
      id
      label
      inverseLabel
      category
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    agentRelationship(id:20) {
      subject {
        name
        type
      }
      relationship {
        label
        category
      }
      object {
        name
        type
      }
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    allAgentRelationships {
      id
      subject {
        name
        type
      }
      relationship {
        label
        category
      }
      object {
        name
        type
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    agent(id: 39) {
      name
      agentRelationships {
        id
        subject {
          name
          type
        }
        relationship {
          label
          category
        }
        object {
          name
          type
        }
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    agent(id: 39) {
      name
      agentRelationships(category: MEMBER) {
        id
        subject {
          name
          type
        }
        relationship {
          label
          category
        }
        object {
          name
          type
        }
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    agent(id: 39) {
      name
      agentRelationships(roleId: 2) {
        id
        subject {
          name
          type
        }
        relationship {
          label
          category
        }
        object {
          name
          type
        }
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    agent(id: 39) {
      name
      agentRoles {
        label
        category
      }
    }
  }
}

# notification data

query ($token: String) {
  viewer(token: $token) {
    allNotificationTypes {
      id
      label
      display
      description
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    notificationSetting(id: 2) {
      id
      agent {
        name
      }
      send
      notificationType {
        id
        label
        display
        description
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    allNotificationSettings {
      id
      agent {
        name
      }
      send
      notificationType {
        label
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    agent(id: 6) {
      name
      agentNotificationSettings {
        id
        agent {
          name
        }
        send
        notificationType {
          id
          label
        }
      }
    }
  }
}

# unit data

query($token: String) {
  viewer(token: $token) {
    unit(id:8) {
      id
      name
      symbol
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    allUnits {
      id
      name
      symbol
    }
  }
}

# resource data

query($token: String) {
  viewer(token: $token) {
    resourceClassification(id:38) {
      id
      name
      image
      category
      note
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    allResourceClassifications {
      id
      name
      unit {
        id
        name
        symbol
      }
      image
      category
      processCategory
      note
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    agent(id: 146) {
      agentDefinedResourceClassifications(action: "work") {
        id
        name
      }
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    allRecipes {
      id
      name
      image
      category
      processCategory
      note
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    resourceClassification(id: 31) {
      name
      classificationResources {
        trackingIdentifier
        currentQuantity {
          numericValue
          unit {
            name
          }
        }
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    resourceClassificationsByProcessCategory(category: CONSUMED) {
      name
      category
      processCategory
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    resourceClassificationsByFacetValues(facetValues: "Material: Product,Material: Raw material,Non-material: Digital,Non-material: Formation") {
      id
      name
      classificationResources {
        id
        trackingIdentifier
        currentQuantity {
          numericValue
          unit {
            name
          }
        }
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    resourceClassificationsByAction(action: PRODUCE) {
      name
      category
      processCategory
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    allFacets {
      id
      name
      description
      facetValues {
        value
        description
      }
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    economicResource(id: 157) {
      id
      resourceClassifiedAs {
        name
        category
      }
      trackingIdentifier
      currentQuantity {
        numericValue
        unit {
          name
        }
      }
      image
      category
      url
      note
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    allEconomicResources {
      id
      resourceClassifiedAs {
        name
        category
      }
      trackingIdentifier
      currentQuantity {
        numericValue
        unit {
          name
        }
      }
      currentLocation {
        name
        address
      }
      image
      note
      resourceContacts {
        name
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    agent(id: 26) {
      name
      ownedEconomicResources {
        id
        resourceClassifiedAs {
          name
          category
        }
        trackingIdentifier
        currentQuantity {
          numericValue
          unit {
            name
          }
        }
        image
        note
        category
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    agent (id:39) {
      name
      ownedEconomicResources(page:1) {
        createdDate
        resourceClassifiedAs {
          name
        }
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    agent (id:39) {
      name
      ownedEconomicResources(category: INVENTORY) {
        owners {
          name
        }
        resourceClassifiedAs {
          name
        }
      }
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    agent(id:106) {
      searchOwnedInventoryResources(searchString: "jam Jars lids") {
        id
        note
        resourceClassifiedAs {
          name
          note
        }
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    agent(id: 6) {
      name
      ownedEconomicResources(category: CURRENCY) {
        id
        resourceClassifiedAs {
          name
          category
        }
        trackingIdentifier
        currentQuantity {
          numericValue
          unit {
            name
          }
        }
        image
        note
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    agent(id: 26) {
      name
      ownedEconomicResources(category: INVENTORY) {
        id
        resourceClassifiedAs {
          name
          category
        }
        trackingIdentifier
        currentQuantity {
          numericValue
          unit {
            name
          }
        }
        image
        note
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    economicResource(id: 20) {
      id
      resourceClassifiedAs {
        name
        category
      }
      trackingIdentifier
      currentQuantity {
        numericValue
        unit {
          name
        }
      }
      transfers {
        id
        transferDate
        provider {
          name
        }
        receiver {
          name
        }
        resourceClassifiedAs {
          name
        }
        giveResource {
          trackingIdentifier
        }
        takeResource {
          trackingIdentifier
        }
        transferQuantity {
          numericValue
          unit {
            name
          }
        }
      }
    }
  }
}

# kispagi
# old
query($token: String) {
  viewer(token: $token) { agent(id:""" + str(project_id) + """) { name
      agentProcesses {
        name id  plannedStart plannedDuration
        unplannedEconomicEvents { id note }
        committedInputs { note id fulfilledBy { fulfilledBy { id }}}
        inputs {
          id start
          provider {id name faircoinAddress} action note requestDistribution
          affectedQuantity{ numericValue unit {name}} note
          validations { id validationDate validatedBy { id name } }
        }
        processClassifiedAs {name} plannedDuration isFinished note
      }
    }
  }
}

#new suggested
query ($token: String) {
  viewer(token: $token) {
    agent(id: 39) {
      id
      name
      agentEconomicEvents(action: "work", year: 2017, month: 9) {
        id
        start
        requestDistribution
        affectedQuantity {
          numericValue
          unit {
            name
          }
        }
        affects {
          resourceClassifiedAs {
            name
            category
          }
          trackingIdentifier
        }
        provider {
          id
          name
          faircoinAddress
        }
        note
        inputOf {
          id
          name
<<<<<<< HEAD
=======
          processPlan {
            id
          }
>>>>>>> a139cbfad931e5b4bd274df6524ccca95b6a3387
        }
        validations {
          id
          validationDate
          validatedBy {
            id
            name
          }
        }
      }
    }
  }
}

# process data

query($token: String) {
  viewer(token: $token) {
    process(id:51) {
      id
      name
      scope {
        name
      }
      processPlan {
        name
        due
      }
      plannedStart
      plannedDuration
      isFinished
      note
      userIsAuthorizedToUpdate
      userIsAuthorizedToDelete
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    allProcesses {
      id
      name
      scope {
        name
      }
      processClassifiedAs {
        name
      }
      plannedStart
      plannedDuration
      isFinished
      note
      isDeletable
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    processClassification (id: 3) {
      id
      name
      scope {
        name
      }
      estimatedDuration
      note
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    allProcessClassifications {
      id
      name
      scope {
        name
      }
      estimatedDuration
      note
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    agent(id:26) {
      name
      agentProcesses {
        id
        name
        plannedStart
        plannedDuration
        isFinished
        note
      }
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    agent(id:39) {
      name
      agentPlans (isFinished: false) {
        id
        name
        due
        note
      }
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    agent(id:26) {
      name
      agentProcesses (isFinished: false) {
        id
        name
        plannedStart
        plannedFinish
        plannedDuration
        isFinished
        note
      }
    }
  }
}

fragment coreEventFields on EconomicEvent {
  action
  start
  affectedQuantity {
    numericValue
    unit {
      name
    }
  }
  affects {
    resourceClassifiedAs {
      name
      category
    }
    trackingIdentifier
  }
  provider {
    id
    name
  }
  receiver {
    id
    name
  }
}
fragment coreCommitmentFields on Commitment {
  action
  plannedStart
  committedOn
  due
  committedQuantity {
    numericValue
    unit {
      name
    }
  }
  resourceClassifiedAs {
    name
    category
  }
  provider {
    id
    name
  }
  receiver {
    id
    name
  }
}
query ($token: String) {
  viewer(token: $token) {
    process(id: 6) {
      name
      unplannedEconomicEvents(action: WORK) {
        ...coreEventFields
      }
      inputs (action: WORK) {
        ...coreEventFields
      }
      outputs {
        ...coreEventFields
      }
      committedInputs {
        ...coreCommitmentFields
      }
      committedOutputs (action: PRODUCE) {
        ...coreCommitmentFields
      }
      nextProcesses {
        name
      }
      previousProcesses {
        name
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    process(id: 52) {
      name
      isStarted
      isFinished
      workingAgents {
        name
        image
        __typename
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    plan(id: 50) {
      name
      scope {
        name
      }
      plannedOn
      due
      note
      planProcesses {
        name
      }
      workingAgents {
        name
        __typename
      }
      kanbanState
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    allPlans {
      name
      planProcesses {
        name
      }
      isDeletable
      createdBy {
        name
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    allPlans {
      id
      name
      plannedNonWorkInputs {
        action
        resourceClassifiedAs {
          name
        }
        committedQuantity {
          numericValue
          unit {
            name
          }
        }
      }
      plannedOutputs {
        action
        resourceClassifiedAs {
          name
        }
        committedQuantity {
          numericValue
          unit {
            name
          }
        }
      }
      nonWorkInputs {
        action
        affects {
          trackingIdentifier
          resourceClassifiedAs {
            name
          }
        }
        affectedQuantity {
          numericValue
          unit {
            name
          }
        }
      }
      outputs {
        action
        affects {
          trackingIdentifier
          resourceClassifiedAs {
            name
          }
        }
        affectedQuantity {
          numericValue
          unit {
            name
          }
        }
      }
    }
  }
}

# event data

query ($token: String) {
  viewer(token: $token) {
    allEconomicEvents {
      id
      action
      start
      affectedQuantity {
        numericValue
        unit {
          name
        }
      }
      note
      url
      affects {
        resourceClassifiedAs {
          name
          category
        }
        trackingIdentifier
      }
      provider {
        id
        name
      }
      receiver {
        id
        name
      }
      inputOf {
        id
        name
      }
      outputOf {
        id
        name
      }
      scope {
        id
        name
      }
      fulfills {
        fulfilledQuantity {
          numericValue
          unit {
            name
          }
        }
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    filteredEconomicEvents (action: "give", resourceClassifiedAsId: 28, startDate: "2017-01-01", endDate: "2017-04-27", receiverId: 56, providerId: 26) {
      id
      action
      start
      affects {
        resourceClassifiedAs {
          id
          name
          category
        }
      }
      provider {
        id
        name
      }
      receiver {
        id
        name
      }
      scope {
        id
        name
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    agent(id: 6) {
      name
      agentEconomicEvents(latestNumberOfDays: 30, requestDistribution: true) {
        id
        action
        start
        requestDistribution
        affectedQuantity {
          numericValue
          unit {
            name
          }
        }
        affects {
          resourceClassifiedAs {
            name
            category
          }
          trackingIdentifier
        }
        provider {
          id
          name
        }
        receiver {
          id
          name
        }
        note
      }
      agentCommitments(page:1) {
        id
        action
        plannedStart
        committedOn
        due
        committedQuantity {
          numericValue
          unit {
            name
          }
        }
        resourceClassifiedAs {
          name
          category
        }
        provider {
          id
          name
        }
        receiver {
          id
          name
        }
        note
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    economicEvent(id: 296) {
      id
      action
      start
      affectedQuantity {
        numericValue
        unit {
          name
        }
      }
      note
      affects {
        resourceClassifiedAs {
          name
          category
        }
        trackingIdentifier
      }
      provider {
        id
        name
      }
      receiver {
        id
        name
      }
      scope {
        id
        name
      }
      userIsAuthorizedToUpdate
      userIsAuthorizedToDelete
      validations {
        id
        validationDate
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    economicEvent(id: 316) {
      id
      action
      start
      affectedQuantity {
        numericValue
        unit {
          name
        }
      }
      note
      affects {
        resourceClassifedAs {
          name
          category
        }
        trackingIdentifier
      }
      provider {
        id
        name
      }
      receiver {
        id
        name
      }
      inputOf {
        name
      }
      outputOf {
        name
      }
      scope {
        id
        name
      }
      fulfills {
        fulfills {
          id
          committedQuantity {
            numericValue
            unit {
              name
            }
          }
        }
        fulfilledQuantity {
          numericValue
          unit {
            name
          }
        }
      }
    }
  }
}

# validation data

query($token: String) {
  viewer(token: $token) {
    validation(id:5) {
      id
      validatedBy {
        name
      }
      economicEvent {
        action
      }
      validationDate
    }
  }
}

query($token: String) {
  viewer(token: $token) {
    allValidations {
      id
      validatedBy {
        name
      }
      economicEvent {
        action
      }
      validationDate
    }
  }
}

# commitment data

query ($token: String) {
  viewer(token: $token) {
    allCommitments {
      id
      action
      plannedStart
      committedOn
      due
      committedQuantity {
        numericValue
        unit {
          name
        }
      }
      note
      resourceClassifiedAs {
        name
        category
      }
      involves {
        id
        resourceClassifiedAs {
          name
          category
        }
        trackingIdentifier
      }
      provider {
        id
        name
      }
      receiver {
        id
        name
      }
      inputOf {
        id
        name
      }
      outputOf {
        id
        name
      }
      scope {
        id
        name
      }
      plan {
        id
        name
      }
      isPlanDeliverable
      forPlanDeliverable {
        id
        action
        outputOf {
          name
        }
      }
      isDeletable
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    commitment(id: 325) {
      id
      action
      plannedStart
      committedOn
      due
      committedQuantity {
        numericValue
        unit {
          name
        }
      }
      note
      resourceClassifiedAs {
        name
        category
      }
      involves {
        id
        resourceClassifiedAs {
          name
          category
        }
        trackingIdentifier
      }
      provider {
        id
        name
      }
      receiver {
        id
        name
      }
      inputOf {
        id
        name
      }
      outputOf {
        id
        name
      }
      scope {
        id
        name
      }
      plan {
        name
      }
      fulfilledBy (requestDistribution: false) {
        fulfilledBy {
          action
          start
          requestDistribution
          provider {
            name
          }
        }
        fulfilledQuantity {
          numericValue
          unit {
            name
          }
        }
      }
      involvedAgents {
        name
      }
      userIsAuthorizedToUpdate
      userIsAuthorizedToDelete
      isDeletable
    }
  }
}

# exchange data

query ($token: String) {
  viewer(token: $token) {
    exchangeAgreement(id: 94) {
      plannedStart
      scope {
        name
      }
      exchangeAgreement {
        name
      }
      note
      transfers {
        name
        provider {
          name
        }
        receiver {
          name
        }
        transferQuantity {
          numericValue
          unit {
            name
          }
        }
      }
      involvedAgents {
        name
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    transfer(id: 160) {
      name
      plannedStart
      scope {
        name
      }
      exchangeAgreement {
        name
      }
      note
      provider {
        name
      }
      receiver {
        name
      }
      transferQuantity {
        numericValue
        unit {
          name
        }
      }
      transferEconomicEvents {
        action
      }
      transferCommitments {
        action
      }
      giveCommitment {
        action
      }
      takeCommitment {
        action
      }
      involvedAgents {
        name
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    transfer(id: 76) {
      name
      plannedStart
      scope {
        name
      }
      note
      provider {
        name
      }
      receiver {
        name
      }
      resourceClassifiedAs {
        name
      }
      giveResource {
        trackingIdentifier
      }
      takeResource {
        trackingIdentifier
      }
      transferQuantity {
        numericValue
        unit {
          name
        }
      }
      transferEconomicEvents {
        action
      }
      giveEconomicEvent {
        action
      }
      takeEconomicEvent {
        action
      }
      transferCommitments {
        action
      }
      involvedAgents {
        name
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    transfer(id: 82) {
      name
      exchangeAgreement {
        plannedStart
      }
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    place(id: 4) {
      id
      name
      address
      latitude
      longitude
      note
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    place(address: "Anacortes, WA 98221") {
      id
      name
      address
      latitude
      longitude
      note
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    allPlaces {
      id
      name
      address
      latitude
      longitude
      note
    }
  }
}

query ($token: String) {
  viewer(token: $token) {
    place(id: 5) {
      placeAgents {
        name
      }
      placeResources {
        trackingIdentifier
        resourceClassifiedAs {
          name
        }
      }
    }
  }
}


######################### SAMPLE MUTATIONS ###########################

mutation ($token: String!) {
  createProcess(token: $token, name: "Test planned finish", plannedStart: "2017-10-01", 
    plannedFinish: "2017-10-10", scopeId: 39, note: "testing", planId: 62) {
    process {
      id
      name
      plannedStart
      plannedFinish
      processPlan {
        name
      }
    }
  }
}

mutation ($token: String!) {
  updateProcess(token: $token, id: 85, 
    plannedFinish: "2017-10-12", isFinished: true, planId: 62) {
    process {
      name
      isFinished
      plannedFinish
      plannedDuration
      processPlan {
        id
        name
      }
    }
  }
}

mutation ($token: String!) {
  deleteProcess(token: $token, id: 38) {
    process {
      name
    }
  }
}

mutation ($token: String!) {  
  createCommitment(token: $token, action: "use", plannedStart: "2018-10-01", due: "2018-10-10",
    scopeId: 39, note: "testing", committedResourceClassifiedAsId: 17, involvesId: 11, 
    committedNumericValue: "3.5", committedUnitId: 2, inputOfId: 6, planId: 52,
    providerId: 79, receiverId: 39, url: "http://www.test.coop") {
    commitment {
      id
      action
      plannedStart
      due
      url
      inputOf {
        name
      }
      outputOf {
        name
      }
      provider {
        name
      }
      receiver {
        name
      }
      scope {
        name
      }
      resourceClassifiedAs {
        name
      }
      involves {
        trackingIdentifier
      }
      committedQuantity {
        numericValue
        unit {
          name
        }
      }
      committedOn
      isFinished
      note
    }
  }
}

mutation ($token: String!) {
  updateCommitment(token: $token, plannedStart: "2017-10-03", due: "2017-10-12",
    note: "testing more", committedNumericValue: "5.5", isFinished: true, id: 440, url: "http://www.testagain.coop") {
    commitment {
      id
      action
      plannedStart
      due
      url
      inputOf {
        name
      }
      outputOf {
        name
      }
      provider {
        name
      }
      receiver {
        name
      }
      scope {
        name
      }
      resourceClassifiedAs {
        name
      }
      involves {
        trackingIdentifier
      }
      committedQuantity {
        numericValue
        unit {
          name
        }
      }
      committedOn
      isFinished
      note
    }
  }
}

mutation ($token: String!) {
  deleteCommitment(token: $token, id: 11) {
    commitment {
      action
    }
  }
}

mutation ($token: String!) {
  createPlan(token: $token, name: "Fudge!", due: "2017-10-15", note: "testing") {
    plan {
      id
      name
      due
      note
    }
  }
}

mutation ($token: String!) {
  createPlanFromRecipe(token: $token, name: "More Jam!", due: "2018-06-20", 
    producesResourceClassificationId: 37, note: "test") {
    plan {
      id
      name
      due
      note
      planProcesses {
        name
      }
    }
  }
}

mutation ($token: String!) {
  updatePlan(token: $token, id:53, name: "Fudge!", due: "2017-10-16", note: "testing more") {
    plan {
      id
      name
      due
      note
    }
  }
}

mutation ($token: String!) {
  deletePlan(token: $token, id: 53) {
    plan {
      name
    }
  }
}

mutation ($token: String!) {
  createEconomicEvent(token: $token, action: "use", start: "2017-10-01", scopeId: 39, 
    note: "testing", affectedResourceClassifiedAsId: 17, affectsId: 11, affectedNumericValue: "3.5", 
    affectedUnitId: 2, inputOfId: 62, providerId: 79, receiverId: 39, url: "hi.com") {
    economicEvent {
      id
      action
      start
      inputOf {
        name
      }
      outputOf {
        name
      }
      provider {
        name
      }
      receiver {
        name
      }
      scope {
        name
      }
      affects {
        trackingIdentifier
        resourceClassifiedAs {
          name
        }
      }
      affectedQuantity {
        numericValue
        unit {
          name
        }
      }
      note
      url
    }
  }
}

#creates a resource also
mutation ($token: String!) {
  createEconomicEvent(token: $token, action: "produce", start: "2017-10-07", scopeId: 39, 
    note: "testing new resource", affectedResourceClassifiedAsId: 37, affectedNumericValue: "30", 
    affectedUnitId: 4, outputOfId: 67, providerId: 39, receiverId: 39, createResource: true,
    resourceNote: "new one", resourceImage: "rrr.com/image", resourceTrackingIdentifier: "test-url",
    resourceUrl: "resource.com") {
    economicEvent {
      id
      action
      start
      inputOf {
        name
      }
      outputOf {
        name
      }
      provider {
        name
      }
      receiver {
        name
      }
      scope {
        name
      }
      affects {
        id
        trackingIdentifier
        resourceClassifiedAs {
          name
        }
        currentQuantity {
          numericValue
        }
        note
      }
      affectedQuantity {
        numericValue
        unit {
          name
        }
      }
      note
      url
    }
  }
}

mutation ($token: String!) {
  createEconomicEvent(token: $token, action: "work", start: "2017-10-01", scopeId: 39, 
    note: "testing no provider", affectedNumericValue: "5", affectedResourceClassifiedAsId: 61,
    inputOfId: 65, affectedUnitId: 2, requestDistribution: true) {
    economicEvent {
      id
      action
      start
      inputOf {
        name
      }
      outputOf {
        name
      }
      provider {
        name
      }
      receiver {
        name
      }
      scope {
        name
      }
      affects {
        trackingIdentifier
        resourceClassifiedAs {
          name
        }
        note
      }
      affectedQuantity {
        numericValue
        unit {
          name
        }
      }
      note
      url
      requestDistribution
    }
  }
}

#create a resource with an event
mutation ($token: String!) {
  createEconomicEvent(token: $token, action: "take", start: "2017-12-01", 
    scopeId: 39, note: "creating a resource", affectedNumericValue: "5", 
    affectedResourceClassifiedAsId: 38, affectedUnitId: 4, resourceCurrentLocationId: 7, 
    resourceTrackingIdentifier: "lynn-test-1234", createResource: true) {
    economicEvent {
      id
      action
      start
      inputOf {
        name
      }
      outputOf {
        name
      }
      provider {
        name
      }
      receiver {
        name
      }
      scope {
        name
      }
      affects {
        trackingIdentifier
        resourceClassifiedAs {
          name
        }
        currentLocation {
          name
        }
      }
      affectedQuantity {
        numericValue
        unit {
          name
        }
      }
      note
      url
    }
  }
}

mutation ($token: String!) {
  updateEconomicEvent(token: $token, id: 350, start: "2017-10-02", scopeId: 39, 
    note: "testing more", affectedResourceClassifiedAsId: 17, affectsId: 11, 
    affectedNumericValue: "4.5", affectedUnitId: 2, inputOfId: 62, providerId: 79, receiverId: 39) {
    economicEvent {
      id
      action
      start
      inputOf {
        name
      }
      outputOf {
        name
      }
      provider {
        name
      }
      receiver {
        name
      }
      scope {
        name
      }
      affects {
        trackingIdentifier
        resourceClassifiedAs {
          name
        }
      }
      affectedQuantity {
        numericValue
        unit {
          name
        }
      }
      note
    }
  }
}

mutation ($token: String!) {
  deleteEconomicEvent(token: $token, id: 350) {
    economicEvent {
      action
      start
    }
  }
}

mutation ($token: String!) {
  updateEconomicResource(token: $token, id: 128, trackingIdentifier: "xxxccc333", 
    note: "testing url", resourceClassifiedAsId: 37, image: "xxx.com", url: "rrr.com") {
    economicResource {
      id
      trackingIdentifier
      resourceClassifiedAs {
        name
      }
      currentQuantity {
        numericValue
        unit {
          name
        }
      }
      note
      image
      url
      currentLocation {
        id
      }
    }
  }
}

mutation ($token: String!) {
  deleteEconomicResource(token: $token, id: 34) {
    economicResource {
      trackingIdentifier
    }
  }
}

mutation ($token: String!) {
  updatePerson(token: $token, id: 74, note: "test", name: "test agent", primaryLocationId: 24,
  image: "https://testocp.freedomcoop.eu/site_media/media/photos/what_is_it.JPG") {
    person {
      id
      name
      note
      image
      primaryLocation {
        name
      }
    }
  }
}

mutation ($token: String!) {
  createOrganization(token: $token, type: "Organization", name: "test org 2") {
    organization {
      id
      name
      note
      image
      type
      primaryLocation {
        name
      }
      primaryPhone
    }
  }
}

mutation ($token: String!) {
  createPerson(token: $token, name: "anne person", note:"test", type: "Individual", primaryLocationId: 24, 
    image: "https://testocp.freedomcoop.eu/site_media/media/photos/what_is_it.JPG", primaryPhone: "333-444-5555" ) {
    person {
      id
      name
      note
      image
      type
      primaryLocation {
        name
      }
      primaryPhone
    }
  }
}

mutation ($token: String!) {
  deletePerson(token: $token, id: 39) {
    person {
      id
      name
    }
  }
}

mutation ($token: String!) {
  deleteOrganization(token: $token, id: 142) {
    organization {
      id
      name
    }
  }
}

mutation ($token: String!) {
  createNotificationSetting(token: $token, notificationTypeId: 1, agentId: 107, send: true) {
    notificationSetting {
      id
      notificationType {
        display
      }
      send
      agent {
        name
      }
    }
  }
}

mutation ($token: String!) {
  updateNotificationSetting (token: $token, id: 137, send: true) {
    notificationSetting {
      id
      notificationType {
        display
      }
      send
      agent {
        name
      }
    }
  }
}

mutation ($token: String!) {
<<<<<<< HEAD
  createValidation(token: $token, validatedById: 6, economicEventId: 392) {
=======
  createValidation(token: $token, validatedById: 6, economicEventId: 393, note: "test") {
>>>>>>> a139cbfad931e5b4bd274df6524ccca95b6a3387
    validation {
      id
      validatedBy {
        name
      }
      economicEvent {
        action
        affectedQuantity {
          numericValue
          unit {
            name
          }
        }
      }
      validationDate
<<<<<<< HEAD
=======
      note
>>>>>>> a139cbfad931e5b4bd274df6524ccca95b6a3387
    }
  }
}

mutation ($token: String!) {
  deleteValidation(token: $token, id: 4) {
    validation {
      validationDate
    }
  }
}

mutation ($token: String!) {
  createAgentRelationship(token: $token, subjectId: 122, objectId: 119, 
    relationshipId: 9, note: "test") {
    agentRelationship {
      id
      subject {
        name
      }
      relationship {
        label
      }
      object {
        name
      }
      note
    }
  }
}

mutation ($token: String!) {
  updateAgentRelationship(token: $token, id: 275, subjectId: 122, objectId: 131, 
    note: "test update") {
    agentRelationship {
      id
      subject {
        name
      }
      relationship {
        label
      }
      object {
        name
      }
      note
    }
  }
}

mutation ($token: String!) {
<<<<<<< HEAD
  createPlace(token: $token, name:"testloc2", note:"test", address:"123 some street", latitude: 54.333, longitude: 45.333) {
    place {
      id
      name
      address
      latitude
      longitude
      note
    }
  }
}

mutation ($token: String!) {
=======
>>>>>>> a139cbfad931e5b4bd274df6524ccca95b6a3387
  createAgentResourceClassification(token: $token, agentId: 6, resourceClassificationId: 60) {
    agentResourceClassification {
      id
      agent {
        name
      }
      resourceClassification {
        name
      }
      action
    }
  }
}

mutation ($token: String!) {
  deleteAgentResourceClassification(token: $token, id: 42) {
    agentResourceClassification {
      agent {
        name
      }
      resourceClassification {
        name
      }
      action
    }
  }
}

<<<<<<< HEAD
mutation ($token: String!) {
  createResourceClassification(token: $token, note: "test create", name:"testrc", 
    image:"http://image.example", category: "inventory", unit:"Each") {
    resourceClassification {
      id
      name
      note
      unit {
        id
        name
      }
      image
      category
    }
  }
}

mutation ($token: String!) {
  createUnit(token: $token, name: "USD", symbol: "$") {
    unit {
      id
      name
      symbol
    }
  }
}

=======
>>>>>>> a139cbfad931e5b4bd274df6524ccca95b6a3387
'''
