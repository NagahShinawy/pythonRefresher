class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    @classmethod
    def franchise(cls):
        print(f"{cls.__name__} - franchise")

    def stock_price(self):
        return sum([item["price"] for item in self.items])

    def store_details(self):
        """
        :param self: Store obj, subclass of Store
        :return:
        """
        print(
            "Store: {} with Stock {} ".format(
                self.__class__.__name__, self.stock_price()
            )
        )


class Souq(Store):
    pass


class Amazon(Store):
    pass


if __name__ == "__main__":
    test = Store("test")
    test.add_item(name="mac", price=20)
    test.add_item(name="huawei", price=40)
    test.add_item(name="hp", price=30)
    print(test.stock_price())
    Store.franchise()
    Souq.franchise()
    sq = Souq("Souq")
    amazon = Amazon("Amazon")
    Amazon.franchise()
    test.store_details()
    sq.store_details()
    amazon.store_details()
