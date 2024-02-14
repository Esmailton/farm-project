from uuid import uuid4
from django.test import TestCase
from django.urls import reverse
from apps.employee.tests.employee_base_test import FakeDataFactory
from apps.employee.models import Employee


class EmployeeUrlTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.employee = self.factory.create_employee()

    def test_employee_create_url(self):
        url_employee = reverse("employee:employee_create")
        self.assertEqual(url_employee, "/employee/create/")

    def test_employee_list_url(self):
        url_employee = reverse("employee:employee_list")
        self.assertEqual(url_employee, "/employee/list/")

    def test_employee_detail_url(self):
        employee_id = uuid4()
        url_employee_detail = reverse(
            "employee:employee_detail", kwargs={"pk": employee_id}
        )
        self.assertEqual(url_employee_detail, f"/employee/{employee_id}/detail/")

    def test_employee_update_url(self):
        employee_id = uuid4()
        url_employee_update = reverse(
            "employee:employee_update", kwargs={"pk": employee_id}
        )
        self.assertEqual(url_employee_update, f"/employee/{employee_id}/update/")

    def test_employee_delete_url(self):
        employee_id = uuid4()
        url_employee_update = reverse(
            "employee:employee_delete", kwargs={"pk": employee_id}
        )
        self.assertEqual(url_employee_update, f"/employee/{employee_id}/delete/")


class EmployeeViewsTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.employee = self.factory.create_employee()

    def test_employee_view_return_status_code_200(self):
        url = reverse("employee:employee_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_employee_view_create_method_post_return_status_code_200(self):
        url = reverse("employee:employee_create")
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_employee_detail_view_return_status_code_200(self):
        employee_id = Employee.objects.first().id
        url_employee_detail = reverse(
            "employee:employee_detail", kwargs={"pk": employee_id}
        )
        response = self.client.get(url_employee_detail)
        self.assertEqual(response.status_code, 200)

    def test_employee_detail_view_render_correct_template(self):
        employee_id = Employee.objects.first().id
        url = reverse("employee:employee_detail", kwargs={"pk": employee_id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, "employee/employee_detail.html")

    def test_employee_view_create_render_correct_template(self):
        url = reverse("employee:employee_create")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "employee/employee_form.html")

    def test_employee_view_update_render_correct_template(self):
        employee = Employee.objects.first()
        url = reverse("employee:employee_update", kwargs={"pk": employee.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, "employee/employee_form.html")

    def test_employee_detail_return_404(self):
        employee_id = uuid4()
        url_employee_detail = reverse(
            "employee:employee_detail", kwargs={"pk": employee_id}
        )
        response = self.client.get(url_employee_detail)
        self.assertEqual(response.status_code, 404)
