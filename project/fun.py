from Customer import Customer
from Supermarket import Supermarket
import pandas as pd
import numpy as np
import random

# -------------------- 
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
