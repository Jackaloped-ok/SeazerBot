import os

#reads from Creds to deliver user credentials to bot
#params:
#return: arr creds: str
def initCreds():
    #contains user data for twitter
    credsFile = (r'{}\creds'.format(os.path.dirname(__file__)))
    with open(credsFile, 'r') as f:
        creds = f.read()
        
    creds = creds.split('\n')
    #empty line
    del creds[len(creds) - 1]

    #get the creds
    delLater = []
    for c in range(len(creds)):
        if creds[c][0] == '#':
            delLater.insert(0, c)
    for d in delLater:
        del creds[d]

    return(creds)

oauth_token, oauth_token_secret, API_key, API_key_secret, userID, screen_name = initCreds()
