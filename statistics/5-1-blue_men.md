[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

In the previous exercises we were looking at empirical distributions as they are based on observations and thus have a finite number of samples.  In this exercise we are looking at analytical distributions which are characterized by CDFs that are mathematical functions and they can be used to model empirical distributions.  In this exercise we are looking at heights which we know are more or less normally distributed.

So first I created our normal distribution using the given parameters for Men, the mean height is 178cm with a standard deviation of 7.7cm.  We can use SciPy to create our normal distrubtion as follows:

```
mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
```

To then find the percentage of men between 5'10 and 6'1, the percentage of the population who meets the height requirement for the Blue Man Group, we can evaluate the CDF as such:

```
low = dist.cdf(177.8)
high = dist.cdf(185.42)
high - low
```

We find that 34.275% of the male population is within the given range.
