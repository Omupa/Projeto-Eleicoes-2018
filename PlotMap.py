import json, os

data_dir = "../data_new/"
array = []
array2 = []
for folder in os.listdir(data_dir):
    data = data_dir + folder + "/"

    if not os.path.exists("../data_locations/" + folder):
        os.makedirs("../data_locations/" + folder)

    for file in os.listdir(data):
        with open(data + file, 'r') as g:
            tweets = g.readlines()
            for line in tweets:
                data = json.loads(line)
                if (data.get('place')):
                    array.append(data.get('place').get('bounding_box').get('coordinates'))
data_loc.close()

for point in array:
    for point2 in point:
        array2.append(point2)


#PLOTING
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


def mapTut():
    # m = Basemap(projection='mill',llcrnrlat=-35,urcrnrlat=7,llcrnrlon=-77,urcrnrlon=-32,resolution='c')
    m = Basemap(projection='mill', llcrnrlat=-35, urcrnrlat=7, llcrnrlon=-77, urcrnrlon=-32)
    m.drawcoastlines()
    m.drawcountries(color='black')
    m.drawstates(color='gray')
    m.fillcontinents(color='#a1a1a1', lake_color='#FFFFFF')
    m.drawmapboundary(fill_color='#ffffff')

    for ponto in array2:
        x, y = m(ponto[0][0], ponto[1][1])
        m.plot(x, y, 'ro')

    plt.title("Localization Plotting")
    plt.show()


mapTut()
