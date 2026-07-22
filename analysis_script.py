''' some basics:
 -the pound symbol (#) denotes comments, anything after it is ignored by the interpreter
 -triple quotes (''' ''') denote a multi-line comment, anything between them is ignored by the interpreter
 -this file is known as a script, you can run it whole, or you can run it line by line
 -in pycharm, you can run parts of a script line by line by clicking on a line, or highlighting several lines, 
  right clicking, and selecting "Execute selection in python console". Those lines will then be executed in the console
'''

'''importing modules
 -at the top of a script, we usually import modules
 -modules give us additional functionality that python does not have
 -modules come from bodies of publicly-available code that are downloaded and installed on your computer
'''

import pandas as pd # pandas is a module for handling tabular data, like spreadsheets
import numpy as np # numpy is a module for handling array data, giving python much of MATLAB's functionality
import matplotlib.pyplot as plt # matplotlib is a module for making plots, like MATLAB's plotting functions

trial_events = pd.read_csv("trial_events.csv") #running this line loads the trial_Events table
# once you do this, try to find "trial_events" in the variable explorer, and click on View as Dataframe to take a look.

'''Part 1: first steps: plotting a histogram'''
# task 1: make a new column called 'time to first lick' which is the difference between the outcome and start times.
## search on google how to make a new pandas column

trial_events['ttfl'] = trial_events['outcome_time'] - trial_events['start_time']

# task 2: once you have your time to first lick column, assign it to a variable with something like:
ttfl = trial_events['ttfl']


# task 3: make a histogram of first lick time
## search on google how to plot a histogram using matplotlib
hist = plt.hist(ttfl, bins=20)

'''Part 2: simulate a random first lick time distribution'''
# task 4: load the "lick_events.csv"
lick_events = pd.read_csv("lick_events.csv")

# task 5: find the mean lick rate for the session (number of licks / time elapsed)
lam = len(lick_events) / (lick_events['time'].max() - lick_events['time'].min())

# task 6: fit an exponential distribution modeling the probability density function of time to first lick
def epdf(x, lam):
    y = lam * np.exp(-lam * x)
    return y

