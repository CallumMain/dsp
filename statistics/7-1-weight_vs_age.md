[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

In this exercise we are looking at the relationships between variables and in particular looking at the correlation between variables and what that means.  To start I made a scatter plot of age vs birth weight:

Then to get a better idea of what is going on in the data I binned the data and plotted the percentiles.  In this plot we can see that weight tends to increase more rapidly between 15 and 25 and then starts to taper off after about 30.

Finally I calculated the Pearson's product-moment correlation coefficient or Pearson's r using the following function:

I also calculated Spearman's rank correlation coefficient or Spearman's rho using the following function:

In the end I got an `r = 0.688` and a `ρ = 0.094` which tells me that these two variables are weekly correlated meaning that there is a week relationship between the two.
