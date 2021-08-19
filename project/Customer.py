class Customer:
    """
    a single customer that moves through the supermarket in a MCMC simulation
    """
    import pandas as pd

    STATES = ['checkout', 'dairy', 'drinks', 'entrance', 'fruit', 'spices']
    TPM = pd.DataFrame(
        [[1.,         0.,         0.,         0.,         0.,         0.,       ],
        [0.10291054, 0.73720655, 0.05860497, 0.,         0.04987896, 0.05139898],
        [0.21595231, 0.01089526, 0.59831432, 0.,         0.08788159, 0.08695652],
        [0.00120741, 0.28722833, 0.15334049, 0.,         0.3769788,  0.18124497],
        [0.20160529, 0.09592383, 0.05484734, 0.,         0.59694681, 0.05067674],
        [0.15054963, 0.19324518, 0.16313526, 0.,         0.09096702, 0.40210292]], 
        index = STATES, 
        columns = STATES
        )
    
    def __init__(self, name, state, budget=100):
        self.name = name
        self.state = state
        self.budget = budget

    def __repr__(self):
        return f'<Customer {self.name} in {self.state}>'

    def is_active(self):
        """Returns True if the customer has not reached the checkout yet."""
        return self.state != 'checkout'

    def next_state(self):
        '''
        Propagates the customer to the next state.
        Returns nothing.
        '''
        import random
        transition_probs = list(Customer.TPM.loc[Customer.TPM.index==self.state].values[0])
        self.state = random.choices(Customer.STATES, weights=transition_probs)[0]

if __name__ == "__main__":
    c1 = Customer('J', 'entrance')
    c1.next_state()
    print(repr(c1))