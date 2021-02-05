# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 13:15:35 2020

@author: TAM048
"""
# 2)hour-wise analysis 
# x-axis: 48 time instants of a day
# y-axis: Normalised energy of load/PV
# boxplot: variation of days over the season or year

#Group by date
solar_home_load=(solar_data[GL_loadtype|CL_loadtype]).groupby('date')[time_series];
solar_home_PV=(solar_data[PV_loadtype].groupby('date'))[time_series];

#step 1:
#Find the half-hourly average load consumption/maximum PV generation
#Firstly sum energy over all customers then over the year  
#Secondly find the half-hourly mean(for load)/max(for PV) energy
#Lastly scaling the data by dividing by No. of days of a year  
mean_load=solar_home_load.sum().sum().mean()/No_of_days_year;
max_PV=solar_home_PV.sum().sum().max()/No_of_days_year;

season_count=0;
for specific_season in season:
    
    #get different dataframe for loadtype then group by dates
    load_data_season=solar_data[specific_season & (GL_loadtype | CL_loadtype)];
    PV_data_season=solar_data[specific_season & PV_loadtype];
    
    load_by_date=load_data_season.groupby('date')[time_series];
    PV_by_customer=PV_data_season.groupby('date')[time_series];
    
    #dataframe for boxplot
    #normalised by value obtained in step 1
    Norm_load_by_date=(load_by_date.sum())/mean_load
    Norm_PV_by_customer=(PV_by_customer.sum())/max_PV
    
    #mean of normalised value over all customers
    norm_mean_load=Norm_load_by_date.mean();
    norm_mean_PV=Norm_PV_by_customer.mean();

    #Load plot
    plt.figure(1)
    fig1, ax1 = plt.subplots()
    ax1.plot(list(range(1,49)),norm_mean_load, 'r', linewidth=2,label='mean')
    box_plot_load=Norm_load_by_date.plot.box(ax=ax1,showfliers=False);
    plt.xticks(np.arange(1,49,6))
    plt.title('Normalised Load Profiles for '+ season_str[season_count]+  ' Over the Year (2012 June - 2013 May)' )
    plt.xlabel('Time')
    plt.ylabel('Normalised Load Consumption')
    plt.ylim(0,2.5)
    plt.show()
    
    #PV plot
    plt.figure(2)
    fig2, ax2 = plt.subplots()
    ax2.plot(list(range(1,49)), norm_mean_PV, 'r', linewidth=2,label='mean')
    box_plot_load=Norm_PV_by_customer.plot.box(ax=ax2,showfliers=False);
    plt.xticks(np.arange(1,49,6))
    plt.title('Normalised PV Generation Profiles for '+ season_str[season_count]+  ' Over the Year (2012 June - 2013 May)' )
    plt.xlabel('Time')
    plt.ylabel('Normalised PV Generation')
    plt.ylim(0,1.3)
    plt.show()

    season_count+=1;
