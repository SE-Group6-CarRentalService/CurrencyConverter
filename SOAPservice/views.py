from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from spyne.application import Application
from spyne.decorator import rpc
from spyne.model.primitive import Unicode, Integer
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from spyne.service import ServiceBase
import xml.etree.cElementTree as ET
import xmltodict
import requests

USDrates = {}

def requestXML():

    global USDrates

    response = requests.get(
        "http://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"
    )
    rates = xmltodict.parse(response.content)
    rates = rates["gesmes:Envelope"]["Cube"]["Cube"]["Cube"]
    USDtoEUR = rates[0]["@rate"]
    for rate in rates:
        if rate["@currency"] != "USD":
            USDrates[rate["@currency"]] = float(rate["@rate"]) / float(USDtoEUR)
        if rate["@currency"] == "USD":
            USDrates["EUR"] = 1 / float(rate["@rate"])


class SoapService(ServiceBase):

    @rpc(str, Integer(nillable=False),str, _returns=float)
    def convertCurrency(ctx,startcurr, quantity, endcurr):
        
        requestXML()

        if startcurr == "USD":
            return quantity * USDrates[endcurr]
        if endcurr == "USD":
            return quantity / USDrates[startcurr]

        return round(quantity * (USDrates[endcurr] / USDrates[startcurr]),2)


soap_app = Application(
    [SoapService],
    tns='django.soap.currencyconverter',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

django_soap_application = DjangoApplication(soap_app)
my_soap_application = csrf_exempt(django_soap_application)
