import requests

def get(requestOptions):
    if (requestOptions):
        url = 'http://' + requestOptions['host'] + ':' + requestOptions['port'] + requestOptions['path']
        res = requests.get(url, headers=requestOptions['headers'])
        return res
    return None
    
def post(requestOptions):
    if (requestOptions):
        url = 'http://' + requestOptions['host'] + ':' + requestOptions['port'] + requestOptions['path']
        res = requests.post(url, headers=requestOptions['headers'], json=requestOptions['body'])
        return res
    return None
    
def put(requestOptions):
    if (requestOptions):
        url = 'http://' + requestOptions['host'] + ':' + requestOptions['port'] + requestOptions['path']
        res = requests.put(url, headers= requestOptions['headers'], json=requestOptions['body'])
        return res
    return None
