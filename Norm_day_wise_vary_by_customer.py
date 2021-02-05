# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 13:15:35 2020

@author: TAM048
"""

# 3)day-wise analysis 
# x-axis: days of a season
# y-axis: Normalised energy of load/PV
# boxplot: variation of customers over the season or year

#Group by Customer and date
solar_home_load=(solar_data[GL_loadtype|CL_loadtype]).groupby(['Customer','date'])[time_series];
solar_home_PV=(solar_data[PV_loadtype].groupby(['Customer','date']))[time_series];

# find the average daily load consumption/ maximum PV generation over the year for each customer
mean_load=solar_home_load.sum().sum(axis=1).groupby('Customer').mean();
max_PV=solar_home_PV.sum().sum(axis=1).groupby('Customer').max()

season_count=0;
for specific_season in season[0:-1]:
    
    load_data_season=solar_data[specific_season & (GL_loadtype | CL_loadtype)];
    PV_data_season=solar_data[specific_season & PV_loadtype];
    
    load_by_customer=load_data_season.groupby(['Customer','date'])[time_series];
    PV_by_customer=PV_data_season.groupby(['Customer','date'])[time_series];
    
    #data frame for box plot
    #find the daily consumption/PV generation for each customer each date
    #turn the manipulated data into a dataframe from series
    Norm_load_by_customer=(load_by_customer.sum().sum(axis=1)/mean_load).to_frame();
    Norm_PV_by_customer=(PV_by_customer.sum().sum(axis=1)/max_PV).to_frame();
    
    Norm_load_by_customer.reset_index(inplace=True);Norm_load_by_customer=Norm_load_by_customer.rename(columns = {0:'Norm_value'});
    Norm_PV_by_customer.reset_index(inplace=True);Norm_PV_by_customer=Norm_PV_by_customer.rename(columns = {0:'Norm_value'});
    
    Norm_load_by_customer=Norm_load_by_customer.pivot_table(index='Customer',columns='date',values='Norm_value');
    Norm_PV_by_customer=Norm_PV_by_customer.pivot_table(index='Customer',columns='date',values='Norm_value');
    
    #normalised mean for line plot
    norm_mean_load=Norm_load_by_customer.mean();
    norm_mean_PV=Norm_PV_by_customer.mean();
    
    #xticks selection for plotting
    daterange=season_daterange[season_count];
    first_day_of_month=(daterange.day==1);
    xtick_index=np.asarray(np.where(first_day_of_month))+1;
    xtick_index=np.concatenate((xtick_index[0], [No_of_days_season[season_count]]), axis=0);    
    Norm_load_by_customer.columns=Norm_load_by_customer.columns.strftime('%b-%d');
    Norm_PV_by_customer.columns=Norm_PV_by_customer.columns.strftime('%b-%d');
    
    #Load plot
    plt.figure(1)
    fig1, ax1 = plt.subplots()
    ax1.plot(list(range(1,len(norm_mean_load)+1)),norm_mean_load, 'r', label='mean')
    box_plot_load=Norm_load_by_customer.plot.box(ax=ax1,showfliers=False);
    plt.xticks(xtick_index,rotation=45)
    plt.title('Normalised Load Profiles for '+ season_str[season_count]+  ' Over the Year (2012 June - 2013 May)' )
    plt.xlabel('Day')
    plt.ylabel('Normalised Load Consumption')
    plt.ylim(0,2.5)
    plt.show()
    
    #PV plot
    plt.figure(2)
    fig2, ax2 = plt.subplots()
    ax2.plot(list(range(1,len(norm_mean_PV)+1)), norm_mean_PV, 'r', label='mean')
    box_plot_load=Norm_PV_by_customer.plot.box(ax=ax2,showfliers=False);
    plt.xticks(xtick_index,rotation=45)
    plt.title('Normalised PV Generation Profiles for '+ season_str[season_count]+  ' Over the Year (2012 June - 2013 May)' )
    plt.xlabel('Day')
    plt.ylabel('Normalised PV Generation')
    plt.ylim(0,1)
    plt.show()

    season_count+=1;    
