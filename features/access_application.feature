# Created by Dele Odusanya at 07/04/16
Feature: Get the token and refresh the user

  Scenario: I can successfully obtain an access token
      Given I am an External Integrator
      When I ask for access token and refresh it
      When I send an application API to RoS eForms to create/update a <application type> application

