import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

plt.title('Population Growth')
plt.grid()

plt.xlabel('Year')
plt.ylabel('Population')

plt.axis([1950, 2010, 0, 10])

plt.scatter(year, pop)
plt.show()