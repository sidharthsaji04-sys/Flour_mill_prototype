import json as js
import tkinter as tk
from tkinter import messagebox

class Order:
     p_d = {'rice': {'mrp': 20, 'time': 2},
            'wheat': {'mrp': 10, 'time': 3},
            'ragi': {'mrp': 30, 'time': 2},
            'chilli': {'mrp': 40, 'time': 1},
            'coriander': {'mrp': 40, 'time': 2},
            'maize': {'mrp': 20, 'time': 4}}

     def __init__(self):
          self.items = []
          self.total_cost = 0
          self.total_time = 0
          self.weights = []

     def add_item(self, item, weight_kg):
          if item in Order.p_d:
               self.weights.append(weight_kg)
               self.items.append(item)
               self.total_cost += Order.p_d[item]['mrp'] * weight_kg
               self.total_time += Order.p_d[item]['time'] * weight_kg
               return True
          else:
               return False

     def to_dict(self):
          return {
               'item':self.items,
               'weight':self.weights ,
               'total_cost': self.total_cost,
               'total_time': self.total_time
          }

     def save_data(self):
             new_data = self.to_dict()

             try:
                 with open('data.json', 'r') as f:
                     existing_data = js.load(f)

                     if not isinstance(existing_data, list):
                         existing_data = []
             except:
                 existing_data = []

             existing_data.append(new_data)

             with open('data.json', 'w') as f:
                 js.dump(existing_data, f, indent=4)

     def load_data(self):
         try:
             return self.to_dict()
         except:
             return f'No data found'


root = tk.Tk()
root.title('Mill app')
item_entry= tk.Entry(root,width=50)
tk.Label(root, text="Item").pack()
item_entry.pack()
weight_entry = tk.Entry(root,width=50)
tk.Label(root, text="Weight (kg)").pack()
weight_entry.pack()
output=tk.Text(root,height=10,width=55)
output.pack()
time_output=tk.Text(root,height=1,width=10)
tk.Label(root,text='Timer').pack()
time_output.pack()
output.insert(tk.END,'WELCOME TO KALAKKODE FLOUR MILL🏭\n')
order = Order()


def add_item():
    try:
        item = item_entry.get().strip().lower()
    except ValueError:
        output.insert(tk.END,'Invalid item\n')
        return
    try:
         weight = float(weight_entry.get().strip().lower())
    except ValueError:
        output.insert(tk.END,'Invalid weight\n')
        return

    if order.add_item(item, weight):
        output.insert(tk.END,f'Added {item} - {weight} kg\n')
        order.save_data()
    else:
        output.insert(tk.END,'Item is not available\n')

    item_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)

def exit():
    root.destroy()

def summary():
    if order.items:
        output.insert(tk.END, f'Total cost: {order.total_cost} rupees\n')
        output.insert(tk.END, f'Total time: {order.total_time} minutes\n')
        output.insert(tk.END, f'{order.load_data()}\n')
    else:
        messagebox.showinfo('summary', 'order is not placed')

def timer():
    if not order.items:
        messagebox.showinfo('timer', 'No order placed yet\n')
        return

    global _timer_job, _remaining_seconds

    if _timer_job is not None:
        return
    item_entry.config(state='disabled')
    weight_entry.config(state='disabled')

    _remaining_seconds = int(round(order.total_time * 60))
    if _remaining_seconds <= 0:
        time_output.delete("1.0", tk.END)
        time_output.insert(tk.END, "0:00")
        return

    def _tick():
        global _timer_job, _remaining_seconds
        minutes, seconds = divmod(_remaining_seconds, 60)
        time_output.delete("1.0", tk.END)
        time_output.insert(tk.END, f"{minutes}:{seconds:02d}")

        _remaining_seconds -= 1
        if _remaining_seconds >= 0:
            _timer_job = root.after(1000, _tick)
        else:
            messagebox.showinfo('order ready', 'your order is ready!')
            _timer_job = None
            item_entry.config(state='normal')
            weight_entry.config(state='normal')


    _tick()

_timer_job = None
_remaining_seconds = 0

button1 = tk.Button(root, text='Add Item ', command=add_item,height=1, width=10)
button1.pack()
button2 = tk.Button(root, text='Summary ', command=summary,height=1, width=10)
button2.pack()
button3=tk.Button(root,text='exit',command=exit,height=1, width=10)
button3.pack()
button4=tk.Button(root,text='Click to start processing',command=timer,height=1, width=20)
button4.pack()
root.mainloop()





