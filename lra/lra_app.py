from libs.api_requests import api_post, quick_test, api_get


def create_application(input_data='create_application_input_data.json'):
    """
    Create the application with input data
    :param: input_data: This should be have json file as post request
    :return:
    """
    response = api_post('application', input_data)

    assert response.status_code == 201,"Application has been created " \
                                "Expected: 201, Actual: {act}".format(act=response.status_code)
    verify = True if "id" in response["result"]["id"] else False
    assert verify


def request_application_finalised_pdf(input_data):
    """
    finalize the application request
    :return:
    """
    result = quick_test('application/{applicationId', input_data)
    response_code = result[0]
    response_body = result[1]

    assert response_code == 201, "The status code returned creating application is not as expected. " \
                                 "Expected: 201, Actual: {act}".format(act=response_code)


def update_application(input_data):
    """
    update application data based on pass data
    :return:
    """
    info = api_post('application/{applicationId}', input_data)
    response_code = info[0]
    response_body = info[1]

    assert response_code == 201,"The status code returned creating application is not as " \
                                "expected. Expected: 201, Actual: {act}".format(act=response_code)


def request_application_draft_pdf(input_data = {}):
    """
    request application draft
    :return:
    """
    info = api_get('application/{applicationId', input_data)
    response_code = info[0]
    response_body = info[1]

    assert response_code == 201,"The status code returned creating application is not as " \
                                "expected. Expected: 201, Actual: {act}".format(act=response_code)

