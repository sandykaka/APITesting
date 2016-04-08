import os

from libs.api_requests import api_post, quick_test, api_get

def get_token(url, body):
    """
    This method will call the api to get the token number
    :return:
    """
    return api_post(url, body)

def refresh_token(url, body):
    """
    this will refresh the token
    :return:
    """
    return api_post(url, body)


def create_application(payload_data='create_application_input_data.json'):
    """
    Create the application with input file data
    :param: input_data: This should be have json file as post request
    :return:
    """
    current_location = os.getcwd()
    payload_file = os.path.join(current_location + "/data/" + payload_data)
    response = api_post('application', payload_data)

    assert response.status_code == 201,"Application has not been created " \
                                "Expected: 201, Actual: {act}".format(act=response.status_code)
    verify = True if "id" in response["result"]["id"] else False
    assert verify


def request_application_finalised_pdf(input_data):
    """
    finalize the application request
    :return:
    """
    pass

def update_application(input_data):
    """
    update application data based on pass data
    :return:
    """
    pass

def request_application_draft_pdf(input_data = {}):
    """
    request application draft
    :return:
    """
    pass

