# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 15:48:41 2020

@author: TAM048
"""
#Import module
import os;
os.system ("cls");
import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;
from datetime import date, timedelta;

#Read two Ausgrid files: 2011-2012 & 2012-2013 for 300 solar home
solar_data_2011_2012=pd.read_csv("2011-2012 Solar home electricity data v2.csv",header=1);
solar_data_2012_2013=pd.read_csv("2012-2013 Solar home electricity data v2.csv",header=1);

#Combine two file together to form data from June 2012 - May 2013 
solar_data_2011_2012['date']=pd.to_datetime(solar_data_2011_2012['date'],format='%d/%m/%Y');
solar_data_2012_2013['date']=pd.to_datetime(solar_data_2012_2013['date'],format='%d/%m/%Y');
solar_data=solar_data_2011_2012[solar_data_2011_2012.date.dt.month==6].append(solar_data_2012_2013[solar_data_2012_2013.date.dt.month!=6], ignore_index=True);

#Data cleaning: customer 2 is found to have empty data for serveral month 
solar_data=solar_data[solar_data.Customer!=2];
No_of_customer=299;

#Get sepcific column 
month=solar_data.date.dt.month;
load_type=solar_data['Consumption Category'];
time_series=solar_data.columns[5:-1];#heading of half-hour gap in each day

#Index of specific season for data
winter_period=(month==6) | (month==7) | (month==8);#92 days
spring_period=(month==9) | (month==10) | (month==11); #91 days
summer_period=(month==12) | (month==1) | (month==2);#90 days
autumn_period=(month==3) | (month==4) | (month==5);#92 days
year_period= (winter_period) | (spring_period) | (summer_period) | (autumn_period);
season=[winter_period,spring_period,summer_period,autumn_period,year_period];

#Index of loadtype
GL_loadtype=load_type=='GC';#general load
CL_loadtype=load_type=='CL';#controlled load
PV_loadtype=load_type=='GG';#PV generation

#define date for each season for manipulation of data
winter_daterange=pd.date_range(date(2012, 6, 1),date(2012, 8, 31));
spring_daterange=pd.date_range(date(2012, 9, 1),date(2012,11, 30));
summer_daterange=pd.date_range(date(2012, 12, 1),date(2013, 2, 28));
autumn_daterange=pd.date_range(date(2013, 3, 1),date(2013, 5, 31));
whole_year_daterange=pd.date_range(date(2012, 6, 1),date(2013, 5, 31));
season_daterange=[winter_daterange,spring_daterange,summer_daterange,autumn_daterange, whole_year_daterange];

No_of_days_winter=len(winter_daterange);
No_of_days_spring=len(spring_daterange);
No_of_days_summer=len(summer_daterange);
No_of_days_autumn=len(autumn_daterange);
No_of_days_year=No_of_days_winter+No_of_days_spring+No_of_days_summer+No_of_days_autumn;
No_of_days_season=[No_of_days_winter,No_of_days_spring,No_of_days_summer,No_of_days_autumn,No_of_days_year]

#string for plotting
season_str=['Winter','Spring','Summer','Autumn','All Seasons'];

# 1)hour-wise analysis 
# x-axis: 48 time instants of a day
# y-axis: Normalised energy of load/PV
# boxplot: variation of 300 customers
#exec(open("Norm_hour_wise_vary_by_customer.py").read())

# 2)hour-wise analysis 
# x-axis: 48 time instants of a day
# y-axis: Normalised energy of load/PV
# boxplot: variation of days over the season or year
#exec(open("Norm_hour_wise_vary_by_day.py").read())

# 3)day-wise analysis 
# x-axis: days of a season or year 
# y-axis: Normalised energy of load/PV
# boxplot: variation of customers over the season or year
#exec(open("Norm_day_wise_vary_by_customer.py").read())

# 4) PV versus load analysis
# capacity against load size annually, scatter plot and frequency histogram
#exec(open('load_vs_PV.py').read())


    




 

    
