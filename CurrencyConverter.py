import xml.etree.cElementTree as ET
import xmltodict
import requests   

USDrates = {}

def requestXML():

    global USDrates

    response = requests.get("http://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml")
    rates = xmltodict.parse(response.content)
    rates = rates['gesmes:Envelope']['Cube']['Cube']['Cube']
    USDtoEUR = rates[0]['@rate']
    for rate in rates:
        if(rate['@currency']!='USD'):
            USDrates[rate['@currency']] = float(rate['@rate'])/float(USDtoEUR)
        if(rate['@currency']=='USD'):
            USDrates['EUR'] = 1/float(rate['@rate'])
            
requestXML()

def convertPrice(price,currency):
    return price*USDrates[currency]


def convertCurrency(startcurr,quantity,endcurr):
    if(startcurr=="USD"):
        return quantity*USDrates[endcurr]
    if(endcurr=="USD"):
        return quantity/USDrates[startcurr]
    
    return quantity*(USDrates[endcurr]/USDrates[startcurr])