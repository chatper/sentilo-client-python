from utils import SentiloRestClient, SentiloLogs, SentiloUtils, SentiloResponse    
    
path = {
    'path' : '/data'
}

'''
    Retrieve a list of the last observations published on a sensor
     
    @param inputMessage
        A map opbject where you can specify params for silter the
        query (it must be in a field named 'qs')
    @returns A JSON object with the observations list
'''
def getLastObservations(inputMessage):
    inputMessage.update(path)
    inputMessage['path'] = inputMessage['path'] + '/' + inputMessage['provider'] + '/' + inputMessage['sensor']
    try:
        response = SentiloRestClient.get(inputMessage)
        SentiloLogs.debug('Observations have been retrieved!')
        return response.json()
    except Exception as e:
        SentiloLogs.error('Error while retrieving observations: ' + e.__str__())
        return SentiloResponse.error(type(e), e.__str__())
    return None

'''
    Send a single or a list of observations to a sensor. It may be an
    observation structure like the specified in the Sentilo API Doc. Please
    see this url for more information:
    http://www.sentilo.io/xwiki/bin/view/ApiDocs.Services.Data/PublishSensorData
    
    @param inputMessage
        A python dictionary with a list of observations
    @returns A JSON object only if there is an error
'''
def sendObservations(inputMessage):
    SentiloLogs.debug('Sending observations')
    inputMessage.update(path)
    inputMessage['path'] = inputMessage['path'] + '/' + inputMessage['provider'] + '/' + inputMessage['sensor']
    if inputMessage['body']['observations']:
        try:
            response = SentiloRestClient.put(inputMessage)
            SentiloLogs.debug('Observations has been sent!')
            if response.status_code == 200:
                SentiloLogs.info('Successfully sent observation!')
                return SentiloResponse.success('200','Observation sent!')
        except Exception as e:
            SentiloLogs.error('Error while sending observations: ' + e.__str__())
            return SentiloResponse.error(type(e), e.__str__())
    else:
        SentiloLogs.debug('There are no observations to send!')
    return None

'''
# Test the functions above

options = {
    'host' : 'HOST_IP',
    'port' : 'HOST_PORT',
    'headers' : {
        'identity_key' : 'PROVIDER_ID'
    },
    'provider' : 'TestProvider',
    'sensor' : 'TestSensor',
    'body' : {
        'observations' : [{
        'value' : '42'
    }]
    }
}
'''
