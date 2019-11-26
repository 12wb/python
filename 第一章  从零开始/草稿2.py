'''
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

rv = st.poisson(50)
num_years = [52, 55, 49, 43, 61, 53, 48, 40, 51, 53, 50, 42, 58, 51, 45]
x = range(15)
plt.bar(np.array(x)-.4, num_years, label='Observed instances')
plt.plot(x, sum(num_years)*rv.pmf(x), ls='dashed',
        lw=2, c='r', label='Poisson distribution\n$(\lambda=2.0)$')
plt.xlim([-1, 8])
plt.ylim([0, 11])
plt.xlabel('# of mass shootings in a year')
plt.ylabel('# of years')
plt.legend(loc='best')
plt.show()
'''

import scipy.stats as st
import matplotlib.pyplot as plt
rv = st.poisson(50)
[(rv.pmf(i),rv.cdf(i)) for i in range(100)]
print([(rv.pmf(i),rv.cdf(i)) for i in range(100)])
plt.plot([(rv.pmf(i),rv.cdf(i)) for i in range(100)])
plt.show()

rv = st.poisson(50)
plt.plot([rv.pmf(i) for i in range(100)])
plt.show()

rv = st.poisson(50)
plt.plot([rv.cdf(i) for i in range(100)])
plt.show()