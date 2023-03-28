import requests
import xmltodict


USDrates = {}

def update_currencies(): 
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
    
    print("Rates were updated")