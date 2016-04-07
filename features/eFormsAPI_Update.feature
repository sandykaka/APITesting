# Created by dele odusanya at 28/03/16
Feature: Send a create/update LR application via API and receive a response - includes basic validation

  Scenario Outline: Send an API to create/update an LR application

  Given I am an External Integrator
  And I send an application API to RoS eForms to update a <application type> application
  When the application is successfully received by RoS eForms
  Then it can be validated against the basic rule sets for an application <application type>

    Examples:
      | application type |
      | DW               |
      | TP               |
      | FR               |
      | VR               |
      | APR              |


