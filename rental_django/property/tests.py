from django.test import TestCase
from property.models import Property, Request, Contract
from users.models import Comuna
from django.contrib.auth.models import User
# Create your tests here.

# setuptestdata

class PropertyTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
            renter = User.objects.create_user('testuser', 'test@test.com', 'testpassword')
            renter.save()
            landlord = User.objects.create_user('testlandlord', 'landord@test.com', 'landlordpassword')
            landlord.save()

    def test_property_crud(self):
        property = Property.objects.create(
            name = 'Casa de prueba',
            description = 'Casa de prueba',
            m2_building = 100,
            m2_total = 200,
            n_parking = 1,
            n_bedrooms = 3,
            n_bathrooms = 2,
            address = 'Calle de prueba 123',
            comuna = Comuna.objects.get_or_create(nombre='Providencia')[0],
            ptype = 0,
            price = 1000000,
            landlord = User.objects.get(username='testlandlord')
        )
        self.assertEqual(property.name, 'Casa de prueba')
        self.assertEqual(property.description, 'Casa de prueba')
        self.assertEqual(property.m2_building, 100)
        self.assertEqual(property.m2_total, 200)
        self.assertEqual(property.n_parking, 1)
        self.assertEqual(property.n_bedrooms, 3)
        self.assertEqual(property.n_bathrooms, 2)
        self.assertEqual(property.address, 'Calle de prueba 123')
        self.assertEqual(property.ptype, 0)
        self.assertEqual(property.price, 1000000)

        property.name = 'Casa de prueba 2'
        property.save()
        self.assertEqual(property.name, 'Casa de prueba 2')

        property.delete()
        self.assertEqual(Property.objects.count(), 0)

    def test_request_crud(self):
        test_property = Property.objects.create(
            name = 'Casa de prueba',
            description = 'Casa de prueba',
            m2_building = 100,
            m2_total = 200,
            n_parking = 1,
            n_bedrooms = 3,
            n_bathrooms = 2,
            address = 'Calle de prueba 123',
            comuna = Comuna.objects.get_or_create(nombre='Providencia')[0],
            ptype = 0,
            price = 1000000,
            landlord = User.objects.get(username='testlandlord')
        )
        user = User.objects.get(username='testuser')
        request = Request.objects.create(
            origin_property = test_property,
            user = user,
            message = 'Mensaje de prueba'
        )
        self.assertEqual(request.origin_property, test_property)
        self.assertEqual(request.user, user)
        self.assertEqual(request.message, 'Mensaje de prueba')

        request.message = 'Mensaje de prueba 2'
        request.save()
        self.assertEqual(request.message, 'Mensaje de prueba 2')

        request.delete()
        self.assertEqual(Request.objects.count(), 0)

    def test_contract_crud(self):
        test_property = Property.objects.create(
            name = 'Casa de prueba',
            description = 'Casa de prueba',
            m2_building = 100,
            m2_total = 200,
            n_parking = 1,
            n_bedrooms = 3,
            n_bathrooms = 2,
            address = 'Calle de prueba 123',
            comuna = Comuna.objects.get_or_create(nombre='Providencia')[0],
            ptype = 0,
            price = 1000000,
            landlord = User.objects.get(username='testlandlord')
        )
        test_user = User.objects.get(username='testuser')
        request = Request.objects.create(
            origin_property = test_property,
            user = test_user,
            message = 'Mensaje de prueba'
        )
        contract = Contract.objects.create(
            origin_request = request,
            start_date = '2020-01-01',
            end_date = '2020-02-01',
            price = 1000000,
            status = False
        )
        self.assertEqual(contract.origin_request, request)
        self.assertEqual(contract.start_date, '2020-01-01')
        self.assertEqual(contract.end_date, '2020-02-01')
        self.assertEqual(contract.price, 1000000)
        self.assertEqual(contract.status, False)

        contract.status = True
        contract.save()
        self.assertEqual(contract.status, True)

        contract.delete()
        self.assertEqual(Contract.objects.count(), 0)