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
from SOAPservice.Curr_Update import USDrates


class SoapService(ServiceBase):

    @rpc(str, Integer(nillable=False),str, _returns=float)
    def convertCurrency(ctx,startcurr, quantity, endcurr):
        
        global USDrates

        if startcurr == "USD" and endcurr == "USD":
            return quantity
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
