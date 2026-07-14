#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    if not isinstance(discount, int) or discount < 0 or discount > 100:
      print("Not valid discount")
      self.discount = 0
    else:
      self.discount = discount

    self.total = 0
    self.items = []
    self.previous_transactions = []

  def add_item(self, item, price, quantity=1):
    self.total += price * quantity
    for _ in range(quantity):
      self.items.append(item)

    self.previous_transactions.append({
      'item': item,
      'price': price,
      'quantity': quantity
    })

  def apply_discount(self):
    if not self.discount:
      print("There is no discount to apply.")
      return

    new_total = self.total * (100 - self.discount) / 100
    self.total = new_total

    # Format output without unnecessary .0 when whole number
    if isinstance(self.total, float) and self.total == int(self.total):
      display_total = int(self.total)
    else:
      display_total = self.total

    print(f"After the discount, the total comes to ${display_total}.")

  def void_last_transaction(self):
    if not self.previous_transactions:
      return

    last = self.previous_transactions.pop()
    amount = last['price'] * last['quantity']
    self.total -= amount

    # remove last added items for that transaction
    for _ in range(last['quantity']):
      if self.items:
        self.items.pop()
