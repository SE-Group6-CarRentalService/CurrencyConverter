from django.test import TestCase, SimpleTestCase

class SOAPserviceTest(SimpleTestCase):

        def test_SOAPservice_statuscode(self):
                response = self.client.get('/SOAPservice/soap_service/?WSDL')
                self.assertEquals(response.status_code,200)
                                

# Create your tests here.
