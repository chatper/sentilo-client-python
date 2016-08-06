from utils import SentiloRestClient, SentiloLogs, SentiloUtils, SentiloResponse

path = {
    'path' : '/subscribe/order'
}

def subscribe(inputMessage):
    SentiloLogs.debug('Adding subscription message!')
    inputMessage.update(path)
    inputMessage['path'] = inputMessage['path'] + '/' + inputMessage['provider'] + '/' + inputMessage['sensor']
    if inputMessage['body']['endpoint']:
        try:
            response = SentiloRestClient.put(inputMessage)
            SentiloLogs.debug('Subscription added!')
            if response.status_code == 200:
                SentiloLogs.info('Successfully added subscription!')
                return SentiloResponse.success('200','Subscription added!')
        except Exception as e:
            SentiloLogs.error('Error while adding subscription: ' + e.__str__())
            return SentiloResponse.error(type(e), e.__str__())
    else:
        SentiloLogs.debug('There are no subscriptions to add!')
    return None

def subscribeToAll(inputMessage):
    SentiloLogs.debug('Adding subscription message to all sensors!')
    inputMessage.update(path)
    inputMessage['path'] = inputMessage['path'] + '/' + inputMessage['provider']
    if inputMessage['body']['endpoint']:
        try:
            response = SentiloRestClient.put(inputMessage)
            SentiloLogs.debug('Subscription added to all sensors!')
            if response.status_code == 200:
                SentiloLogs.info('Successfully added subscription to all sensors!')
                return SentiloResponse.success('200','Subscription added to all sensors!')
        except Exception as e:
            SentiloLogs.error('Error while adding subscription to all sensors: ' + e.__str__())
            return SentiloResponse.error(type(e), e.__str__())
    else:
        SentiloLogs.debug('There are no subscriptions to add!')
    return None
