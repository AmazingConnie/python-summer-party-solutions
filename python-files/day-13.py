#!/usr/bin/env python
# coding: utf-8

# # Day 13: New Milkshake Flavor Selection for Launch

# You are a Product Analyst working with the Shake Shack R&D team to evaluate customer ratings for experimental milkshake flavors. Your team has collected ratings data from a small sampling test. Your task is to systematically analyze and clean the ratings data to identify top-performing flavors.

# In[ ]:


import pandas as pd
import numpy as np

milkshake_ratings_data = [
  {
    "flavor": "Classic Chocolate",
    "rating": 4.5,
    "customer_id": "CUST001",
    "rating_date": "2024-07-05"
  },
  {
    "flavor": "Strawberry Swirl",
    "rating": 3.8,
    "customer_id": "CUST002",
    "rating_date": "2024-07-10"
  },
  {
    "flavor": "Vanilla Bean",
    "rating": 4.2,
    "customer_id": "CUST003",
    "rating_date": "2024-07-15"
  },
  {
    "flavor": "Caramel Delight",
    "rating": 3.5,
    "customer_id": "CUST004",
    "rating_date": "2024-07-20"
  },
  {
    "flavor": "Mocha Bean",
    "rating": null,
    "customer_id": "CUST005",
    "rating_date": "2024-07-25"
  },
  {
    "flavor": "Classic Chocolate",
    "rating": 4.5,
    "customer_id": "CUST001",
    "rating_date": "2024-07-05"
  },
  {
    "flavor": "Classic Chocolate",
    "rating": 5,
    "customer_id": "CUST006",
    "rating_date": "2024-08-01"
  },
  {
    "flavor": "Strawberry Swirl",
    "rating": 4,
    "customer_id": "CUST007",
    "rating_date": "2024-08-02"
  },
  {
    "flavor": "Vanilla Bean",
    "rating": 3.9,
    "customer_id": "CUST008",
    "rating_date": "2024-08-03"
  },
  {
    "flavor": "Caramel Delight",
    "rating": 4.8,
    "customer_id": "CUST009",
    "rating_date": "2024-10-04"
  },
  {
    "flavor": "Mocha Bean",
    "rating": 2.5,
    "customer_id": "CUST010",
    "rating_date": "2024-09-05"
  },
  {
    "flavor": "Classic Chocolate",
    "rating": 4.7,
    "customer_id": "CUST011",
    "rating_date": "2024-10-06"
  },
  {
    "flavor": "Strawberry Swirl",
    "rating": null,
    "customer_id": "CUST012",
    "rating_date": "2024-10-07"
  },
  {
    "flavor": "Vanilla Bean",
    "rating": 4.3,
    "customer_id": "CUST013",
    "rating_date": "2024-10-08"
  },
  {
    "flavor": "Caramel Delight",
    "rating": 4.9,
    "customer_id": "CUST014",
    "rating_date": "2024-10-09"
  },
  {
    "flavor": "Mocha Bean",
    "rating": 3.3,
    "customer_id": "CUST015",
    "rating_date": "2024-08-10"
  },
  {
    "flavor": "Classic Chocolate",
    "rating": 1,
    "customer_id": "CUST016",
    "rating_date": "2024-08-11"
  },
  {
    "flavor": "Strawberry Swirl",
    "rating": 6,
    "customer_id": "CUST017",
    "rating_date": "2024-08-12"
  },
  {
    "flavor": "Vanilla Bean",
    "rating": 3,
    "customer_id": "CUST018",
    "rating_date": "2024-08-13"
  },
  {
    "flavor": "Caramel Delight",
    "rating": 4.2,
    "customer_id": "CUST019",
    "rating_date": "2024-08-14"
  },
  {
    "flavor": "Mocha Bean",
    "rating": 4.1,
    "customer_id": "CUST020",
    "rating_date": "2024-08-15"
  },
  {
    "flavor": "Classic Chocolate",
    "rating": 3.7,
    "customer_id": "CUST021",
    "rating_date": "2024-08-16"
  },
  {
    "flavor": "Strawberry Swirl",
    "rating": 3.9,
    "customer_id": "CUST022",
    "rating_date": "2024-08-17"
  },
  {
    "flavor": "Vanilla Bean",
    "rating": 4.4,
    "customer_id": "CUST023",
    "rating_date": "2024-08-18"
  },
  {
    "flavor": "Caramel Delight",
    "rating": 3.6,
    "customer_id": "CUST024",
    "rating_date": "2024-08-19"
  },
  {
    "flavor": "Mocha Bean",
    "rating": null,
    "customer_id": "CUST025",
    "rating_date": "2024-08-20"
  },
  {
    "flavor": "Classic Chocolate",
    "rating": 4.8,
    "customer_id": "CUST026",
    "rating_date": "2024-08-21"
  },
  {
    "flavor": "Strawberry Swirl",
    "rating": 4.6,
    "customer_id": "CUST027",
    "rating_date": "2024-08-22"
  },
  {
    "flavor": "Vanilla Bean",
    "rating": 4,
    "customer_id": "CUST028",
    "rating_date": "2024-08-23"
  },
  {
    "flavor": "Caramel Delight",
    "rating": 4.4,
    "customer_id": "CUST029",
    "rating_date": "2024-08-24"
  },
  {
    "flavor": "Mocha Bean",
    "rating": 3.2,
    "customer_id": "CUST030",
    "rating_date": "2024-11-25"
  },
  {
    "flavor": "Classic Chocolate",
    "rating": 4.9,
    "customer_id": "CUST031",
    "rating_date": "2024-11-26"
  },
  {
    "flavor": "Strawberry Swirl",
    "rating": 4.1,
    "customer_id": "CUST032",
    "rating_date": "2024-11-27"
  },
  {
    "flavor": "Vanilla Bean",
    "rating": 3.3,
    "customer_id": "CUST033",
    "rating_date": "2024-11-28"
  },
  {
    "flavor": "Caramel Delight",
    "rating": 3.8,
    "customer_id": "CUST034",
    "rating_date": "2024-11-29"
  },
  {
    "flavor": "Mocha Bean",
    "rating": 4,
    "customer_id": "CUST035",
    "rating_date": "2024-11-30"
  },
  {
    "flavor": "Classic Chocolate",
    "rating": 4.3,
    "customer_id": "CUST036",
    "rating_date": "2024-12-01"
  },
  {
    "flavor": "Strawberry Swirl",
    "rating": null,
    "customer_id": "CUST037",
    "rating_date": "2024-12-02"
  },
  {
    "flavor": "Vanilla Bean",
    "rating": 3.7,
    "customer_id": "CUST038",
    "rating_date": "2024-12-03"
  },
  {
    "flavor": "Caramel Delight",
    "rating": 4.5,
    "customer_id": "CUST039",
    "rating_date": "2024-12-04"
  },
  {
    "flavor": "Mocha Bean",
    "rating": 3.9,
    "customer_id": "CUST040",
    "rating_date": "2024-12-05"
  },
  {
    "flavor": "Classic Chocolate",
    "rating": 4.4,
    "customer_id": "CUST041",
    "rating_date": "2024-12-06"
  },
  {
    "flavor": "Strawberry Swirl",
    "rating": 3.5,
    "customer_id": "CUST042",
    "rating_date": "2024-12-07"
  },
  {
    "flavor": "Vanilla Bean",
    "rating": 4.6,
    "customer_id": "CUST043",
    "rating_date": "2024-12-08"
  },
  {
    "flavor": "Caramel Delight",
    "rating": 4.2,
    "customer_id": "CUST044",
    "rating_date": "2025-02-09"
  },
  {
    "flavor": "Mocha Bean",
    "rating": 3.4,
    "customer_id": "CUST045",
    "rating_date": "2025-02-10"
  },
  {
    "flavor": "Classic Chocolate",
    "rating": null,
    "customer_id": "CUST046",
    "rating_date": "2025-02-11"
  },
  {
    "flavor": "Strawberry Swirl",
    "rating": 4,
    "customer_id": "CUST047",
    "rating_date": "2025-02-12"
  },
  {
    "flavor": "Vanilla Bean",
    "rating": 4.1,
    "customer_id": "CUST048",
    "rating_date": "2025-02-13"
  },
  {
    "flavor": "Caramel Delight",
    "rating": 4.3,
    "customer_id": "CUST049",
    "rating_date": "2025-04-14"
  },
  {
    "flavor": "Mocha Bean",
    "rating": 3.7,
    "customer_id": "CUST050",
    "rating_date": "2025-04-15"
  },
  {
    "flavor": "Classic Chocolate",
    "rating": 4.6,
    "customer_id": "CUST051",
    "rating_date": "2025-04-16"
  },
  {
    "flavor": "Strawberry Swirl",
    "rating": 4.3,
    "customer_id": "CUST052",
    "rating_date": "2025-04-17"
  },
  {
    "flavor": "Vanilla Bean",
    "rating": 3.8,
    "customer_id": "CUST053",
    "rating_date": "2025-04-18"
  },
  {
    "flavor": "Caramel Delight",
    "rating": null,
    "customer_id": "CUST054",
    "rating_date": "2025-06-19"
  },
  {
    "flavor": "Mocha Bean",
    "rating": 4.7,
    "customer_id": "CUST055",
    "rating_date": "2025-06-20"
  },
  {
    "flavor": "Classic Chocolate",
    "rating": 4,
    "customer_id": "CUST056",
    "rating_date": "2025-06-21"
  },
  {
    "flavor": "Strawberry Swirl",
    "rating": 4.2,
    "customer_id": "CUST057",
    "rating_date": "2025-06-22"
  },
  {
    "flavor": "Vanilla Bean",
    "rating": 3.6,
    "customer_id": "CUST058",
    "rating_date": "2025-06-23"
  },
  {
    "flavor": "Caramel Delight",
    "rating": 4,
    "customer_id": "CUST059",
    "rating_date": "2025-06-24"
  }
]
milkshake_ratings = pd.DataFrame(milkshake_ratings_data)


# ## Question 1
# 
# There was an error in our data collection process, and we unknowingly introduced duplciate rows into our data. Remove any duplicate entries in the customer ratings data to ensure the accuracy of the analysis.

# In[ ]:


# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: milkshake_ratings
# Please print your final result or dataframe
milkshake_ratings = milkshake_ratings.drop_duplicates()

milkshake_ratings


# ## Question 2
# 
# For each milkshake flavor, calculate the average customer rating and append this as a new column to the milkshake_ratings DataFrame. Don't forget to clean the DataFrame first by dropping duplicate values.

# In[ ]:


milkshake_ratings = milkshake_ratings.drop_duplicates()

avg_rating = milkshake_ratings.groupby('flavor')['rating'].mean().reset_index()
avg_rating.rename(columns={'rating':'avg_flavor_rating'}, inplace=True)

#milkshake_ratings['avg'] = avg_rating['flavor']

milkshake_ratings_with_avg = pd.merge(milkshake_ratings, avg_rating, on='flavor', how='left')
milkshake_ratings_with_avg


# ## Question 3
# 
# For each row in dataset, calculate the difference between that customer's rating and the average rating for the flavor. Don't forget to clean the DataFrame first by dropping duplicate values.

# In[ ]:


milkshake_ratings = milkshake_ratings.drop_duplicates()

avg_rating = milkshake_ratings.groupby('flavor')['rating'].mean().reset_index()
avg_rating.rename(columns={'rating':'avg_flavor_rating'}, inplace=True)

#milkshake_ratings['avg'] = avg_rating['flavor']

milkshake_ratings_with_avg = pd.merge(milkshake_ratings, avg_rating, on='flavor', how='left')
milkshake_ratings_with_avg['rating'] = milkshake_ratings_with_avg['rating'].fillna(0)

milkshake_ratings_with_avg['rating_diff'] = milkshake_ratings_with_avg['rating'] - milkshake_ratings_with_avg['avg_flavor_rating']

milkshake_ratings_with_avg['rating_diff']


# Made with ❤️ by [Interview Master](https://www.interviewmaster.ai)
