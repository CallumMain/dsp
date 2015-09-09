[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

In this exercise we are examining the difference between the birth weights of first babies versus other babies.  I started off by taking a look at the mean and the variance of both of the groups and then calculated the difference between the means of both groups and found that first babies are lighter on average than other babies by about 2oz.  In order to quantify this difference I then computed Cohen's d for the two groups usin this function:

```
def Cohens_D(x1, x2, x0):
    d = (x1.mean() - x2.mean()) / x0.var()**0.5
    return d
```

I calculated a d of -0.0886 which is a very small effect size meaning that there is no meaningful difference in average weight between the two groups.  One thing to note is that there is a slight margin of difference between the d that I got and the d that the book got and I think this may be due to rounding error as I used the variance of the whole population whereas they calculated the pooled varience.

I then repeated the exact same set of calculations for the length of pregnancy and found that first babies have slightly longer average pregnancies but the effect size is still 0.0289 which is very small and as a result there is no meaningful difference.
