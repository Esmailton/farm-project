from uuid import uuid4
from django.test import TestCase
from django.urls import reverse
from apps.farm.tests.farm_base_test import FakeDataFactory
from apps.farm.models import Farm


class FarmUrlTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.farm = self.factory.create_farm()

    def test_farm_create_url(self):
        url_farm = reverse("farm:farm_create")
        self.assertEqual(url_farm, "/farm/create/")

    def test_farm_list_url(self):
        url_farm = reverse("farm:farm_list")
        self.assertEqual(url_farm, "/farm/list/")

    def test_farm_detail_url(self):
        farm_id = uuid4()
        url_farm_detail = reverse("farm:farm_detail", kwargs={"pk": farm_id})
        self.assertEqual(url_farm_detail, f"/farm/{farm_id}/detail/")

    def test_farm_update_url(self):
        farm_id = uuid4()
        url_farm_update = reverse("farm:farm_update", kwargs={"pk": farm_id})
        self.assertEqual(url_farm_update, f"/farm/{farm_id}/update/")

    def test_farm_delete_url(self):
        farm_id = uuid4()
        url_farm_update = reverse("farm:farm_delete", kwargs={"pk": farm_id})
        self.assertEqual(url_farm_update, f"/farm/{farm_id}/delete/")


class FarmViewsTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.farm = self.factory.create_farm()

    def test_farm_view_return_status_code_200(self):
        url = reverse("farm:farm_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_farm_view_create_method_post_return_status_code_200(self):
        url = reverse("farm:farm_create")
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_farm_detail_view_return_status_code_200(self):
        farm_id = Farm.objects.first().id
        url_farm_detail = reverse("farm:farm_detail", kwargs={"pk": farm_id})
        response = self.client.get(url_farm_detail)
        self.assertEqual(response.status_code, 200)

    def test_farm_detail_view_render_correct_template(self):
        farm_id = Farm.objects.first().id
        url = reverse("farm:farm_detail", kwargs={"pk": farm_id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, "farm/farm_detail.html")

    def test_farm_view_create_render_correct_template(self):
        url = reverse("farm:farm_create")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "farm/farm_form.html")

    def test_farm_view_update_render_correct_template(self):
        farm = Farm.objects.first()
        url = reverse("farm:farm_update", kwargs={"pk": farm.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, "farm/farm_form.html")

    def test_farm_detail_return_404(self):
        farm_id = uuid4()
        url_farm_detail = reverse("farm:farm_detail", kwargs={"pk": farm_id})
        response = self.client.get(url_farm_detail)
        self.assertEqual(response.status_code, 404)
