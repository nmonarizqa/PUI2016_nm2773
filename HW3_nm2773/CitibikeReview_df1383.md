## Review of nm2773 Citibike Hypothesis Test


#### Idea:
How does age group impact trip distance? Are the millennials tend to take longer rides than the others?

#### Null Hypothesis:  
H_0 : The ratio of long distance trips by young riders to all distance trips by young
riders is less than or equal to the ratio of long distance trips by the rest of the population
to all distance trips by the rest of the population.

#### Alternative Hypothesis:  
H_1 : The ratio of long distance trips by young riders to all distance trips by young riders is greater
than the ratio of long distance trips by the rest of the population to all distance trips by the rest of the population.

#### a.)
The null and alternative hypothesis are correct according to the initial problem statement of 
do millennials take longer distance trips?

#### b.)
The data that was selected for the test has all the necessary values to test the hypothesis, i.e., age and distance.
My only suggestion would be to consider eliminating extreme outliers in trip distance.
For example the max trip distance is over 5000 miles (very unlikely this is correct).

#### c.)
I recommend using a z test to test if the proportion of long distance trips is larger for millennials compared to non-millennials.
Because you are testing proportions and the sample size is large enough a normal distribution can be assumed and the following z statistic
should be appropiate to test your hypothesis:  

Z = (p1-p2) / sqrt((p*(1−p)*(1/n1+1/n2)))
