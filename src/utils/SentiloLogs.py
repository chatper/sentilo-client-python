import datetime

options = {
    'className' : 'Sentilo',
    'enableLogs' : True,
    'enableDebug' : False,
    'enableInfo' : True,
    'enableWarn' : True,
    'enableError' : True,
    'enableFatal' : True
}
    
def __logMessage(type, message):
    today = datetime.date.today()
    if options['enableLogs']:
        print('%s : [%s][%s] %s' % (today, options['className'], type, message))
            
def init(logsOptions):
    if logsOptions:
        options.update(logsOptions)
            
def debug(message):
    if options['enableDebug']:
        __logMessage('DEBUG', message)
            
def info(message):
    if options['enableInfo']:
        __logMessage('INFO', message)
            
def warn(message):
    if options['enableError']:
        __logMessage('ERROR', message)
        
def error(message):
    if options['enableError']:
        __logMessage('ERROR', message)
        
def fatal(message):
    if options['enableFatal']:
        __logMessage('FATAL', message)
