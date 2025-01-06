from django.test import TestCase
from django.contrib.auth import get_user_model
from inventory.models import (
    Category,
    Supplier,
    Product,
    Order,
    OrderItem,
    InventoryHistory,
)

User = get_user_model()  # Ensures the custom User model is referenced


class TestOrderModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.order = Order.objects.create(
            user=self.user, order_type="sale", total_amount=100.00
        )

    def test_order_creation(self):
        self.assertEqual(self.order.user, self.user)
        self.assertEqual(self.order.total_amount, 100.00)
        self.assertEqual(self.order.status, "pending")


class TestOrderItemModel(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(
            name="Laptop",
            price=1500.00,
            stock_quantity=10,
            threshold=5,
            category=self.category,
        )
        self.user = User.objects.create_user(username="testuser", password="password")
        self.order = Order.objects.create(
            user=self.user, order_type="sale", total_amount=0.00
        )

    def test_order_item_creation(self):
        order_item = OrderItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=2,
            price_at_purchase=1500.00,
        )
        self.assertEqual(order_item.product.name, "Laptop")
        self.assertEqual(order_item.quantity, 2)
        self.assertEqual(self.product.stock_quantity, 8)


class TestInventoryHistoryModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.category = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(
            name="Laptop",
            price=1500.00,
            stock_quantity=10,
            threshold=5,
            category=self.category,
        )
        self.history = InventoryHistory.objects.create(
            product=self.product,
            user=self.user,
            action="add",
            quantity_changed=5,
        )

    def test_inventory_history_creation(self):
        self.assertEqual(str(self.history), "Laptop - add by testuser")
        self.assertEqual(self.history.action, "add")
        self.assertEqual(self.history.quantity_changed, 5)
