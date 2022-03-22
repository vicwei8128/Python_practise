import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontpath = "Fonts/SourceHanSansCN-Regular.otf"
prop = fm.FontProperties(fname=fontpath)

year = [1950, 1970, 1990, 2010]
pop = [3.1, 4.2, 5.5, 6.3]

plt.title("人口成長趨勢",  fontproperties = prop, size= 20)
plt.grid()

plt.xlabel("年代", fontproperties = prop)
plt.ylabel("人口", fontproperties = prop)

plt.axis([1950, 2010, 0, 10])
plt.plot(year, pop)
plt.scatter(year, pop)
plt.show()