# Importing required libraries.
import pandas as pd
import numpy as np
import seaborn as sns #visualisation
import matplotlib.pyplot as plt #visualisation
sns.set(color_codes=True)

# Tweets extraction
tweets = pd.read_json("tweets_extraction.json")

# Displaying the JSON file
print(tweets)

# Verifying data type
print(tweets.dtypes)

# Verifying data structure
print(tweets.info())

# Gets descriptive statistics for numeric columns
print(tweets.describe())


# Open a text file in writing mode only for tweets
with open("tweets.txt", "w") as f:
    # Redirect stdout to file
    print("\nTweets:", file=f)
    # Iterate over each row of the tweets DataFrame
    for index, tweet in tweets.iterrows():
        print("\n", tweet, file=f)
    
# Open a text file in writing mode only for tweets information
with open("tweets_verifications.txt", "w") as g:
    # Redirect stdout to file
    print("\nDATA TYPES:", file=g)
    print(tweets.dtypes, file=g)
    
    print("\nDATA STRUCTURE:", file=g)
    print(tweets.info(), file=g)
    
    print("\nDESCRIPTIVE STATISTICS:", file=g)
    print(tweets.describe(), file=g)