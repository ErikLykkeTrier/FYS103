from scipy.stats import poisson
import matplotlib.pyplot as plt
import math 

#%% Oppgave 11.1 *
#calculate probability
pd = []
v = []
mu = 0.5
for i in range(1,7):
    pd_i = poisson.pmf(k=i, mu=mu)
    pd.append(pd_i)
    v.append(i)

plt.hist(pd)
plt.title("Oppgave 11.1*")
#plt.show()
#%% Oppgave 11.3 **
# (a)

R = 5.00000000000000000000000*10**19

T = 3.0000000000000000000000000000*10**(-20)

u= R*T

#print('mu er ',u)
# (b)
svar = []
for v in range(0,4):
    mm = math.e**(-1.5)*(1.5**v)/math.factorial(v)
    svar.append(mm)

#print(svar)

# (c)
svarc = 1- sum(svar)
#print("Sannsynligheten for 4 eller mer:", svarc)


# %% oppgave 11.7

# (b)

PP_svar = []

for m in range(7,12):
    pp_m = poisson.pmf(k=m, mu=9)
    PP_svar.append(pp_m)
#print(PP_svar)

# (c)

nysvar = 1-sum(PP_svar)
#print(nysvar)

#(d)

#%%  Oppgave 11.13 **


