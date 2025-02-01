
import pandas as pd

neutral_df = pd.read_csv("neutral.txt")
resting_df = pd.read_csv("resting.txt")
violent_df = pd.read_csv("violent.txt")



print("neutral_df:", neutral_df.shape)
print("resting_df:", resting_df.shape)
print("violent_df:", violent_df.shape)
