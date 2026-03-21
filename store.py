from order import Order


class Store:
    """
    Central class that manages the product catalog and processes checkouts.

    Responsibilities (Single Responsibility kept per class):
      - Maintain the catalog of available products.
      - Process the checkout: validate the cart, reduce stock, create an Order.
    """

    def __init__(self, name: str):
        """Create a store with a name, empty catalog, and empty order list."""
        self._name = name
        self._catalog: dict = {}  # product_id -> Product
        self._orders: list = []

    @property
    def name(self) -> str:
        """Return the store name."""
        return self._name

    # --- Catalog management ---

    def add_product(self, product):
        """Add or replace a product in the catalog by product_id."""
        self._catalog[product.product_id] = product

    def get_product(self, product_id: str):
        """Return one product by id, or raise an error if not found."""
        if product_id not in self._catalog:
            raise ValueError(f"Product '{product_id}' not found in catalog.")
        return self._catalog[product_id]

    def list_products(self) -> list:
        """Return all catalog products as a list."""
        return list(self._catalog.values())

    def display_catalog(self):
        """Print the catalog in a readable format."""
        print(f"\n{'=' * 55}")
        print(f"  {self._name} — Product Catalog")
        print(f"{'=' * 55}")
        for product in self._catalog.values():
            print(f"  [{product.product_id}] {product.get_info()}")
        print(f"{'=' * 55}\n")

    # --- Checkout ---

    def checkout(self, customer, cart) -> Order:
        """Complete checkout: validate cart, reduce stock, create order, clear cart."""
        if cart.is_empty():
            raise ValueError("Cannot checkout with an empty cart.")

        for item in cart.items:
            item.product.reduce_stock(item.quantity)

        order = Order(
            customer=customer,
            items=list(cart.items),
            total=cart.get_total(),
            shipping_total=cart.get_shipping_total(),
        )

        customer.add_order(order)
        self._orders.append(order)
        cart.clear()

        return order

    # --- Order history ---

    def get_all_orders(self) -> list:
        """Return a copy of all orders created in this store."""
        return list(self._orders)
