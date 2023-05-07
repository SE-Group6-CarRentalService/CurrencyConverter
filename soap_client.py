from suds.client import Client
from suds.cache import NoCache

#my_client = Client('http://13.50.231.174:8501/SOAPservice/soap_service/?WSDL', cache=NoCache())
my_client = Client('https://currency-converter-g6.azurewebsites.net/SOAPservice/soap_service/?WSDL', cache=NoCache())

print(my_client)
print('output: ', my_client.service.convertCurrency('EUR',50,'JPY'))
