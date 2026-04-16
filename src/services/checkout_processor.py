from core.order import Order

class CheckoutProcessor:
    """Handles the checkout process for the store."""

    def process_checkout(self, customer, cart, orders) -> Order:
        """Complete checkout: validate cart, reduce stock, create order, clear cart."""
        if cart.is_empty():
            raise ValueError("Cannot checkout with an empty cart.")

        # Reduce the stock of each product in the cart by the quantity purchased
        for item in cart.items:
            item.product.reduce_stock(item.quantity)

        order = Order(
            customer=customer,
            items=list(cart.items),
            total=cart.get_total(),
            shipping_total=cart.get_shipping_total(),
        )

        customer.add_order(order)
        orders.add_order(order)  # Use the correct method to add an order
        cart.clear()

        return order