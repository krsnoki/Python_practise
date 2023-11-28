import matplotlib.pyplot as plt

data = {'Hindavi' : 80, 'Sarthak': 60, 'Kalyani': 90, 'Shreya': 64, 'Prasad': 78 }

names = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (10, 5))
plt.bar(names, values, color = 'g', width = 0.4)

plt.xlabel('Names')
plt.ylabel('Values')
plt.title('kalyanis bargraph')
plt.show()
