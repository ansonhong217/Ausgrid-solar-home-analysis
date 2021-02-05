# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 13:45:09 2020

@author: TAM048
"""
# 1)hour-wise analysis 
# x-axis: 48 time instants of a day
# y-axis: Normalised energy of load/PV
# boxplot: variation of 300 customers 


#Group by Customer
solar_home_load=(solar_data[GL_loadtype|CL_loadtype]).groupby('Customer')[time_series];
solar_home_PV=(solar_data[PV_loadtype].groupby('Customer'))[time_series];

#Step 1:
#Find the half-hourly average Load Consumption/maximum PV generation for each customer over the whole year
#Firstly sum all energy over the whole year at each time instant 
#Secondly find the mean(for load)/max(for PV) over a day
#Lastly scaling the data by dividing by No. of days of a year  
mean_load=solar_home_load.sum().mean(axis=1)/No_of_days_year;
max_PV=solar_home_PV.sum().max(axis=1)/No_of_days_year;

days_count=0;
for specific_season in season:
    
    load_data_season=solar_data[specific_season & (GL_loadtype | CL_loadtype)];
    PV_data_season=solar_data[specific_season & PV_loadtype];
    
    load_by_customer=load_data_season.groupby('Customer')[time_series];
    PV_by_customer=PV_data_season.groupby('Customer')[time_series];
    
    #dataframe for boxplot
    #Similar to step 1
    #Firstly find the total energy for each customer over a specific season
    #Then normalised by value found in Step 1, 
    #Lastlyscaling the data by No. of days of a season
    Norm_load_by_customer=(load_by_customer.sum()/No_of_days_season[days_count])/np.array(mean_load)[:,None];
    Norm_PV_by_customer=(PV_by_customer.sum()/No_of_days_season[days_count])/np.array(max_PV)[:,None];
    
    #mean of normalised value over all customers
    norm_mean_load=Norm_load_by_customer.mean();
    norm_mean_PV=Norm_PV_by_customer.mean();

    #Load plot
    plt.figure(1)
    fig1, ax1 = plt.subplots()
    ax1.plot(list(range(1,len(norm_mean_load)+1)),norm_mean_load, 'r', linewidth=2,label='mean')
    box_plot_load=Norm_load_by_customer.plot.box(ax=ax1,showfliers=False);
    plt.xticks(np.arange(1,49,6))
    plt.title('Normalised Load Profiles for '+ season_str[days_count]+  ' Over the Year (2012 June - 2013 May)' )
    plt.xlabel('Time')
    plt.ylabel('Normalised Load Consumption')
    plt.ylim(0,2.5)
    plt.show()
    
    #PV plot
    plt.figure(2)
    fig2, ax2 = plt.subplots()
    ax2.plot(list(range(1,len(norm_mean_PV)+1)), norm_mean_PV, 'r', linewidth=2,label='mean')
    box_plot_load=Norm_PV_by_customer.plot.box(ax=ax2,showfliers=False);
    plt.xticks(np.arange(1,49,6))
    plt.title('Normalised PV Generation Profiles for '+ season_str[days_count]+  ' Over the Year (2012 June - 2013 May)' )
    plt.xlabel('Time')
    plt.ylabel('Normalised PV Generation')
    plt.ylim(0,1.2)
    plt.show()

    days_count+=1;

