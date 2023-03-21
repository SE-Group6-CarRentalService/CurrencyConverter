from suds.client import Client
from suds.cache import NoCache

my_client = Client('http://127.0.0.1:9000/SOAPservice/soap_service/?WSDL', cache=NoCache())
print(my_client)
print('output: ', my_client.service.convertCurrency('EUR',50,'JPY'))