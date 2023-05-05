from src.analyze_log import (func_quantid_never, func_never_was)
from collections import Counter

class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self) -> None:
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append((customer, order, day))

    def get_most_ordered_dish_per_customer(self, customer):
        result = [order[1] for order in self.orders if order[0] == customer]
        return max(result, key=result.count)

    def get_never_ordered_per_customer(self, customer):
        return func_quantid_never(customer, self.orders)

    def get_days_never_visited_per_customer(self, customer):
        return func_never_was(customer, self.orders)

    def get_busiest_day(self):
        days = [item[2] for item in self.orders]
        return Counter(days).most_common()[0][0]

    def get_least_busy_day(self):
        pass
