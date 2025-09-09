#!/usr/bin/env python
# coding: utf-8

# # Day 15: UberPool Driver Earnings Optimization Strategies

# You are a Business Analyst on the Uber Pool Product Team working to optimize driver compensation. The team aims to understand how trip characteristics impact driver earnings. Your goal is to develop data-driven recommendations that maximize driver earnings potential.

# In[ ]:


import pandas as pd
import numpy as np

fct_trips_data = [
  {
    "trip_id": 101,
    "driver_id": 1,
    "ride_type": "UberPool",
    "trip_date": "2024-07-05",
    "rider_count": 3,
    "total_distance": 10.5,
    "total_earnings": 22.5
  },
  {
    "trip_id": 102,
    "driver_id": 1,
    "ride_type": "UberPool",
    "trip_date": "2024-07-15",
    "rider_count": 2,
    "total_distance": 8,
    "total_earnings": 18
  },
  {
    "trip_id": 103,
    "driver_id": 2,
    "ride_type": "UberPool",
    "trip_date": "2024-08-10",
    "rider_count": 4,
    "total_distance": 15,
    "total_earnings": 35
  },
  {
    "trip_id": 104,
    "driver_id": 3,
    "ride_type": "UberX",
    "trip_date": "2024-07-20",
    "rider_count": 1,
    "total_distance": 5,
    "total_earnings": 12
  },
  {
    "trip_id": 105,
    "driver_id": 2,
    "ride_type": "UberPool",
    "trip_date": "2024-09-01",
    "rider_count": 3,
    "total_distance": 12,
    "total_earnings": 30
  },
  {
    "trip_id": 106,
    "driver_id": 4,
    "ride_type": "UberPool",
    "trip_date": "2024-09-15",
    "rider_count": 5,
    "total_distance": 20,
    "total_earnings": 50
  },
  {
    "trip_id": 107,
    "driver_id": 4,
    "ride_type": "UberPool",
    "trip_date": "2024-10-01",
    "rider_count": 3,
    "total_distance": 9,
    "total_earnings": 25
  },
  {
    "trip_id": 108,
    "driver_id": 5,
    "ride_type": "UberPool",
    "trip_date": "2024-08-25",
    "rider_count": 4,
    "total_distance": 11,
    "total_earnings": 28
  },
  {
    "trip_id": 109,
    "driver_id": 1,
    "ride_type": "UberPool",
    "trip_date": "2024-09-30",
    "rider_count": 3,
    "total_distance": 6,
    "total_earnings": 16
  },
  {
    "trip_id": 110,
    "driver_id": 2,
    "ride_type": "UberPool",
    "trip_date": "2024-07-07",
    "rider_count": 2,
    "total_distance": 7,
    "total_earnings": 15
  },
  {
    "trip_id": 111,
    "driver_id": 3,
    "ride_type": "UberPool",
    "trip_date": "2024-08-05",
    "rider_count": 4,
    "total_distance": 13,
    "total_earnings": 32
  },
  {
    "trip_id": 112,
    "driver_id": 5,
    "ride_type": "UberX",
    "trip_date": "2024-09-10",
    "rider_count": 1,
    "total_distance": 4,
    "total_earnings": 10
  },
  {
    "trip_id": 113,
    "driver_id": 6,
    "ride_type": "UberPool",
    "trip_date": "2024-07-30",
    "rider_count": 3,
    "total_distance": 22,
    "total_earnings": 45
  },
  {
    "trip_id": 114,
    "driver_id": 6,
    "ride_type": "UberPool",
    "trip_date": "2024-08-22",
    "rider_count": 4,
    "total_distance": 18,
    "total_earnings": 42
  },
  {
    "trip_id": 115,
    "driver_id": 7,
    "ride_type": "UberPool",
    "trip_date": "2024-09-21",
    "rider_count": 5,
    "total_distance": 25,
    "total_earnings": 60
  }
]
fct_trips = pd.DataFrame(fct_trips_data)


# ## Question 1
# 
# What is the average driver earnings per completed UberPool ride with more than two riders between July 1st and September 30th, 2024? This analysis will help isolate trips that meet specific rider thresholds to understand their impact on driver earnings.

# In[ ]:


# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_trips
# Please print your final result or dataframe
fct_trips['trip_date'] = pd.to_datetime(fct_trips['trip_date'])

cond1 = fct_trips['trip_date'] >= '2024-07-01'
cond2 = fct_trips['trip_date'] <= '2024-09-30'
cond3 = fct_trips['ride_type'] == 'UberPool'
cond4 = fct_trips['rider_count'] > 2

new_table = fct_trips[cond1 & cond2 & cond3 & cond4]
new_table

new_table_earnings = new_table['total_earnings'].mean()

new_table_earnings


# ## Question 2
# 
# For completed UberPool rides between July 1st and September 30th, 2024, derive a new column calculating earnings per mile (total_earnings divided by total_distance) and then compute the average earnings per mile for rides with more than two riders. This calculation will reveal efficiency metrics for driver compensation.

# In[ ]:


# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_trips
# Please print your final result or dataframe
fct_trips['trip_date'] = pd.to_datetime(fct_trips['trip_date'])

cond1 = fct_trips['trip_date'] >= '2024-07-01'
cond2 = fct_trips['trip_date'] <= '2024-09-30'
cond3 = fct_trips['ride_type'] == 'UberPool'
cond4 = fct_trips['rider_count'] > 2

new_table = fct_trips[cond1 & cond2 & cond3 & cond4]

new_table['earnings_per_mile'] = new_table['total_earnings'] / new_table['total_distance']

new_table_avg_earnings_per_mile = new_table['earnings_per_mile'].mean()

new_table_avg_earnings_per_mile


# ## Question 3
# 
# Identify the combination of rider count and total distance that results in the highest average driver earnings per UberPool ride between July 1st and September 30th, 2024. This analysis directly recommends optimal trip combination strategies to maximize driver earnings.

# In[ ]:


# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: fct_trips
# Please print your final result or dataframe
fct_trips['trip_date'] = pd.to_datetime(fct_trips['trip_date'])

cond1 = fct_trips['trip_date'] >= '2024-07-01'
cond2 = fct_trips['trip_date'] <= '2024-09-30'
cond3 = fct_trips['ride_type'] == 'UberPool'

new_table = fct_trips[cond1 & cond2 & cond3]

grouped = new_table.groupby(['rider_count', 'total_distance'])['total_earnings'].mean()

grouped_top = grouped.idxmax()

grouped_top


# Made with ❤️ by [Interview Master](https://www.interviewmaster.ai)
