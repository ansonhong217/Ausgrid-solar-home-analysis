# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 11:34:37 2020

@author: TAM048
"""
# 4) PV versus load analysis
# capacity against load size annually, scatter plot and frequency histogram

#find the load type: PV/load consumption
PV_solar_data=solar_data[PV_loadtype];
load_solar_data=solar_data[GL_loadtype|CL_loadtype];

#PV: find the capacity of each customer
#Load: find the average daily consumption over the year 
group_PV=(PV_solar_data.groupby('Customer')['Generator Capacity']).mean();  group_PV.name='PV Capacity (kWp)';
group_load=(load_solar_data.groupby('Customer')[time_series]).mean().sum(axis=1); group_load.name='Load (kWh)';
Load_vs_capacity = pd.merge(group_PV, group_load, right_index = True, 
               left_index = True)

#scatter plot to study relationship between PV capacity and load size
scp = Load_vs_capacity.plot.scatter(y='PV Capacity (kWp)', x='Load (kWh)');

#frequency histogram plot
N_sqrt=math.ceil(No_of_customer**0.5);#No_of_bin for histogram
Load_vs_capacity.hist(bins=N_sqrt);plt.show()

#Mean load for each custer during season
solar_home_load=(solar_data[GL_loadtype|CL_loadtype]).groupby(['Customer','date'])[time_series];
solar_home_PV=(solar_data[PV_loadtype].groupby(['Customer','date']))[time_series];

load_by_customer_by_day=solar_home_load.sum().sum(axis=1);
PV_by_customer_by_day=solar_home_PV.sum().sum(axis=1);

load_by_customer_by_day.name='Daily Load (kWh)';
PV_by_customer_by_day.name='Daily PV Generation (kWh)';

N_customer_days=len(PV_by_customer_by_day);
N_sqrt=math.ceil(N_customer_days**0.5);#No_of_bin for histogram

#histogram for load
plt.hist(load_by_customer_by_day,bins=N_sqrt);
plt.xlabel('Daily Load (kWh)');
plt.ylabel('No of Customer Days');
plt.title('Histogram for No. of Customer Days versus Load Consumption');
plt.show();

#histogram for PV
plt.hist(PV_by_customer_by_day,bins=N_sqrt,color='orange');
plt.xlabel('Daily PV Generation (kWh)');
plt.ylabel('No of Customer Days');
plt.title('Histogram for No. of Customer Days versus PV Generation');  
plt.show();

#Combine two histograms together
plt.hist(load_by_customer_by_day,bins=N_sqrt,alpha=0.5,label='Load Consumption');
plt.hist(PV_by_customer_by_day,bins=N_sqrt,alpha=0.5,label='PV Generation');
plt.xlabel('Daily Energy (kWh)');
plt.ylabel('No of Customer Days');
plt.xlim(0, 100)
plt.legend()
plt.title('Comparison of No. of Customer Days between Load Consumption and PV Generation');
                      

    