from uuid import uuid4
from django.test import TestCase
from django.urls import reverse
from .vehicle_base_test import FakeDataFactory
from apps.vehicle.models import Vehicle, VehicleModel, Fleet, FleetCategory, Brand


class VehicleUrlTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.vehicle = self.factory.create_vehicle()

    def test_vehicle_create_url(self):
        url_vehicle = reverse("vehicle:vehicle_create")
        self.assertEqual(url_vehicle, "/vehicle/create/")

    def test_vehicle_list_url(self):
        url_vehicle = reverse("vehicle:vehicle_list")
        self.assertEqual(url_vehicle, "/vehicle/list/")

    def test_vehicle_detail_url(self):
        vehicle_id = uuid4()
        url_vehicle_detail = reverse(
            "vehicle:vehicle_detail", kwargs={"pk": vehicle_id}
        )
        self.assertEqual(url_vehicle_detail, f"/vehicle/{vehicle_id}/detail/")

    def test_vehicle_update_url(self):
        vehicle_id = uuid4()
        url_vehicle_update = reverse(
            "vehicle:vehicle_update", kwargs={"pk": vehicle_id}
        )
        self.assertEqual(url_vehicle_update, f"/vehicle/{vehicle_id}/update/")

    def test_vehicle_delete_url(self):
        vehicle_id = uuid4()
        url_vehicle_update = reverse(
            "vehicle:vehicle_delete", kwargs={"pk": vehicle_id}
        )
        self.assertEqual(url_vehicle_update, f"/vehicle/{vehicle_id}/delete/")


class BrandUrlTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.brand = self.factory.create_brand()

    def test_brand_create_url(self):
        url_brand = reverse("vehicle:brand_create")
        self.assertEqual(url_brand, "/brand/create/")

    def test_brand_list_url(self):
        url_brand = reverse("vehicle:brand_list")
        self.assertEqual(url_brand, "/brand/list/")

    def test_brand_detail_url(self):
        brand_id = uuid4()
        url_brand_detail = reverse("vehicle:brand_detail", kwargs={"pk": brand_id})
        self.assertEqual(url_brand_detail, f"/brand/{brand_id}/detail/")

    def test_brand_update_url(self):
        brand_id = uuid4()
        url_brand_update = reverse("vehicle:brand_update", kwargs={"pk": brand_id})
        self.assertEqual(url_brand_update, f"/brand/{brand_id}/update/")

    def test_brand_delete_url(self):
        brand_id = uuid4()
        url_brand_update = reverse("vehicle:brand_delete", kwargs={"pk": brand_id})
        self.assertEqual(url_brand_update, f"/brand/{brand_id}/delete/")


class FleetCategoryUrlTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.fleet_category = self.factory.create_fleet_category()

    def test_fleet_category_create_url(self):
        url_fleet_category = reverse("vehicle:fleet_category_create")
        self.assertEqual(url_fleet_category, "/fleet_category/create/")

    def test_fleet_category_list_url(self):
        url_fleet_category = reverse("vehicle:fleet_category_list")
        self.assertEqual(url_fleet_category, "/fleet_category/list/")

    def test_fleet_category_detail_url(self):
        fleet_category_id = uuid4()
        url_fleet_category_detail = reverse(
            "vehicle:fleet_category_detail", kwargs={"pk": fleet_category_id}
        )
        self.assertEqual(
            url_fleet_category_detail, f"/fleet_category/{fleet_category_id}/detail/"
        )

    def test_fleet_category_update_url(self):
        fleet_category_id = uuid4()
        url_fleet_category_update = reverse(
            "vehicle:fleet_category_update", kwargs={"pk": fleet_category_id}
        )
        self.assertEqual(
            url_fleet_category_update, f"/fleet_category/{fleet_category_id}/update/"
        )

    def test_fleet_category_delete_url(self):
        fleet_category_id = uuid4()
        url_fleet_category_update = reverse(
            "vehicle:fleet_category_delete", kwargs={"pk": fleet_category_id}
        )
        self.assertEqual(
            url_fleet_category_update, f"/fleet_category/{fleet_category_id}/delete/"
        )


class FleetUrlTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.fleet = self.factory.create_fleet()

    def test_fleet_create_url(self):
        url_fleet = reverse("vehicle:fleet_create")
        self.assertEqual(url_fleet, "/fleet/create/")

    def test_fleet_list_url(self):
        url_fleet = reverse("vehicle:fleet_list")
        self.assertEqual(url_fleet, "/fleet/list/")

    def test_fleet_detail_url(self):
        fleet_id = uuid4()
        url_fleet_detail = reverse("vehicle:fleet_detail", kwargs={"pk": fleet_id})
        self.assertEqual(url_fleet_detail, f"/fleet/{fleet_id}/detail/")

    def test_fleet_update_url(self):
        fleet_id = uuid4()
        url_fleet_update = reverse("vehicle:fleet_update", kwargs={"pk": fleet_id})
        self.assertEqual(url_fleet_update, f"/fleet/{fleet_id}/update/")

    def test_fleet_delete_url(self):
        fleet_id = uuid4()
        url_fleet_update = reverse("vehicle:fleet_delete", kwargs={"pk": fleet_id})
        self.assertEqual(url_fleet_update, f"/fleet/{fleet_id}/delete/")


class VehicleModelUrlTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.vehicle_model = self.factory.create_vehicle_model()

    def test_vehicle_model_create_url(self):
        url_vehicle_model = reverse("vehicle:vehicle_model_create")
        self.assertEqual(url_vehicle_model, "/vehicle_model/create/")

    def test_vehicle_model_list_url(self):
        url_vehicle_model = reverse("vehicle:vehicle_model_list")
        self.assertEqual(url_vehicle_model, "/vehicle_model/list/")

    def test_vehicle_model_detail_url(self):
        vehicle_model_id = uuid4()
        url_vehicle_model_detail = reverse(
            "vehicle:vehicle_model_detail", kwargs={"pk": vehicle_model_id}
        )
        self.assertEqual(
            url_vehicle_model_detail, f"/vehicle_model/{vehicle_model_id}/detail/"
        )

    def test_vehicle_model_update_url(self):
        vehicle_model_id = uuid4()
        url_vehicle_model_update = reverse(
            "vehicle:vehicle_model_update", kwargs={"pk": vehicle_model_id}
        )
        self.assertEqual(
            url_vehicle_model_update, f"/vehicle_model/{vehicle_model_id}/update/"
        )

    def test_vehicle_model_delete_url(self):
        vehicle_model_id = uuid4()
        url_vehicle_model_update = reverse(
            "vehicle:vehicle_model_delete", kwargs={"pk": vehicle_model_id}
        )
        self.assertEqual(
            url_vehicle_model_update, f"/vehicle_model/{vehicle_model_id}/delete/"
        )


class VehicleViewsTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.vehicle = self.factory.create_vehicle()

    def test_vehicle_view_return_status_code_200(self):
        url = reverse("vehicle:vehicle_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_vehicle_view_create_method_post_return_status_code_200(self):
        url = reverse("vehicle:vehicle_create")
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_vehicle_detail_view_return_status_code_200(self):
        vehicle_id = Vehicle.objects.first().id
        url_vehicle_detail = reverse(
            "vehicle:vehicle_detail", kwargs={"pk": vehicle_id}
        )
        response = self.client.get(url_vehicle_detail)
        self.assertEqual(response.status_code, 200)

    def test_vehicle_detail_view_render_correct_template(self):
        vehicle_id = Vehicle.objects.first().id
        url = reverse("vehicle:vehicle_detail", kwargs={"pk": vehicle_id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, "vehicle/vehicle_detail.html")

    def test_vehicle_view_create_render_correct_template(self):
        url = reverse("vehicle:vehicle_create")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "vehicle/vehicle_form.html")

    def test_vehicle_view_update_render_correct_template(self):
        vehicle = Vehicle.objects.all().last()
        url = reverse("vehicle:vehicle_update", kwargs={"pk": vehicle.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, "vehicle/vehicle_form.html")

    def test_vehicle_detail_return_404(self):
        vehicle_id = uuid4()
        url_vehicle_detail = reverse(
            "vehicle:vehicle_detail", kwargs={"pk": vehicle_id}
        )
        response = self.client.get(url_vehicle_detail)
        self.assertEqual(response.status_code, 404)


class VehicleModelViewsTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.vehicle_model = self.factory.create_vehicle_model()

    def test_vehicle_model_view_return_status_code_200(self):
        url = reverse("vehicle:vehicle_model_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_vehicle_model_view_create_method_post_return_status_code_200(self):
        url = reverse("vehicle:vehicle_model_create")
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_vehicle_model_detail_view_return_status_code_200(self):
        vehicle_model_id = VehicleModel.objects.first().id
        url_vehicle_model_detail = reverse(
            "vehicle:vehicle_model_detail", kwargs={"pk": vehicle_model_id}
        )
        response = self.client.get(url_vehicle_model_detail)
        self.assertEqual(response.status_code, 200)

    def test_vehicle_model_detail_view_render_correct_template(self):
        vehicle_model_id = VehicleModel.objects.first().id
        url = reverse("vehicle:vehicle_model_detail", kwargs={"pk": vehicle_model_id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, "vehicle_model/vehicle_model_detail.html")

    def test_vehicle_model_view_create_render_correct_template(self):
        url = reverse("vehicle:vehicle_model_create")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "vehicle_model/vehicle_model_form.html")

    def test_vehicle_model_view_update_render_correct_template(self):
        vehicle_model = VehicleModel.objects.all().last()
        url = reverse("vehicle:vehicle_model_update", kwargs={"pk": vehicle_model.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, "vehicle_model/vehicle_model_form.html")

    def test_vehicle_model_detail_return_404(self):
        vehicle_model_id = uuid4()
        url_vehicle_model_detail = reverse(
            "vehicle:vehicle_model_detail", kwargs={"pk": vehicle_model_id}
        )
        response = self.client.get(url_vehicle_model_detail)
        self.assertEqual(response.status_code, 404)


class FleetViewsTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.fleet = self.factory.create_fleet()

    def test_fleet_view_return_status_code_200(self):
        url = reverse("vehicle:fleet_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_fleet_view_create_method_post_return_status_code_200(self):
        url = reverse("vehicle:fleet_create")
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_fleet_detail_view_return_status_code_200(self):
        fleet_id = Fleet.objects.first().id
        url_fleet_detail = reverse("vehicle:fleet_detail", kwargs={"pk": fleet_id})
        response = self.client.get(url_fleet_detail)
        self.assertEqual(response.status_code, 200)

    def test_fleet_detail_view_render_correct_template(self):
        fleet_id = Fleet.objects.first().id
        url = reverse("vehicle:fleet_detail", kwargs={"pk": fleet_id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, "fleet/fleet_detail.html")

    def test_fleet_view_create_render_correct_template(self):
        url = reverse("vehicle:fleet_create")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "fleet/fleet_form.html")

    def test_fleet_view_update_render_correct_template(self):
        fleet = Fleet.objects.all().last()
        url = reverse("vehicle:fleet_update", kwargs={"pk": fleet.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, "fleet/fleet_form.html")

    def test_fleet_detail_return_404(self):
        fleet_id = uuid4()
        url_fleet_detail = reverse("vehicle:fleet_detail", kwargs={"pk": fleet_id})
        response = self.client.get(url_fleet_detail)
        self.assertEqual(response.status_code, 404)


class FleetCategoryViewsTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.fleet_category = self.factory.create_fleet_category()

    def test_fleet_category_view_return_status_code_200(self):
        url = reverse("vehicle:fleet_category_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_fleet_category_view_create_method_post_return_status_code_200(self):
        url = reverse("vehicle:fleet_category_create")
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_fleet_category_detail_view_return_status_code_200(self):
        fleet_category_id = FleetCategory.objects.first().id
        url_fleet_category_detail = reverse(
            "vehicle:fleet_category_detail", kwargs={"pk": fleet_category_id}
        )
        response = self.client.get(url_fleet_category_detail)
        self.assertEqual(response.status_code, 200)

    def test_fleet_category_detail_view_render_correct_template(self):
        fleet_category_id = FleetCategory.objects.first().id
        url = reverse("vehicle:fleet_category_detail", kwargs={"pk": fleet_category_id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, "fleet_category/fleet_category_detail.html")

    def test_fleet_category_view_create_render_correct_template(self):
        url = reverse("vehicle:fleet_category_create")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "fleet_category/fleet_category_form.html")

    def test_fleet_category_view_update_render_correct_template(self):
        fleet_category = FleetCategory.objects.all().last()
        url = reverse("vehicle:fleet_category_update", kwargs={"pk": fleet_category.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, "fleet_category/fleet_category_form.html")

    def test_fleet_category_detail_return_404(self):
        fleet_category_id = uuid4()
        url_fleet_category_detail = reverse(
            "vehicle:fleet_category_detail", kwargs={"pk": fleet_category_id}
        )
        response = self.client.get(url_fleet_category_detail)
        self.assertEqual(response.status_code, 404)


class BrandViewsTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.fleet_category = self.factory.create_brand()

    def test_brand_view_return_status_code_200(self):
        url = reverse("vehicle:brand_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_brand_view_create_method_post_return_status_code_200(self):
        url = reverse("vehicle:brand_create")
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_brand_detail_view_return_status_code_200(self):
        brand_id = Brand.objects.first().id
        url_brand_detail = reverse("vehicle:brand_detail", kwargs={"pk": brand_id})
        response = self.client.get(url_brand_detail)
        self.assertEqual(response.status_code, 200)

    def test_brand_detail_view_render_correct_template(self):
        brand_id = Brand.objects.first().id
        url = reverse("vehicle:brand_detail", kwargs={"pk": brand_id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, "brand/brand_detail.html")

    def test_brand_view_create_render_correct_template(self):
        url = reverse("vehicle:brand_create")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "brand/brand_form.html")

    def test_brand_view_update_render_correct_template(self):
        brand = Brand.objects.all().last()
        url = reverse("vehicle:brand_update", kwargs={"pk": brand.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, "brand/brand_form.html")

    def test_brand_detail_return_404(self):
        brand_id = uuid4()
        url_brand_detail = reverse("vehicle:brand_detail", kwargs={"pk": brand_id})
        response = self.client.get(url_brand_detail)
        self.assertEqual(response.status_code, 404)
