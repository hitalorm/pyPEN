import pandas as pd
import matplotlib.pyplot as plt

col = ['kpar','body','mat','x','y','z','u','v','w','e','elost','wght','tallymode','ilb(5)']
df = pd.read_csv('tallyParticleTrackStructure.dat', delimiter = '\s+', names = col, skiprows=7)
#rint(df)
print(df['kpar'][0])
df = df[(df['kpar']=='3') & (df['tallymode']==-99)]

plt.hist(df['e']/1e6)
plt.show()
