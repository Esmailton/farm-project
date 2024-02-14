from uuid import uuid4
from django.test import TestCase
from django.urls import reverse
from apps.workshop.tests.workshop_base_test import FakeDataFactory
from apps.workshop.models import Workshop


class WorkshopUrlTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.workshop = self.factory.create_workshop()

    def test_workshop_create_url(self):
        url_workshop = reverse("workshop:workshop_create")
        self.assertEqual(url_workshop, "/workshop/create/")

    def test_workshop_list_url(self):
        url_workshop = reverse("workshop:workshop_list")
        self.assertEqual(url_workshop, "/workshop/list/")

    def test_workshop_detail_url(self):
        workshop_id = uuid4()
        url_workshop_detail = reverse(
            "workshop:workshop_detail", kwargs={"pk": workshop_id}
        )
        self.assertEqual(url_workshop_detail, f"/workshop/{workshop_id}/detail/")

    def test_workshop_update_url(self):
        workshop_id = uuid4()
        url_workshop_update = reverse(
            "workshop:workshop_update", kwargs={"pk": workshop_id}
        )
        self.assertEqual(url_workshop_update, f"/workshop/{workshop_id}/update/")

    def test_workshop_delete_url(self):
        workshop_id = uuid4()
        url_workshop_update = reverse(
            "workshop:workshop_delete", kwargs={"pk": workshop_id}
        )
        self.assertEqual(url_workshop_update, f"/workshop/{workshop_id}/delete/")


class WorkshopViewsTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.workshop = self.factory.create_workshop()

    def test_workshop_view_return_status_code_200(self):
        url = reverse("workshop:workshop_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_workshop_view_create_method_post_return_status_code_200(self):
        url = reverse("workshop:workshop_create")
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_workshop_detail_view_return_status_code_200(self):
        workshop_id = Workshop.objects.first().id
        url_workshop_detail = reverse(
            "workshop:workshop_detail", kwargs={"pk": workshop_id}
        )
        response = self.client.get(url_workshop_detail)
        self.assertEqual(response.status_code, 200)

    def test_workshop_detail_view_render_correct_template(self):
        workshop_id = Workshop.objects.first().id
        url = reverse("workshop:workshop_detail", kwargs={"pk": workshop_id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, "workshop/workshop_detail.html")

    def test_workshop_view_create_render_correct_template(self):
        url = reverse("workshop:workshop_create")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "workshop/workshop_form.html")

    def test_workshop_view_update_render_correct_template(self):
        workshop = Workshop.objects.first()
        url = reverse("workshop:workshop_update", kwargs={"pk": workshop.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, "workshop/workshop_form.html")

    def test_workshop_detail_return_404(self):
        workshop_id = uuid4()
        url_workshop_detail = reverse(
            "workshop:workshop_detail", kwargs={"pk": workshop_id}
        )
        response = self.client.get(url_workshop_detail)
        self.assertEqual(response.status_code, 404)
