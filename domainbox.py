from suds.client import Client

class DomainBox(object):
    LIVE_URL = 'https://live.domainbox.net/?WSDL'
    SANDBOX_URL = 'https://sendbox.domainbox.net/?WSDL'

    def __init__(self, reseller, username, password, live=False):
        if live is True:
            self.client = Client(LIVE_URL)
        else:
            self.client = Client(SANDBOX_URL)

        self.auth_params = self.client.factory.create('AuthenticationParameters')

        self.auth_params.Reseller = reseller
        self.auth_params.Username = username
        self.auth_params.Password = password
