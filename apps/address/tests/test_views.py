from uuid import uuid4
from django.test import TestCase
from django.urls import reverse
from .address_base_test import FakeDataFactory
from apps.address.models import Address


class AddressUrlTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.address = self.factory.create_address()

    def test_address_create_url(self):
        url_address = reverse("address:address_create")
        self.assertEqual(url_address, "/address/create/")

    def test_address_list_url(self):
        url_address = reverse("address:address_list")
        self.assertEqual(url_address, "/address/list/")

    def test_address_detail_url(self):
        address_id = uuid4()
        url_address_detail = reverse(
            "address:address_detail", kwargs={"pk": address_id}
        )
        self.assertEqual(url_address_detail, f"/address/{address_id}/detail/")

    def test_address_update_url(self):
        address_id = uuid4()
        url_address_update = reverse(
            "address:address_update", kwargs={"pk": address_id}
        )
        self.assertEqual(url_address_update, f"/address/{address_id}/update/")

    def test_address_delete_url(self):
        address_id = uuid4()
        url_address_update = reverse(
            "address:address_delete", kwargs={"pk": address_id}
        )
        self.assertEqual(url_address_update, f"/address/{address_id}/delete/")


class addressViewsTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.address = self.factory.create_address()

    def test_address_view_return_status_code_200(self):
        url = reverse("address:address_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_address_view_create_method_post_return_status_code_200(self):
        url = reverse("address:address_create")
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_address_detail_view_return_status_code_200(self):
        address_id = Address.objects.first().id
        url_address_detail = reverse(
            "address:address_detail", kwargs={"pk": address_id}
        )
        response = self.client.get(url_address_detail)
        self.assertEqual(response.status_code, 200)

    def test_address_detail_view_render_correct_template(self):
        address_id = Address.objects.first().id
        url = reverse("address:address_detail", kwargs={"pk": address_id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, "address/address_detail.html")

    def test_address_view_create_render_correct_template(self):
        url = reverse("address:address_create")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "address/address_form.html")

    def test_address_view_update_render_correct_template(self):
        address = Address.objects.all().last()
        url = reverse("address:address_update", kwargs={"pk": address.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, "address/address_form.html")

    def test_address_detail_return_404(self):
        address_id = uuid4()
        url_address_detail = reverse(
            "address:address_detail", kwargs={"pk": address_id}
        )
        response = self.client.get(url_address_detail)
        self.assertEqual(response.status_code, 404)
