import pytest
from base.models import Product, Order, ShippingAddress, OrderItem


def test_new_order_creation(create_order):
    count = Order.objects.all().count()
    assert count == 1


def test_porder_creation(create_order):
    assert isinstance(create_order, Order) is True


def test_new_order_details(create_order):
    assert create_order.user.first_name == "test_name"
    assert create_order.paymentMethod == "paypal"
    assert create_order.taxPrice == 20
    assert create_order.shippingPrice == 100
    assert create_order.totalPrice == 120


def test_delete_order(create_order):
    Order.delete(create_order)
    count = Order.objects.all().count()
    assert count == 0


def test_shipping_address_creation(create_shipping_address):
    count = ShippingAddress.objects.all().count()
    assert count == 1


def test_shipping_address_details(create_shipping_address):
    assert create_shipping_address.address == "mota gur"
    assert create_shipping_address.city == "akko"
    assert create_shipping_address.postalCode == 24256
    assert create_shipping_address.country == "israel"


def test_delete_shipping_address(create_shipping_address):
    ShippingAddress.delete(create_shipping_address)
    count = ShippingAddress.objects.all().count()
    assert count == 0


def test_order_item_creation(create_order_item):
    count = OrderItem.objects.all().count()
    assert count == 1


def test_order_item_details(create_order_item):
    assert create_order_item.name==Product.name
    assert create_order_item.qty==3
    assert create_order_item.price==30


def test_delete_order_item(create_order_item):
    OrderItem.delete(create_order_item)
    count = OrderItem.objects.all().count()
    assert count == 0