class Supermarket:
    """manages multiple Customer instances that are currently in the market.
    """
    import pandas as pd
    from Customer import Customer

    def __init__(self):        
        # a list of Customer objects
        self.customers = []
        self.minutes = 0
        # self.last_id = 0 #?

    def __repr__(self):
        return f'It is {self.minutes} now, and there are {len(self.customers)} customers in the supermarket.'

    def get_time(self, current_time):
        """current time in HH:MM format,
        """
        self.minutes = current_time
        # current_time = pd.Timestamp.now().normalize()
        # self.minutes = current_time
        # print(current_time)
        return self.minutes

    def print_customers(self):
        """print all customers with the current time and id in CSV format.
        """
        for one_customer in self.customers:
            print(self.minutes,',', one_customer.name, ',', one_customer.state)
        return None

    def next_minute(self):
        """propagates all customers to the next state.
        """
        for one_customer in self.customers:
            one_customer.next_state()
        
        self.minutes = self.minutes
        return None
    
    def add_new_customers(self, one_customer):
        """randomly creates new customers.
        """
        self.customers.append(one_customer)
        return None

    def remove_exitsting_customers(self):
        """removes every customer that is not active any more.
        """
        for one_customer in self.customers:
            if one_customer.is_active() == False: 
                self.customers.remove(one_customer)
        return None