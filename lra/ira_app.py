from libs.api_requests import api_post, quick_test, api_get


def create_application(input_data='create_application_input_data.json'):
    """
    Create the application with input data
    :return:
    """
    info = api_post('application', input_data)
    response_code = info[0]
    response_body = info[1]

    assert response_code == 201,"The status code returned creating application is not as " \
                                "expected. Expected: 201, Actual: {act}".format(act=response_code)
    assert response_body.contains, "id"

    #rs_deed = response_body["application_name"]["type_of_deed"]
    #rs_id = response_body["application_name"]["id"]

    #assert rs_deed == type_of_deed, "The type of deed in response is not same as in request"
    # "The response type of deed is: {}".format(rs_deed)

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

