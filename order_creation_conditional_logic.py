class OnlineOrder:
    pass


class StoreOrder:
    pass


class PhoneOrder:
    pass


class OrderProcessor:
    ORDER_TYPES = {
        "online": OnlineOrder,
        "store": StoreOrder,
        "phone": PhoneOrder,
    }

    def create_order(self, order_type):
        order_class = self.ORDER_TYPES.get(order_type)

        if order_class is None:
            raise ValueError("Unknown order type")

        return order_class()
