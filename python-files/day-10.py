#!/usr/bin/env python
# coding: utf-8

# # Day 10: App Store Ratings Performance by App Category

# You are a Product Analyst for the Apple App Store team investigating app ratings data. Your focus is to clean and understand rating distributions across different app categories. The team wants to leverage basic statistical insights to guide app performance strategies.

# In[ ]:


import pandas as pd
import numpy as np

app_ratings_data = [
  {
    "app_id": "app001",
    "rating": "4.5",
    "category": "Games",
    "review_date": "2024-07-05"
  },
  {
    "app_id": "app002",
    "rating": "3.9",
    "category": "Productivity",
    "review_date": "2024-07-06"
  },
  {
    "app_id": "app001",
    "rating": "4.7",
    "category": "Games",
    "review_date": "2024-07-10"
  },
  {
    "app_id": "app003",
    "rating": " 4.0 ",
    "category": "Health & Fitness",
    "review_date": "2024-08-15"
  },
  {
    "app_id": "app004",
    "rating": "five",
    "category": "Education",
    "review_date": "2024-09-01"
  },
  {
    "app_id": "app005",
    "rating": null,
    "category": "Games",
    "review_date": "2024-10-11"
  },
  {
    "app_id": "app006",
    "rating": "4.2",
    "category": "Lifestyle",
    "review_date": "2024-10-20"
  },
  {
    "app_id": "app007",
    "rating": "4",
    "category": "Utilities",
    "review_date": "2024-11-15"
  },
  {
    "app_id": "app008",
    "rating": "3.5",
    "category": "Entertainment",
    "review_date": "2024-12-01"
  },
  {
    "app_id": "app009",
    "rating": "4.9",
    "category": "Health & Fitness",
    "review_date": "2024-12-15"
  },
  {
    "app_id": "app010",
    "rating": "4,2",
    "category": "Games",
    "review_date": "2025-01-07"
  },
  {
    "app_id": "app011",
    "rating": "3.5",
    "category": "Productivity",
    "review_date": "2025-01-15"
  },
  {
    "app_id": "app012",
    "rating": "4.0",
    "category": "Education",
    "review_date": "2025-01-20"
  },
  {
    "app_id": "app013",
    "rating": "2.1",
    "category": "Games",
    "review_date": "2025-02-14"
  },
  {
    "app_id": "app014",
    "rating": "3.8",
    "category": "Lifestyle",
    "review_date": "2025-02-20"
  },
  {
    "app_id": "app015",
    "rating": "4.5",
    "category": "Games",
    "review_date": "2025-03-03"
  },
  {
    "app_id": "app016",
    "rating": "3.3",
    "category": "Utilities",
    "review_date": "2025-03-12"
  },
  {
    "app_id": "app017",
    "rating": "4.8",
    "category": "Entertainment",
    "review_date": "2025-03-20"
  },
  {
    "app_id": "app018",
    "rating": "4.6",
    "category": "Health & Fitness",
    "review_date": "2025-04-01"
  },
  {
    "app_id": "app019",
    "rating": null,
    "category": "Education",
    "review_date": "2025-04-10"
  },
  {
    "app_id": "app020",
    "rating": "3.2",
    "category": "Games",
    "review_date": "2025-04-15"
  },
  {
    "app_id": "app002",
    "rating": "3.7",
    "category": "Productivity",
    "review_date": "2025-04-20"
  },
  {
    "app_id": "app003",
    "rating": "4.0",
    "category": "Health & Fitness",
    "review_date": "2025-05-01"
  },
  {
    "app_id": "app001",
    "rating": "4.6",
    "category": "Games",
    "review_date": "2025-05-05"
  },
  {
    "app_id": "app004",
    "rating": "5",
    "category": "Education",
    "review_date": "2025-05-11"
  },
  {
    "app_id": "app005",
    "rating": "6.0",
    "category": "Games",
    "review_date": "2025-05-13"
  },
  {
    "app_id": "app006",
    "rating": "4.1",
    "category": "Lifestyle",
    "review_date": "2025-05-15"
  },
  {
    "app_id": "app007",
    "rating": "3.0",
    "category": "Utilities",
    "review_date": "2025-05-20"
  },
  {
    "app_id": "app008",
    "rating": "4.2",
    "category": "Entertainment",
    "review_date": "2025-06-02"
  },
  {
    "app_id": "app009",
    "rating": "4.4",
    "category": "Health & Fitness",
    "review_date": "2025-06-07"
  },
  {
    "app_id": "app010",
    "rating": "3.5",
    "category": "Games",
    "review_date": "2025-06-10"
  },
  {
    "app_id": "app011",
    "rating": "4.0",
    "category": "Productivity",
    "review_date": "2025-06-12"
  },
  {
    "app_id": "app012",
    "rating": "4.3",
    "category": "Education",
    "review_date": "2025-06-15"
  },
  {
    "app_id": "app013",
    "rating": "4.1",
    "category": "Games",
    "review_date": "2025-06-18"
  },
  {
    "app_id": "app014",
    "rating": "not available",
    "category": "Lifestyle",
    "review_date": "2025-06-20"
  },
  {
    "app_id": "app015",
    "rating": "3.9",
    "category": "Games",
    "review_date": "2025-06-21"
  },
  {
    "app_id": "app016",
    "rating": "4.6",
    "category": "Utilities",
    "review_date": "2025-06-22"
  },
  {
    "app_id": "app017",
    "rating": "4.0",
    "category": "Entertainment",
    "review_date": "2024-07-07"
  },
  {
    "app_id": "app018",
    "rating": "3.8",
    "category": "Health & Fitness",
    "review_date": "2024-07-08"
  },
  {
    "app_id": "app019",
    "rating": "4.2",
    "category": "Education",
    "review_date": "2024-07-09"
  },
  {
    "app_id": "app020",
    "rating": "4.7",
    "category": "Games",
    "review_date": "2024-07-10"
  },
  {
    "app_id": "app002",
    "rating": "3.8",
    "category": "Productivity",
    "review_date": "2024-07-11"
  },
  {
    "app_id": "app003",
    "rating": "4.3",
    "category": "Health & Fitness",
    "review_date": "2024-07-12"
  },
  {
    "app_id": "app004",
    "rating": "4.4",
    "category": "Education",
    "review_date": "2024-07-13"
  },
  {
    "app_id": "app005",
    "rating": "4.5",
    "category": "Games",
    "review_date": "2024-07-14"
  },
  {
    "app_id": "app006",
    "rating": "4.0",
    "category": "Lifestyle",
    "review_date": "2024-07-15"
  },
  {
    "app_id": "app007",
    "rating": null,
    "category": "Utilities",
    "review_date": "2024-07-16"
  },
  {
    "app_id": "app008",
    "rating": "4.6",
    "category": "Entertainment",
    "review_date": "2024-07-17"
  },
  {
    "app_id": "app009",
    "rating": "3.9",
    "category": "Health & Fitness",
    "review_date": "2024-07-18"
  },
  {
    "app_id": "app010",
    "rating": "4.1",
    "category": "Games",
    "review_date": "2024-07-19"
  }
]
app_ratings = pd.DataFrame(app_ratings_data)


# ## Question 1
# 
# There are some data inconsistencies in the 'rating' column, specifically: leading or trailing white space, decimals represented by commas instead of decimal points (eg. 4,2 instead of 4.2), and non-numeric values. Clean up these data issues and convert the column to a numeric data type.

# In[ ]:


# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: app_ratings
# Please print your final result or dataframe
app_ratings['rating'] = app_ratings['rating'].str.strip()

app_ratings['rating'] = app_ratings['rating'].str.replace(',', '.')

app_ratings['rating'] = pd.to_numeric(app_ratings['rating'], errors='coerce')

app_ratings = app_ratings[app_ratings['rating'].notna()]

app_ratings


# ## Question 2
# 
# Using the cleaned dataset, display the first and last five entries to get an overview of the app ratings across different categories.

# In[ ]:


# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: app_ratings
# Please print your final result or dataframe
app_ratings['rating'] = app_ratings['rating'].str.strip()

app_ratings['rating'] = app_ratings['rating'].str.replace(',', '.')

app_ratings['rating'] = pd.to_numeric(app_ratings['rating'], errors='coerce')

app_ratings = app_ratings[app_ratings['rating'].notna()]

app_ratings_top = app_ratings.head()

app_ratings_bottom =  app_ratings.tail()

print(app_ratings_top) 
print(app_ratings_bottom)


# ## Question 3
# 
# Calculate the basic summary statistics (mean, median, standard deviation) of app ratings for each category to identify variations and performance patterns.

# In[ ]:


# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: app_ratings
# Please print your final result or dataframe
app_ratings['rating'] = app_ratings['rating'].str.strip()

app_ratings['rating'] = app_ratings['rating'].str.replace(',', '.')

app_ratings['rating'] = pd.to_numeric(app_ratings['rating'], errors='coerce')

app_ratings = app_ratings[app_ratings['rating'].notna()]

app_ratings_mean = app_ratings.groupby('category')['rating'].mean()

app_ratings_median = app_ratings.groupby('category')['rating'].median()

app_ratings_std = app_ratings.groupby('category')['rating'].std()

print(app_ratings_mean)
print(app_ratings_median)
print(app_ratings_std)


# Made with ❤️ by [Interview Master](https://www.interviewmaster.ai)
