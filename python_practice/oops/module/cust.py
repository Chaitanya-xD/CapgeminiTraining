import random

class customers:
  def __init__(self, name):
    self.orders = {}
    self.customer_name = name

  def add(self, id, item):
    self.orders[id] = [item]

class order_id:
  def id(self):
    return random.randrange(10000,100000)
