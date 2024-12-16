# from scipy.stats import norm
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# ## plotting a normal standard distribution curve
# x = np.arange(1,10, 0.01)
# mean = np.mean(x)
# sd = np.std(x)
# pdf = norm.pdf(x, loc = (mean+1), scale = sd)
# sns.lineplot(x=x, y=pdf)
# plt.show()
# #######################################################################################################################

# from scipy.stats import norm
# mean = 503
# sd = 1.53
# prob = norm(loc = mean, scale = sd).cdf(506)
# print(round(prob * 100,2))

#######################################################################################################################
# from scipy.stats import norm
# mean = 1120
# sd = 140
# upper_prob = norm(loc = mean, scale = sd).cdf(1250)
# lower_prob = norm(loc = mean, scale = sd).cdf(1100)
# prob = upper_prob - lower_prob
# print(round(prob * 100,2))