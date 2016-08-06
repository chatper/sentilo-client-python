from utils import SentiloRestClient, SentiloLogs, SentiloUtils, SentiloResponse

path = {
    'path' : '/catalog'
}

'''
    Retrieve a sensors list for the provider, into a data estructure that
    represents the entire provider information
     
    @param inputMessage
        A properties object that describes the request options
    @returns JSON Object If the request goes OK, then return a JSON object
        that contains a list of sensors for the provider. Returns an
        error object in other case
'''
def getSensors(inputMessage):
    SentiloLogs.debug('Retrieving authorized sensors from catalog!')
    inputMessage.update(path)
    inputMessage['path'] = inputMessage['path'] + '/' + inputMessage['provider']
    try:
        response = SentiloRestClient.get(inputMessage)
        SentiloLogs.debug('Sensors retrieved!')
        return response.json()['providers'][0]
    except Exception as e:
        SentiloLogs.error('Error while retrieving sensors!')
        return SentiloResponse.error(type(e),e.__str__())
    return None


'''
    Registers a list of sensors into the catalog. The inputMessage must
    contains, at least, a body field with a correct sensors list structure
    like the especified in the Sentilo API Doc. Please, see this url for more
    information:
    http://www.sentilo.io/xwiki/bin/view/APIDocs.Service.Catalog/CreateSensors
     
    @param inputMessage
        A properties object that describes the request options, with
        the list of sensors
'''
def registerSensors(inputMessage):
    SentiloLogs.debug('Registering sensors!')
    inputMessage.update(path)
    inputMessage['path'] = inputMessage['path'] + '/' + inputMessage['provider']
    if inputMessage['body']['sensors']:
        try:
            response = SentiloRestClient.post(inputMessage)
            SentiloLogs.debug('Sensors registered!')
            if response.status_code == 200:
                SentiloLogs.info('Successfully registered sensors!')
                return SentiloResponse.success('200','Sensors registered!')
        except Exception as e:
            SentiloLogs.error('Error while registering sensors: ' + e.__str__())
            return SentiloResponse.error(type(e), e.__str__())
    else:
        SentiloLogs.debug('There are no sensors to register!')
    return None


'''
    Update a list of sensors that already exists into the catalog. The
    inputMessage must contains, at least, a body field with a correct sensors
    list structure like the especified in the Sentilo API Doc. Please, see
    this url for more information:
    http://www.sentilo.io/xwiki/bin/view/APIDocs.Service.Catalog/CreateSensors
     
    @param inputMessage
        A properties object that describes the request options, with
        the list of sensors
'''
def updateSensors(inputMessage):
    SentiloLogs.debug('Updating sensors!')
    inputMessage.update(path)
    inputMessage['path'] = inputMessage['path'] + '/' + inputMessage['provider']
    if inputMessage['body']['sensors']:
        try:
            response = SentiloRestClient.put(inputMessage)
            SentiloLogs.debug('Sensors updated!')
            if response.status_code == 200:
                SentiloLogs.info('Successfully updated sensors!')
                return SentiloResponse.success('200','Sensors updated!')
        except Exception as e:
            SentiloLogs.error('Error while updating sensors: ' + e.__str__())
            return SentiloResponse.error(type(e), e.__str__())
    else:
        SentiloLogs.debug('There are no sensors to update!')
    return None


'''
    Registers a list of alerts into the catalog. The inputMessage must
    contains, at least, a body field with a correct alerts list structure
    like the especified in the Sentilo API Doc. Please, see this url for more
    information:
    http://www.sentilo.io/xwiki/bin/view/APIDocs.Services.Alert/CreateAlerts
     
    @param inputMessage
        A properties object that describes the request options, with
        the list of alerts
'''
def registerAlerts(inputMessage):
    SentiloLogs.debug('Registering alerts!')
    inputMessage.update(path)
    inputMessage['path'] = inputMessage['path'] + '/' + '/alert/' + inputMessage['provider']
    if inputMessage['body']['alerts']:
        try:
            response = SentiloRestClient.post(inputMessage)
            SentiloLogs.debug('Alerts registered!')
            print(response)
            if response.status_code == 200:
                SentiloLogs.info('Successfully registered alerts!')
                return SentiloResponse.success('200','Alerts registered!')
        except Exception as e:
            SentiloLogs.error('Error while registering alerts: ' + e.__str__())
            return SentiloResponse.error(type(e), e.__str__())
    else:
        SentiloLogs.debug('There are no alerts to register!')
    return None

'''
# Test the functions above

options = {
    'host' : 'HOST_IP',
    'port' : 'HOST_PORT',
    'headers' : {
        'identity_key' : 'PROVIDER_ID'
    },
    'provider' : 'TestProiver',
    'sensor' : 'TestSensor',
    'body' : {
        'alerts' : [{
            'id' : 'testAlert',
            'type' : 'EXTERNAL'
        }]
    }
}
'''
