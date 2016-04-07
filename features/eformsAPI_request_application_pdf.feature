# Created by Dele Odusanya at 28/03/16
Feature: Request the application PDF via API and the PDF is returned

  Scenario Outline: send a message to RoS eServices to request the eForm PDF, send back a final application PDF 4
    Given I am an external Integrator
    When I send a request for a <application type> application PDF via API providing the application ID that has been sent by RoS eForms
    And the application ID is confirmed as valid
    If the <application type> application PDF is marked as final and locked to further editing
    Then I receive via API the application PDF for the <application type>


    Examples:
      | application type |
      | DW               |
      | TP               |
      | FR               |
      | VR               |
      | APR              |
