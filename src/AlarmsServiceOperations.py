from utils import SentiloRestClient, SentiloLogs, SentiloUtils, SentiloResponse

path = {
    'path' : '/alarm'
}

def publish(alert, inputMessage):
    SentiloLogs.debug('Publishing alarm!')
    inputMessage.update(path)
    inputMessage['path'] = inputMessage['path'] + '/' + alert
    if inputMessage['body']['message']:
        try:
            response = SentiloRestClient.put(inputMessage)
            SentiloLogs.debug('Alarm published!')
            if response.status_code == 200:
                SentiloLogs.info('Successfully published alarm!')
                return SentiloResponse.success('200','Alarm published!')
        except Exception as e:
            SentiloLogs.error('Error while publishing alarm: ' + e.__str__())
            return SentiloResponse.error(type(e), e.__str__())
    else:
        SentiloLogs.debug('There is no alarm to publish!')
    return None

'''
# Test the functions above

options = {
    'host' : 'HOST_IP',
    'port' : 'HOST_PORT',
    'headers' : {
        'identity_key' : 'PROVIDER_ID'
    },
    'body' : {
        'message' : 'A test alarm'
    }
}
    
print(publish('test-alert', options))
'''
