#!/usr/bin/env python
# coding: utf-8

# In[10]:


#!pip install wwo-hist


# In[3]:


from wwo_hist import retrieve_hist_data
import os
os.chdir("/Users/gonzalorigirozzi/Downloads")
frequency=12
start_date = '11-DEC-2018'
end_date = '11-JAN-2019'
api_key = '35b7a88fa68046849a6210511221107'
location_list = ['california']

hist_weather_data = retrieve_hist_data(api_key,
                                location_list,
                                start_date,
                                end_date,
                                frequency,
                                location_label = False,
                                export_csv = True,
                                store_df = True)


# In[11]:


from wwo_hist import retrieve_hist_data
import os
os.chdir("")
frequency=12
start_date = '1-JAN-2015'
end_date = '31-DEC-2015'
api_key = '35b7a88fa68046849a6210511221107'
location_list = ['20637 20653 20688 20740 20794 20871 21040 21158 21208 21241 21411 21502 21536 21625 21638 21639 21643 21650 21704 21742 21801 21811 21853 21912']

hist_weather_data = retrieve_hist_data(api_key,
                                location_list,
                                start_date,
                                end_date,
                                frequency,
                                location_label = False,
                                export_csv = True,
                                store_df = True)


# In[ ]:




