"""Generate random dummy data for demo purposes"""

import string
import numpy as np
import pandas as pd

RAND_SEED = 42
NUM_ROWS = int(10.e6)
FILE_PATH = 'data/demo.csv'

# set random seed
np.random.seed(RAND_SEED)

# generate data
data = pd.DataFrame(data={'A': np.random.randint(0, 100, NUM_ROWS),
                          'B': np.random.choice(list(string.ascii_uppercase), NUM_ROWS),
                          'C': np.random.rand(NUM_ROWS),
                          'D': np.random.normal(100, 10, NUM_ROWS),
                          'E': np.random.exponential(10, NUM_ROWS)},
                    columns=['A', 'B', 'C', 'D', 'E'])

# store data
data.to_csv(FILE_PATH, index=False, header=True)
