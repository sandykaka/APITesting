import json
import time
import traceback
import requests
from logging_conf import Logger


def api_get(call):
    """
    This function executes GET call for API
    """
    max_tries = 2
    rs = None
    for retry in xrange(max_tries):
        try:
            rs = requests.get(call)
            rs = [rs ,json.loads(rs.text) ,call]
            return rs if rs[0].status_code not in [500, 404] else \
                Logger.logr.info("Request failed")
        except \
        (ValueError, requests.ConnectionError, requests.RequestException) as er:
            traceback.print_exc()
            Logger.logr.debug("Error found as : {}".format(er))
            Logger.logr.debug(
                "GET: %s fail once retrying again..." % call) if retry == 1 \
                else Logger.logr.error("Request failed")
            time.sleep(1)

    return rs


def api_post(call, payload):
    """This function executes POST call for API

    Example of call: Full URL
    Example of body:

    {"items": [{"id": "5571294817", \
    "item": "14856071", "quantity": 1}], \
    "userId": 24279715}
    """
    headers = {'Content-Type': 'application/json'}
    rs = None
    payload = json.dumps(payload) if type(payload) == dict else payload
    try:
        rs = requests.post(call, data = payload, headers = headers)
        Logger.logr.debug(call)
        if rs.status_code in [500,404]:
            Logger.logr.error(">>>>>>>request get failed<<<<<<<")

    except (ValueError, requests.RequestException, requests.ConnectionError, requests.HTTPError) as request_err:
        traceback.print_exc()
        Logger.logr.debug("error while calling the api endpoint as {}".format(request_err))
        Logger.logr.error("Error while accessing the endpoint")


    return rs

def api_put(call, payload):
    """
    This function executes PUT call for API
    """
    headers = {'content-type': 'application/json'}
    rs = ''
    try:
        #escape situation with locked transaction where 409 is returned
        counter = 0
        delay_flag = True
        rs = None
        while delay_flag == True:
            counter += 1
            if counter <= 12:
                rs = requests.put(call, data = payload, headers = headers)
                rs = [rs,json.loads(rs.text),call]
                Logger.logr.debug('~')
                Logger.logr.debug(call)

                if rs[0].status_code not in [409]:
                    delay_flag=False
                else:
                    Logger.logr.debug("GOT 409 (order lock) *|-= sleeping for 10 seconds")
                    time.sleep(10)
            else:
                delay_flag = False

        if rs[0].status_code in [500,404]:
            Logger.logr.error("request get failed")

    except (ValueError, requests.RequestException, requests.ConnectionError, requests.HTTPError) as request_err:
        Logger.logr.debug("error while calling the api endpoint as {}".format(request_err))

    return rs

def api_delete(call):
    """
    Description: This function executes DELETE call for API
    :parameter call: endpoint to call
    Example of call: /user_profile/50355425
    """
    counter = 0
    max_tries = 2

    rs = ''
    while counter < max_tries:
        try:
            rs = requests.delete(call)
            rs = [rs, '', call]
            if 'tosnew' not in call.split('/'):
                Logger.logr.info('~')
                Logger.logr.info(call)

            if rs[0].status_code in [500, 404]:
                Logger.logr.error("request get failed")
            counter = max_tries
        except (ValueError, requests.RequestException, requests.ConnectionError, requests.HTTPError) as request_err:
            traceback.print_exc()
            Logger.logr.debug("error while calling the api endpoint as {}".format(request_err))
            if counter < max_tries:
                counter += 1
                Logger.logr.debug('DELETE: %s fail once...' % call)
                time.sleep(1)
            else:
                Logger.logr.error("request get failed")
                return rs[0].status_code
            raise Exception('Error in call!')

    return rs

def quick_test(rs,expected_status_code):
    """
    Description:
    Parameters:
    Returns:
    """
    #test for status code
    if type(rs) is list:

        if rs[0].status_code !=409 :

            assert rs[0].status_code == expected_status_code, \
                "Actual status_code: %s. Expected status_code: %s. URL: %s. Response: %s. " % \
                (rs[0].status_code,expected_status_code,rs[2],rs[1])

    else:
        assert rs.status_code == expected_status_code, \
            "Actual status_code: %s. Expected status_code: %s " % \
            (rs.status_code,expected_status_code)

    # check if errors section of api response is not empty
    try:
        api_rs = rs[1]
        if api_rs['errors'] !={}:
            Logger.logr.info('!!!!'+str(api_rs['errors']))
    except (KeyError, TypeError, IndexError) as ierror:
        Logger.logr.debug("quick test verification failed as => '{}'".format(ierror))

    try:
        api_rs = rs[1][0]
        if api_rs['errors'] != {}:
            Logger.logr.info('!!!!'+str(api_rs['errors']))
    except (ValueError, KeyError, TypeError, IndexError) as ierror:
        Logger.logr.debug("quick test verification failed as => '{}'".format(ierror))

def json_file_to_string(self, file_location):
    """
    This method will convert any file to json string, which can be used as payload to make the requests
    :param self:
    :param file_location:  location of the file
    :return:  return json data
    """
    with open(file_location) as json_data:
        json_data = json.load(json_data)
        return json.dumps(json_data)

