from django.test import TestCase,Client
from django.contrib.auth.models import User

class UserAuthenticationTestCase(TestCase):

    def setUp(self):
        client=Client()
        User.objects.create_user("jawad","jawadkhan444@gmail.com","123456")

    def test_unauthorized_test_case(self):
        # Product view test
        response=self.client.get('/app/products/')
        self.assertEqual(response.status_code,401)

        # Address view test
        response=self.client.get('/app/address/')
        self.assertEqual(response.status_code,401)

        # Delete product view test
        response=self.client.get('/app/delete_product/1/')
        self.assertEqual(response.status_code,401)

        # Edit product view test
        response=self.client.get('/app/edit_product/1/')
        self.assertEqual(response.status_code,401)

        # User products test view test
        response=self.client.get('/app/my_products/')
        self.assertEqual(response.status_code,401)

        # Address view test
        response=self.client.get('/app/profile/')
        self.assertEqual(response.status_code,401)
        # Address view test
        response=self.client.get('/app/upload_image/')
        self.assertEqual(response.status_code,401)

        # Address view test
        response=self.client.get('/app/logout/')
        self.assertEqual(response.status_code,401)

