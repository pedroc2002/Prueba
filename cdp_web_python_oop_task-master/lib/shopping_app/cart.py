class Cart:
    from ownable import set_owner
    from item_manager import show_items

    def __init__(self, owner):
        self.set_owner(owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self, seller):
        total_amount = self.total_amount()

        if self.owner.wallet.balance < total_amount:
            print("No fondos suficientes")
            return

        self.owner.wallet.withdraw(total_amount)    
        seller.wallet.deposit(total_amount)

        for item in self.items:
            item.set_owner(self.owner)

        self.items = []