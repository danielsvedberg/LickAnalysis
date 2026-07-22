'''
Welcome to lesson 2: likelihood and Monte Carlo simulation
Follow the instructions in the comments to complete the tasks.
You can run this script line by line, or run the whole script at once.
'''

#run the following to load the data
import pandas as pd # pandas is a module for handling tabular data, like spreadsheets
import numpy as np # numpy is a module for handling array data, giving python much of MATLAB's functionality# this line is needed to make matplotlib work on some computers, but not all. If you get an error when you run the script, try commenting out this line by putting a # in front of it.

import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt # matplotlib is a module for making plots, like MATLAB's plotting functions

trial_events = pd.read_csv("trial_events.csv") #loads the trial_events table
trial_events['ttfl'] = trial_events['outcome_time'] - trial_events['start_time'] #makes a new column called 'ttf' (time to first lick) which is the difference between the outcome and start times.
ttfl = trial_events['ttfl'] #assigns the 'ttfl' column to a variable called ttfl
lick_events = pd.read_csv("lick_events.csv") #loads the lick_events table

lam = len(lick_events) / (lick_events['time'].max() - lick_events['time'].min())
def epdf(x, lam):
    y = lam * np.exp(-lam * x)
    return y

# get the maximum likelihood estimate of lambda for ttfl
# generate an array of possible lambda values to test
lam_values = np.linspace(0, 2, 10000)
mlelikes = []
for lam in lam_values:
    mlelikes.append(np.sum(np.log(epdf(ttfl, lam))))

#plot the likelihood of each lambda value
plt.plot(lam_values, mlelikes)
plt.show(block=True)

#shortcut get the maximum likelihood estimate of lambda for ttfl
lam = lam_values[np.argmax(mlelikes)]

'''
Example 1: Hypothesis test against Monte Carlo simulation
'''
'''
Ex.1 Part 1: likelihood of observed data: 
as we discussed, you can calculate the likelihood of some data under a given model. 
Below, calculate the likelihood of the observed first lick times under the exponential 
distribution model we fit in lesson 1. (take a look at the above code, it's from lesson 1)
remember: the likelihood is the product of each data point's probability density under the model.
Follow the instructions below to calculate this
'''
# Step 1: in the space below, use the epdf function to generate an array with the probability density of each data point.
# Hint: epdf can take individual values or an array of values, so you can just pass in the ttfl array to get the probability density of each data point.


# Step 2: In the space below, use np.prod() to take the product of all the elements in the array you just generated.
# Hint: google "numpy product" to see how to use np.prod() to take the product of all the elements in an array.


# Step 3: below, make a function combining the above two steps, so that you can easily calculate the likelihood of any data under the model. We'll use this function later.
# call the function explike, and have it take two arguments: data and lam. Have it return a single number: the likelihood of the data under the model.



# Step 3: print the likelihood to see what it is.



'''
Ex.1 Part 2: Monte Carlo simulation
Now that we have the likelihood of the observed data under the model, we want to compare it to a null distribution. 
To do this, we can use Monte Carlo simulation to generate a distribution of likelihoods simulated under the model.
Pop quiz! to test for a p-value as small as 0.001, how many random samples do we need to generate?
First, you want to figure out how to generate one random sample of first lick times that is the same size as the observed data. 
Then, you can use a for-loop to generate many random samples and calculate the likelihood of each one under the model.
Follow the instructions below to generate a distribution of likelihoods under the model.
'''
# Step 1: in the space below, use np.random.exponential() to generate a random sample of first lick times under the exponential distribution model we fit in lesson 1.
# important hint! np.random.exponential() takes the scale parameter, which is 1/lambda. So you need to pass in 1/lam as the scale parameter.


# Step 2: below, calculate the likelihood of the random sample you just generated under the model, and print it.
# You can use the same method you used to calculate the likelihood of the observed data.


# Step 3: now that you know how to generate 1 random sample, you can use a for-loop to generate many random samples and calculate the likelihood of each one under the model.
# hint 1: you want to store the likelihoods into a list. I give you one here below to get you started.
sim_likes = [] #this is an empty list that will store the likelihoods of the random samples under the model.
# below, write a for-loop that runs for 1000 iterations. for i in range(1000): is a good way to do this.
# under the for-loop, write a line that generates a random sample of first lick times under the exponential distribution model we fit in lesson 1.
# then, write a line that calculates the likelihood of the random sample under the model
# then, write a line that appends the likelihood to the sim_likes list
# hint 2: you can use the append() method of a list to add an element to the end of the list.
# For example, sim_likes.append(sim_like) will add the likelihood of the random sample to the sim_likes list.


# step 4: convert the sim_likes list to a numpy array, so that we can easily calculate the p-value later.


'''
Ex 1. Part 3: Hypothesis testing
Now that we have a distribution of likelihoods under the model, we can compare the observed likelihood to this null distribution.
To get the p-value, calculate the proportion of simulated likelihoods that are less than or equal to the observed likelihood.
'''
# Step 1: in the space below, calculate the proportion of simulated likelihoods that are less than or equal to the observed likelihood, and print it.
# hint 1: compare the sim_likes array and the observed likelihood using the <= operator to mark which simulated likelihoods are less than or equal to the observed likelihood.
# hint 2: use np.mean() to calculate the proportion of True values in the true/false array you just created


# step 2: get the p=0.05 threshold for the null distribution, and print it.
# hint 1: use np.percentile() to calculate the 5th percentile of the sim_likes array. This will give you the p=0.05 threshold for the null distribution


'''
Ex 1. Part 4: Data visualization
One way to visualize this hypothesis test is with a bar graph
'''
#Step 1: below, get the 5th and 95th percentiles of the sim_likes array, assign them to variables


#Step 2: plot a bar graph of the empirical likelihood, and the 5th and 95th percentiles of the null distribution
#Hint: you want to log the y axis, since the likelihoods are very small numbers. You can do this with plt.yscale('log')


#Step 3: make a histogram of the null distribution, and a vertical line for the empirical likelihood
#Hint: you will want to log the x axis and use 1000 bins for the histogram. You can do this with plt.xscale('log') and plt.hist(sim_likes, bins=1000)
