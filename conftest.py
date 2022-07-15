import pytest
from django.contrib.auth.models import User
from rest_framework.templatetags.rest_framework import data

from base.models import Product, Order, OrderItem, ShippingAddress, Review


@pytest.fixture()
def new_user_factory(db):
    def create_app_user(
            username: str = None,
            password: str = None,
            first_name: str = "firstname",
            last_name: str = "lastname",
            email: str = "test@test.com",
            is_staff: str = False,
            is_superuser: str = False,
            is_active: str = True,

    ):
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,

        )
        return user

    return create_app_user


@pytest.fixture()
def new_user(db, new_user_factory):
    return new_user_factory("test@test.com", "test_password", "test_name")


@pytest.fixture()
def new_superuser(db, new_user_factory):
    return new_user_factory("test@test.com", "test_password", "test_name", is_staff="True", is_superuser="True",
                            is_active="True")


@pytest.fixture()
def create_product(db, new_user):
    new_product = Product.objects.create(
        user=new_user,
        name="test name",
        price=50,
        brand="test brand",
        countInStock=50,
        category="test category",
        description="this is test description"
    )
    return new_product


@pytest.fixture()
def create_review(db, new_user, create_product):
    new_review = Review.objects.create(
        user=new_user,
        product=create_product,
        name=User.username,
        rating=4,
        comment="test comment",
    )
    return new_review


@pytest.fixture()
def create_order(db, new_user):
    return Order.objects.create(
        user=new_user,
        paymentMethod='paypal',
        taxPrice=20,
        shippingPrice=100,
        totalPrice=120
    )


@pytest.fixture()
def create_shipping_address(db, create_order):
    return ShippingAddress.objects.create(
        order=create_order,
        address="mota gur",
        city="akko",
        postalCode=24256,
        country="israel",
    )


@pytest.fixture()
def create_order_item(db, create_order, create_product):
    return OrderItem.objects.create(
        product=create_product,
        order=create_order,
        name=Product.name,
        qty=3,
        price=30,
    )
