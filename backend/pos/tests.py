from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from common.tests import LoginMixin
from model_mommy import mommy
from users.models import User
from .models import(
    Organization, SalesAgent, ProductTypes, Sales
)


class TestProductTypeViews(LoginMixin, APITestCase):

    def test_create_product_types(self):
        data = {
            "name": "Insurance",
            "organization": mommy.make(Organization).id
        }
        url = reverse('api:v1:pos:product_type')
        response = self.client.post(url, data)
        self.assertEquals(201, response.status_code)
        self.assertEqual(response.data['name'], data['name'])

    def test_update_product_type(self):
        pt = mommy.make(
            ProductTypes, name='Insurance')
        url = reverse(
            'api:v1:pos:product_type_details', kwargs={'pk': pt.id})
        data = {
            "name": "Bank Account"
        }
        response = self.client.patch(url, data)
        self.assertEquals(200, response.status_code)
        self.assertEqual(response.data['name'], data['name'])

    def test_retrive_product_type(self):
        pt = mommy.make(
            ProductTypes, name='Insurance')
        mommy.make(ProductTypes)
        url = reverse(
            'api:v1:pos:product_type_details', kwargs={'pk': pt.id})
        response = self.client.get(url)
        self.assertEquals(200, response.status_code)
        self.assertEqual(response.data['name'], "Insurance")

    def test_list_product_types(self):
        pt = mommy.make(
            ProductTypes, name="insurance")
        pt2 = mommy.make(ProductTypes)
        url = reverse(
            'api:v1:pos:product_type')
        response = self.client.get(url)
        self.assertEquals(200, response.status_code)
        res = [item['name'] for item in response.data['results']]
        self.assertIn(pt.name, res)
        self.assertIn(pt2.name, res)


class TestSalesAgentViews(LoginMixin, APITestCase):

    def test_create_sales_agent_success(self):
        data = {
            "profile": {
                "email": "user@pos.co.ke",
                "first_name": "Hakuna",
                "last_name": "Ruhusa",
                "other_names": "",
                "password": "rubbishpass"
            },
            "organization": mommy.make(Organization).id
        }
        url = reverse('api:v1:pos:agent')
        response = self.client.post(url, data)
        self.assertEquals(201, response.status_code)
        self.assertEqual(
            response.data['profile']['email'], data['profile']['email'])

    def test_create_agent_fail_missing_email(self):
        data = {
            "profile": {
                "first_name": "Hakuna",
                "last_name": "Ruhusa",
                "other_names": "",
                "password": "rubbishpass"
            },
            "organization": mommy.make(Organization).id
        }
        url = reverse('api:v1:pos:agent')
        response = self.client.post(url, data)
        self.assertEquals(400, response.status_code)
        self.assertTrue('profile' in response.data)
        self.assertTrue('email' in response.data['profile'])

    def test_update_sales_agent_success(self):
        user = mommy.make(User, email='user_test@gmail.com')
        agent = mommy.make(
            SalesAgent, profile=user)
        url = reverse(
            'api:v1:pos:agent_details',
            kwargs={'pk': agent.id})
        data = {
            "profile": {
                "id": str(user.id),
                "email": "new_email@gmail.com"
            }
        }
        response = self.client.patch(url, data)
        self.assertEquals(200, response.status_code)
        self.assertEqual(
            response.data['profile']['email'], data['profile']['email'])

    def test_update_sales_agent_success_no_profile(self):
        user = mommy.make(User, email='user_test@gmail.com')
        agent = mommy.make(
            SalesAgent, profile=user, organization=mommy.make(Organization))
        url = reverse(
            'api:v1:pos:agent_details',
            kwargs={'pk': agent.id})
        org = mommy.make(Organization)
        data = {
            "organization": org.id
        }
        response = self.client.patch(url, data)
        self.assertEquals(200, response.status_code)
        self.assertEqual(response.data['organization'], org.id)

    def test_update_sales_agent_fail(self):
        user = mommy.make(User, email='user_test@gmail.com')
        agent = mommy.make(
            SalesAgent, profile=user)
        url = reverse(
            'api:v1:pos:agent_details',
            kwargs={'pk': agent.id})
        data = {
            "profile": {
                "email": "new_email@gmail.com"
            }
        }
        response = self.client.patch(url, data)
        self.assertEquals(400, response.status_code)
        self.assertTrue('profile' in response.data)

    def test_retrieve_sales_agent(self):
        user = mommy.make(User, email='user_test@gmail.com')
        agent = mommy.make(
            SalesAgent, profile=user)
        mommy.make(SalesAgent)
        url = reverse(
            'api:v1:pos:agent_details',
            kwargs={'pk': agent.id})
        response = self.client.get(url)
        self.assertEquals(200, response.status_code)
        self.assertEqual(
            response.data['profile']['email'], "user_test@gmail.com")

    def test_list_sales_agents(self):
        user = mommy.make(User, email='user_test@gmail.com')
        agent = mommy.make(
            SalesAgent, profile=user)
        agent2 = mommy.make(SalesAgent)
        url = reverse(
            'api:v1:pos:agent')
        response = self.client.get(url)
        self.assertEquals(200, response.status_code)
        res = [item['id'] for item in response.data['results']]
        self.assertIn(str(agent.id), res)
        self.assertIn(str(agent2.id), res)


class TestOrganizationViews(LoginMixin, APITestCase):

    def test_create_organization_success(self):
        data = {
            "profile": {
                "email": "user@pos.co.ke",
                "first_name": "Hakuna",
                "last_name": "Ruhusa",
                "other_names": "",
                "password": "rubbishpass"
            }
        }
        url = reverse('api:v1:pos:organization')
        response = self.client.post(url, data)
        self.assertEquals(201, response.status_code)
        self.assertEqual(
            response.data['profile']['email'], data['profile']['email'])

    def test_create_organization_fail_missing_email(self):
        data = {
            "profile": {
                "first_name": "Hakuna",
                "last_name": "Ruhusa",
                "other_names": "",
                "password": "rubbishpass"
            }
        }
        url = reverse('api:v1:pos:organization')
        response = self.client.post(url, data)
        self.assertEquals(400, response.status_code)
        self.assertTrue('profile' in response.data)
        self.assertTrue('email' in response.data['profile'])

    def test_update_organization_success(self):
        user = mommy.make(User, email='user_test@gmail.com')
        org = mommy.make(
            Organization, profile=user)
        url = reverse(
            'api:v1:pos:organization_details',
            kwargs={'pk': org.id})
        data = {
            "profile": {
                "id": user.id,
                "email": "new_email@gmail.com"
            }
        }
        response = self.client.patch(url, data)
        self.assertEquals(200, response.status_code)
        self.assertEqual(
            response.data['profile']['email'], data['profile']['email'])

    def test_retrieve_organization(self):
        user = mommy.make(User, email='user_test@gmail.com')
        org = mommy.make(
            Organization, profile=user)
        mommy.make(SalesAgent)
        url = reverse(
            'api:v1:pos:organization_details',
            kwargs={'pk': org.id})
        response = self.client.get(url)
        self.assertEquals(200, response.status_code)
        self.assertEqual(
            response.data['profile']['email'], "user_test@gmail.com")

    def test_list_organizations(self):
        user = mommy.make(User, email='user_test@gmail.com')
        org = mommy.make(
            Organization, profile=user)
        org2 = mommy.make(Organization)
        url = reverse(
            'api:v1:pos:organization')
        response = self.client.get(url)
        self.assertEquals(200, response.status_code)
        res = [item['id'] for item in response.data['results']]
        self.assertIn(str(org.id), res)
        self.assertIn(str(org2.id), res)


class TestSalesViews(LoginMixin, APITestCase):

    def test_create_sales(self):
        data = {
            "latitude": 0.03232,
            "longitude": 0.323232,
            "product": mommy.make(ProductTypes).id,
            "customer_email": "customer@gmail.com",
            "customer_id_number": "29143213",
            "customer_phone": "0715441321",
            "customer_first_name": "Brian",
            "customer_last_name": "Leon",
            "follow_up_date": "2015-09-09T00:00:00",
            "agent": mommy.make(SalesAgent).id
        }
        url = reverse('api:v1:pos:sales')
        response = self.client.post(url, data)
        self.assertEquals(201, response.status_code)
        self.assertEqual(
            response.data['customer_email'], data['customer_email'])

    def test_update_sales(self):
        sale = mommy.make(
            Sales, customer_email='customer@gmail.com')
        url = reverse(
            'api:v1:pos:sales_details', kwargs={'pk': sale.id})
        data = {
            "customer_email": "customer2@gmail.com"
        }
        response = self.client.patch(url, data)
        self.assertEquals(200, response.status_code)
        self.assertEqual(
            response.data['customer_email'], data['customer_email'])

    def test_rsales(self):
        sales = mommy.make(
            Sales, customer_email="customer@gmail.com")
        mommy.make(Sales)
        url = reverse(
            'api:v1:pos:sales_details', kwargs={'pk': sales.id})
        response = self.client.get(url)
        self.assertEquals(200, response.status_code)
        self.assertEqual(response.data['customer_email'], "customer@gmail.com")

    def test_list_sales(self):
        sale = mommy.make(Sales)
        sale2 = mommy.make(Sales)
        url = reverse(
            'api:v1:pos:sales')
        response = self.client.get(url)
        self.assertEquals(200, response.status_code)
        res = [item['customer_email'] for item in response.data['results']]
        self.assertIn(sale.customer_email, res)
        self.assertIn(sale2.customer_email, res)
