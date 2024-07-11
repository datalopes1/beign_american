#%% 
import pandas as pd
import numpy as np
# %%
df = pd.read_csv("data/raw/nonvoters_data.csv")
df.head()
# %%
df.columns.to_list()[:30]
# %%
df.columns.to_list()[30:60]
# %%
df.columns.to_list()[60:90]
# %%
df.columns.to_list()[90:]
