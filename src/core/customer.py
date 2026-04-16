class Customer:
    """Stores customer information and their order history."""

    def __init__(self, customer_id: str, name: str, email: str):
        self._customer_id = customer_id
        self._name = name
        self._email = email
        self._orders: list = []

    # --- Getters (Encapsulation) ---
    @property
    def customer_id(self) -> str:
        return self._customer_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    def add_order(self, order):
        """Add a new order to the customer's order history."""
        self._orders.append(order)

    def get_orders(self) -> list:
        """Return a copy of the customer's orders."""
        return list(self._orders)

    def __str__(self) -> str:
        """Return a readable customer summary (name and email)."""
        return f"Customer: {self._name} | Email: {self._email}"
