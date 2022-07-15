import pytest
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from base.models import Product, Review


def test_new_product_creation(create_product):
    count = Product.objects.all().count()
    assert count == 1


def test_product_creation(create_product):
    assert isinstance(create_product, Product) is True


def test_new_product_details(create_product):
    assert create_product.name == "test name"
    assert create_product.price == 50
    assert create_product.brand == "test brand"
    assert create_product.countInStock == 50
    assert create_product.category == "test category"
    assert create_product.description == "this is test description"


def test_delete_product(create_product):
    Product.delete(create_product)
    count = Product.objects.all().count()
    assert count == 0


def test_review_creation(create_review):
    count = Review.objects.all().count()
    assert count == 1


def test_review_details(create_review):
    assert create_review.name == User.username
    assert create_review.rating == 4
    assert create_review.comment == "test comment"


def test_delete_review(create_review):
    Review.delete(create_review)
    count = Review.objects.all().count()
    assert count == 0



# @pytest.mark.parametrize(
#     "name,price,brand,countInStock,category,description,validity",
#
#     ("productname", "0", "productbrand", "50", "productcategory", "nothing",True),
#
# )
# @pytest.mark.django_db
# def test_product_instance(name,price,brand,countInStock,category,description,validity):
#     form= RegistrationForm(
#     data={
#
#         "name" : name,
#         "price" : price,
#         "brand" : brand,
#         "countInStock" : countInStock,
#         "category" : category,
#         "description" : description,
#     },
#     )
#     assert form.is_valid() is validity

# Api test  - Integration testing
# def test_api_product_creation():
#     client = APIClient()
#     response = client.post("/api/products/create/")
#     # data = response.data
#     assert response.status_code == 200

# def test_exmp():
#     assert 1 == 1
