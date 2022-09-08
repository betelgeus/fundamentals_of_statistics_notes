# Main question: Is any of the individual parameters or combined make the results between 4 groups statistically significant?
# We have results from 4 tests Young-Low_dosis, Young-High_dosis, Old-Low_dosis, Old-High_dosis (see data link below)
# Our Zero hypothesis (H-zero) is that the results between groups are not statistically significant
# For H-zero to be true F has to be very small (close to 0) and P > 0.05
# A statistically significant test result (P ≤ 0.05) means that the Zerp hypothesis is false or should be rejected
# For the results to be statistically significant F has to be not too small, definetly not close to 0 and P < 0.05
# (P > 0.05 is the probability that the null hypothesis is true)

# Process followed:
# 1. Import libraries
# 2. Import and read dataset
# 3. Clean dataset
# 4. Do EDA (exploratory data analysis) to see the data
# 5. Find F and P
# 6. Conclusion

# 1. Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns

# 2. Import and read dataset
url = 'https://raw.githubusercontent.com/betelgeus/fundamentals_of_statistics_notes/main/data/atherosclerosis.csv'
df = pd.read_csv(url, header=None, sep=',')
# print(df)

# 3. Clean dataset
# We need to clean the data: drop the first row and move column labels to header
# We set the column labels to equal the values in the 1st row (index location 0):
df.columns = df.iloc[0]
# print(df)

# Then we drop the 1st row using iloc
# We will save the new dataset as df_cleaned and will use this dataset from the rest of the operations
df_cleaned = df.iloc[pd.RangeIndex(len(df)).drop(0)]
# print(df_cleaned)

# We convert the 'expr' column to numeric:
df_cleaned.expr = pd.to_numeric(df_cleaned['expr'], errors='coerce')
# print(df_cleaned)
for i in df_cleaned['age']:
    if i == '1':
        print(df_cleaned.loc[1])
#        df_cleaned['age'] = 'Young'
    elif i == '2':
        print(df_cleaned.iloc[1])
#        df_cleaned['age'] = 'Old'
print(df_cleaned)

# 4. Do EDA (exploratory data analysis) to see the data
# Let's explore data looking at boxplot by dose
# We can see the overlap of medians and boxes
df_cleaned.boxplot('expr', by='dose', figsize=(12, 8), grid=True)
# plt.show()

# 4. Do EDA (exploratory data analysis) to see the data
# Let's explore data looking at boxplot by age
# In this case there is a bit more difference and the median of each group is outside the box of the other group
df_cleaned.boxplot('expr', by='age', figsize=(12, 8), grid=True)
# plt.show()

# another view is via pairplot (not too useful here)
sns.pairplot(df_cleaned, y_vars="expr", x_vars=['age', 'dose'])
# plt.show()
