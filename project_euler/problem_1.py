# PROBLEM 2.2
# PROBLEM 1.3

import numpy as np
import matplotlib.pyplot as plt


def ff(x, h):
    return 2*np.cos((2*x0+h)/2)*np.cos(h/2)


x0 = 1.2
h = 10**-6

x = np.array([])
for h in 10.0**np.arange(20, -20, -0.5):
    x = ff(x0, h)
    print(x0)

#df_dx = (f(x0 + h) - f(x0-h))/2*h
#abs_err = abs(df_dx - np.cos(1.2))
#est_err = 0.5*abs(np.sin(1.2))*h
#rel_err=abs(df_dx - np.cos(1.2))/abs(np.cos(1.2))
#plt.loglog(h, abs_err, h, est_err, '--',h,rel_err)
#plt.legend({"absolute error", "estimated error","relative error"})
# plt.xlabel("h")
# plt.ylabel("error");
# print(abs_err)

#something=[10**x for x in range(-20,20)]
