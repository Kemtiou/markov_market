from Customer import Customer
from Supermarket import Supermarket
import pandas as pd
import numpy as np
import random

# -------------------- test one customer
c1 = Customer('J', 'entrance')
c1.next_state()
print(repr(c1))

# -------------------- test supermarket with one customer

# # instanciate Supermarket
# s = Supermarket('2021-09-17 07:00:00')
# # instanciate one customer
# c1 = Customer('Billy', 'entrance')
# c2 = Customer('Willy', 'entrance')
# # add the customer to the supermarket
# s.add_new_customers(c1)
# s.add_new_customers(c2)
# # time ticks for 15 minutes in 1 min frequency
# t_open = pd.Timestamp('2021-09-17 07:00:00')
# t_close = pd.Timestamp('2021-09-17 07:15:00')
# for t in pd.date_range(start=t_open, end=t_close, freq='min'):
#     if c1 in s.customers: # if customer still in supermarket customer list
#         if c1.is_active() == False: # if customer is at checkout then remove
#             s.remove_exitsting_customers(c1) #    
#         if c1.is_active: # only if customer not at checkout then next state 
#             c1.next_state()
#     if c2 in s.customers: # if customer still in supermarket customer list
#         if c2.is_active() == False: # if customer is at checkout then remove
#             s.remove_exitsting_customers(c2) #    
#         if c2.is_active: # only if customer not at checkout then next state 
#             c2.next_state()
#     print(s.customers)
# # nice ! but not smart with increasing customers and entering time not defined

# --------------------- How about using customer_no and entering time in the data? How?
# df = pd.read_csv('../data/monday.csv', sep=';', parse_dates=True, index_col=[0])
# print(df.head(5))


# time ticks for 15 minutes in 1 min frequency
# try something easier : according to data roughly 100 customers entering per hour
# start and end of simulation
t_open = pd.Timestamp('2021-09-17 07:00:00')
t_close = pd.Timestamp('2021-09-17 07:15:00')
# instanciate supermarkt
s = Supermarket()
# instanciate customer_no
customer_no = 1
for t in pd.date_range(start=t_open, end=t_close, freq='min'):
    # update time
    s.get_time(t)

    # add entering customers 
    n = round(np.random.normal(1.7, 1)) # around 100/hour normalized distribution 
    if n > 0: 
        for i in range(n):
            c = Customer(str(customer_no), 'entrance')
            # add new customers to the supermarket
            s.add_new_customers(c)
            customer_no += 1

    # remove customers at checkout
    s.remove_exitsting_customers()

    # update customer next state
    s.next_minute()
    
    #s.print_customers()
    print(repr(s))





#---- more fun/complicated if:
# - customers behaviors were generated from different mc models 
# - analyze entering hourly profile apply to model
#---- questions : 
# - rule for customer enter
# - rule for mapping state into coordinate/block shown in project figure
# - wired difference between .py and .ipynb when code is identical