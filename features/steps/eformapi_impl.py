from behave import *
from behave import Given
from behave import Then
from behave import When

use_step_matcher("re")

''' Start of Binding List

    @Given("I am an External Integrator")
    @When("I send an application API to RoS eForms to create/update a <application type> application")
    @Then("the application is successfully received by RoS eForms")
    @Then("it can be validated against the basic rule sets for an application < application type = DW, TP, FR, VR or APR>")
    @step("I send an application API to RoS eForms to create a (.+) application")
    @then("it can be validated against the basic rule sets for an application (.+)")
    @step("the application is successfully received by RoS eForms")

End Of Binding List '''

@Given("I am an External Integrator")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@When("I send an application API to RoS eForms to create/update a <application type> application")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    pass


@Then("the application is successfully received by RoS eForms")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@Then("it can be validated against the basic rule sets for an application < application type = DW, TP, FR, VR or APR>")
def step_impl(context):
    # context.execute_steps(assert info[1].contains, "id")
    """
    :type context: behave.runner.Context
    """
    pass


@When("I send an application API to RoS eForms to create a (.+) application")
def step_impl(context, arg0):
    """
    :type context: behave.runner.Context
    :type arg0: str
    """
    pass



@Then("it can be validated against the basic rule sets for an application (.+)")
def step_impl(context, arg0):
    """
    :type context: behave.runner.Context
    :type arg0: str
    """
    pass


@Then("the application is successfully received by RoS eForms")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass