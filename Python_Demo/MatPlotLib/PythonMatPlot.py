import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = 'Fonts/SourceHanSansCN-Regular.otf'
prop = fm.FontProperties(fname=font_path)

year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

plt.title('人口成長趨勢', fontproperties=prop, size=20)
plt.grid()

plt.xlabel('年', fontproperties=prop)
plt.ylabel('人口', fontproperties=prop)

plt.axis([1950, 2010, 0, 10])

plt.plot(year, pop)
plt.show()