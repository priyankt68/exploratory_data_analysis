# states_ut,sub_centres,primary_health_centres,community_health_centres

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mortality_records = pd.read_csv('imr.csv')
pop_density_records = pd.read_csv('pop_density_2011.csv')

for state in mortality_records['states_ut']:
	male_mortality = sum(mortality_records['m'])
	female_mortality = sum(mortality_records['f'])
	



per_state = ((mortality_records['m'] + mortality_records['f' ])/ (male_mortality + female_mortality)) * 100;


states_name = pd.Series(mortality_records['states_ut']);

x = pd.DataFrame({'states_ut':states_name,'state_imr_percent':per_state},columns=['states_ut','state_imr_percent']);
print x;

imr_pop_density = pd.merge(pop_density_records,x,on='states_ut')

imr_per_pop_density = pd.DataFrame({'states_ut':states_name,'imr_per_pop_d':np.round((imr_pop_density['state_imr_percent'] / 
						imr_pop_density['pop_density']),4)});

imr_per_pop_density.to_csv('imr_per_pop_density',sep=',',encoding='utf-8',index=False);









#per_state.columns = pd.MultiIndex.from_tuples(zip(['imr_percent'], per_state.columns))

#print per_state;
#statewise = np.round(statewise,4);
#states_ut =  np.array(mortality_records['states_ut']).reshape(35,1)
#print statewise.shape;
#print states_ut.shape;

#statewise_imr = (np.concatenate((states_ut,statewise),axis=0);

#print statewise_imr;





#states_ut = mortality_records['states_ut'];

#per_state_merged = (states_ut + per_state);

#print per_state_merged;

#print states_ut;

#per_state.index = mortality_records['states_ut'];

#imr_pop_density = pd.merge(per_state,pop_density_records);

#print imr_pop_density;








#print frame['primary_health_centres'];