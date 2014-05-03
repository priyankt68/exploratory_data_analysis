# states_ut,sub_centres,primary_health_centres,community_health_centres

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


x = pd.read_csv('num_of_scs_phcs.csv');

frame = pd.DataFrame(x)


print frame['states_ut'][:10];

print frame['community_health_centres'].value_counts;

#print frame['primary_health_centres'];