raw = np.genfromtxt('BodyTemperature_nohead.txt')
raw.shape
raw

male = raw[:,0]
numMale = male.sum()
numFemale = len(male)-numMale

gender = raw[:,0]
age    = raw[:,1]
hr     = raw[:,2]
temp   = raw[:,3]
gender.mean()
age.mean()
hr.mean()
temp.mean()

male = (gender == 1)
female = (gender == 0)
meanres = np.zeros(2,3)
maxres = np.zeros(2,3)
minres = np.zeros(2,3)

'''
Result format:
      | Age     | HeartRate | Temperature |
______|_________|___________|_____________|
Male  |_________|___________|_____________|
Female|_________|___________|_____________|
'''

meanres[0,0] = age[male].mean()
meanres[0,1] = hr[male].mean()
meanres[0,2] = temp[male].mean()
meanres[1,0] = age[female].mean()
meanres[1,1] = hr[female].mean()
meanres[1,2] = temp[female].mean()
maxres[0,0] = age[male].max()
maxres[0,1] = hr[male].max()
maxres[0,2] = temp[male].max()
maxres[1,0] = age[female].max()
maxres[1,1] = hr[female].max()
maxres[1,2] = temp[female].max()
minres[0,0] = age[male].min()
minres[0,1] = hr[male].min()
minres[0,2] = temp[male].min()
minres[1,0] = age[female].min()
minres[1,1] = hr[female].min()
minres[1,2] = temp[female].min()

