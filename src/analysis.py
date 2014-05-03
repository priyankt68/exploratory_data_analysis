import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mortality_records = pd.read_csv('data/input_data/imr.csv')
pop_density_records = pd.read_csv('data/input_data/pop_density_2011.csv')

for state in mortality_records['states_ut']:
	male_mortality = sum(mortality_records['m'])
	female_mortality = sum(mortality_records['f'])

per_state = ((mortality_records['m'] + mortality_records['f' ])/ (male_mortality + female_mortality)) * 100;

states_name = pd.Series(mortality_records['states_ut']);

x = pd.DataFrame({'states_ut':states_name,'state_imr_percent':per_state},columns=['states_ut','state_imr_percent']);

imr_pop_density = pd.merge(pop_density_records,x,on='states_ut')

imr_per_pop_density = pd.DataFrame({'states_ut':states_name,'imr_per_pop_d':np.round((imr_pop_density['state_imr_percent'] / 
						imr_pop_density['pop_density']),4)});

imr_per_pop_density.to_csv('../data/output_data/imr_per_pop_density.csv',sep=',',encoding='utf-8',index=False);


