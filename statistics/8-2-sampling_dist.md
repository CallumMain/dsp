[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

In this exercise we are looking at sampling from a distribution and seeing the effects of the sample size on the error and confidence interval.  To start I sampled from an exponential distribution with sample size `n=10` with `λ=2` and simulated this 1000 times and plotted the resulting sampling distribution:

![Fig1](/img/Q6Fig1.png)

I then calculated the standard error of our estimate and the 90% confidence interval and got a standard error of 0.896717911545 and a 90% confidence interval between (1.2901330772324622, 3.869233489242792).  Clearly our error is very high here so I increased the sample size to `n=100` and ran the experiment and plotted the results:

![Fig2](/img/Q6Fig2.png)

The standard error is now 0.211118579366  and the confidence interval is now (1.7179432268950321, 2.3887031376972865).  We can see that the interval has narrowed and the error has dropped dramatically.  I ran the experiment one more time with `n=1000` and plotted the results again

![Fig3](/img/Q6Fig3.png)

The standard error is now 0.0615597512828 and the confidence interval is (1.9023814501496725, 2.1071755080490551).  So we can see that the interval is narrowing around the actual value we are estimating which is 2.  Finally I plotted all of the standard errors versus number of samples:

![Fig4](/img/Q6Fig4.png)

As you can see, the standard error drops dramatically between `n=10` and `n=100` but then starts to taper off between `n=100` and `n=1000` and I would expect the slope would decrease as the number of samples increases.  This means that while increasing the samples estimates the distribution better, but the improvements diminish as the number of samples increases.
