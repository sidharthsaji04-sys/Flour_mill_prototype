import time as t
class Mill:
     p_d = {'rice': {'mrp': 20, 'time': 2},
            'wheat': {'mrp': 10, 'time': 3},
            'ragi': {'mrp': 30, 'time': 2},
            'chilli': {'mrp': 40, 'time': 1},
            'coriander': {'mrp': 40, 'time': 2},
            'maize': {'mrp': 20, 'time': 4}}
     def __init__(self, name):
          self.name = name
          self.orders = []
          self.total_cost = []
          self.total_time = []
          self.total_orders = 0

     def user(self):
          print(f"Welcome to {self.name} mill")
          print('Items able to grind: rice, wheat, ragi, chilli, coriander, maize')
          time = []
          cost = []
          order = []
          current_order = {
               "items": [],
               "total_time": 0,
               "total_cost": 0
          }
          while True:
               item = input('Enter the material you have : ').strip().lower()
               order.append(item)

               if item in Mill.p_d:
                    values = Mill.p_d[item]
                    print(f"{item} is {values['mrp']} rupees only.")
                    print(f"Total grind time: {values['time']} minutes")
                    current_order["items"].append(item)
                    current_order["total_time"] += values["time"]
                    current_order["total_cost"] += values["mrp"]
                    cost.append(values["mrp"])
                    self.total_time.append(values["time"])
                    time.append(values["time"])
               else:
                    print(f"{item} is not available")


               nxt_item = input('do you want to add another item?(y/n) : ').strip().lower()
               if nxt_item == 'y':
                    continue
               elif nxt_item == 'n':
                    break
               else:
                    print('Please enter y for yes and n for no')

          self.orders.append(current_order)
          self.total_orders += 1

          if self.orders:
               total_time = sum(time)
               for x in order:
                    print(f"Order: {x}")
               print(f'Total cost: {sum(cost)} rupees')
               print(f"Total grind time: {total_time} minutes")
               self.total_orders+=1


     def order(self):
          while True:
               ord=input('Another order(y or n)?: ').strip().lower()
               if ord == 'y':
                    Mill.user(self)
               else:
                    break

          with open('mill orders', 'a') as f:
               f.write(f'{self.orders}\n')
               f.write(f'Total cost: {sum(order["total_cost"] for order in self.orders)} rupees\n')

     def timer(self):
          print(f'Total orders = {self.total_orders}')

          for i, order in enumerate(self.orders, start=1):
               print(f"\nProcessing Order {i}...")

               seconds = order["total_time"] * 60
               for ti in range(seconds, 0, -1):
                    minutes, sec = divmod(ti, 60)
                    print(f"Order {i} Time left: {minutes}:{sec:02d}")
                    t.sleep(1)
               print(f"\nOrder {i} completed!")
          print("\nAll orders completed. Thank you!")


mill=Mill('Walter')
mill.user()
mill.order()
mill.timer()
