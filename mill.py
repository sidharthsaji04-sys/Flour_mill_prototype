import time as t
p_d={'rice':{'mrp':20,'time':2},
     'wheat':{'mrp':10,'time':3},
     'ragi':{'mrp':30,'time':2},
     'chilli':{'mrp':40,'time':1},
     'coriander':{'mrp':40,'time':2},
     'maize':{'mrp':20,'time':4}}

order=[]
time=[]

class Mill:
     def __init__(self,name):
          self.name = name
     def user(self):
          global order, time
          print(f"Welcome to {self.name} mill")
          print('Items able to grind: rice, wheat, ragi, chilli, coriander, maize')

          while True:
               item = input('Enter the material you have : ').strip().lower()

               if item in p_d:
                    values = p_d[item]
                    print(f"{item} is {values['mrp']} rupees only.")
                    order.append((item, values["mrp"]))
                    time.append(values["time"])
                    t.sleep(values["time"])
               else:
                    print(f"{item} is not available")

               nxt_item = input('do you want to add another item?(y/n) : ').strip().lower()
               if nxt_item == 'y':
                    continue
               elif nxt_item == 'n':
                    break
               else:
                    print('Please enter y for yes and n for no')

          if order:
               total_cost = sum(price for _, price in order)
               total_time = sum(time)
               print(f"Order: {order}")
               print(f"Total cost: {total_cost} rupees")
               print(f"Total grind time: {total_time} minutes")
               with open('mill orders', 'a') as f:
                    f.write(f'{order}\n')
                    f.write(f'Total cost: {total_cost} rupees\n')

     def timer(self):
          global time
          seconds = sum(time) * 60
          for ti in range(seconds, 0, -1):
               minutes, seconds = divmod(ti, 60)
               print(f"Time left: {minutes}:{seconds}")
               t.sleep(1)
          print('Your order is ready to pick up')
          print('Thank you for your time')

mill=Mill('Walter')
mill.user()
mill.timer()
