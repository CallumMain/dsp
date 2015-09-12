[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

In this exercise we are looking at Probability Mass Functions (PMFs) and Cumulative Distribution Functions (CMFs) and comparing their uses.  I started off by creating a list of 1000 randomly generated numbers that I generated using `random.random()`.  Then I then created and plotted a PMF from this distriution seen below:

As you can see, its hard to really tell what's going on just by looking at the distribution, we can't really tell whether or not the distribution is uniform or not.  This is because as the number of values gets bigger, the probability of each value gets smaller and as a result, random noise has a much larger effect on the distribution.  To try and deal with this I then created and ploted a CDF from the original distribution.  The CDF describes the probability that a given x in a distribution will be less than or equal to x.  The CDF is shown below:

As you can see the distribution is roughly a straight line which makes sense since the distribution should be uniform.  To confim this we calculate the mean of the CDF we get 0.5 which confirms that the distribution is uniform.
