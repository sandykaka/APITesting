# Created by Dele Odusanya at 28/03/16
Feature: Send a create/update LR application via API and receive a response - includes basic validation

  Scenario Outline: Send an API to create/update an LR application
    Given I am an External Integrator <name>
    When I send an application API to RoS eForms to create a <application type> application
    And the application is successfully received by RoS eForms
    Then it can be validated against the basic rule sets for an application <application type>
    Examples:
      | application type | name          |
      | DW               | extIntegrator1|
      | TP               | extIntegrator1|
      | FR               | extIntegrator1|
      | VR               | extIntegrator1|
      | APR              | extIntegrator1|




