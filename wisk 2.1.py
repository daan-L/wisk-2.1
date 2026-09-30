import numpy as np

fout_g = 0.14
g = 9.81
t = np.array([0.56, 0.54, 0.66, 0.72, 0.78, 0.79, 0.66, 0.59, 0.79, 0.66, 0.66, 0.66])

n = len(t)

som = sum(t)

t_gem = som/n

s = np.sqrt(1/(n-1)*np.sum((t-t_gem)**2))
fout_t= (1/np.sqrt(n))*s


fout_h0 = np.sqrt((1/2*t_gem**2*fout_g)**2+(g*t_gem*fout_t)**2)

h0 = 0.5*g*t_gem**2

print(t_gem)
print(h0, "+-", fout_h0, "meter")
