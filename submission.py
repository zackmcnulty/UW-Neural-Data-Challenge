#load the train data with popular tool pandas
import pandas as pd
import numpy as np
import os 
import matplotlib.pyplot as plt 
%matplotlib inline

#load the stimuli with numpy
stim = np.load('../input/stim.npy')
df = pd.read_csv('../input/train.csv')
df.index = df.Id#turn the first col to index
df = df.iloc[:,1:]#get rid of first col that is now index
df.head()
