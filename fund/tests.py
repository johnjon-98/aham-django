from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class FundAPITestCase(APITestCase):

    def setUp(self):
        self.fund_data = {
            "name": "Fund 1",
            "manager": "Alice",
            "description": "A sample fund for test.",
            "net_asset_value": 1000000,
            "performance": 7.45
        }
        self.create_url = reverse('fund:fund_c')
        self.fund = self.client.post(self.create_url, self.fund_data).data


    def test_create_fund(self):
        response = self.client.post(self.create_url, self.fund_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['data']['name'], self.fund_data['name'])

    def test_list_funds(self):
        list_url = reverse('fund:fund_l')
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_read_fund(self):
        read_url = reverse('fund:fund_r', args=[self.fund['data']['id']])
        response = self.client.get(read_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.fund['data']['id'])

    def test_update_fund(self):
        update_url = reverse('fund:fund_u', args=[self.fund['data']['id']])
        updated_data = self.fund_data.copy()
        updated_data['performance'] = 9.1
        response = self.client.put(update_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['performance'], 9.1)

    def test_partial_update_fund(self):
        patch_url = reverse('fund:fund_u', args=[self.fund['data']['id']])
        response = self.client.patch(patch_url, {"manager": "Jane Smith"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['manager'], "Jane Smith")

    def test_delete_fund(self):
        delete_url = reverse('fund:fund_d', args=[self.fund['data']['id']])
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
