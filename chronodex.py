import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

date = '20191113' 
tick = []
radii = []
radii_mood = []
notes = []

# read in timetable
with open(str('./data/'+date+'.txt'), "r") as filestream:
    for line in filestream:
        currentline = line.rstrip('\n')
        currentline = currentline.split(',')
        tick.append(int(currentline[0]))
        if currentline[1].strip():
            radii.append(currentline[1].strip())
        else:
            radii.append(radii[-1])
        if currentline[2].strip():
            radii_mood.append(int(currentline[2]))
        else: 
            radii_mood.append(radii_mood[-1])
        notes.append(currentline[3].strip())
# prepare palette that shows up in legend based on unique agenda items
palette = [[0.8, 0.8, 0.2, 0.6],
          [0.5, 0.2, 0.2, 0.6],
          [1, 0.1, 0.5, 0.6],
          [0.5, 0.1, 0.5, 0.6],
          [0.2, 0.4, 0.6, 0.6],
          [1, 0.5, 0.2, 0.6],
          [0.2, 0.8, 0.2, 0.6], 
          [0.1, 0.8, 1, 0.6]]

legend_elements = []
agenda = list(set(radii))
agenda.sort()
for i in range(len(agenda)):
    legend_elements.append(mpatches.Patch(facecolor=palette[i],
                         label=agenda[i]))
# plot
N = 24
bottom = 2

# create theta for 24 hours
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False) + np.pi / N

colors = np.array([(0.2, 1, 0.6, 0.6)]*len(radii))
for i in range(len(agenda)):
    mask = [radii[j] == agenda[i] for j in range(len(radii))] # assign color based on agenda palette
    colors[mask] = palette[i]

# width of each bin on the plot
width = (2*np.pi) / (N)

# make a polar plot
plt.figure(figsize = (12, 8))
ax = plt.subplot(111, polar=True)
bars = ax.bar(theta, radii_mood, width=width, bottom=bottom, color=colors)
for i in range(len(theta)):
    if notes[i]:
        if (radii_mood[i] == radii_mood[i-1] and i>0):
            ax.annotate(notes[i],xy=(theta[i]+width/2,radii_mood[i]+2))
        elif (radii_mood[i] - radii_mood[i-1] <= 2 and i>0 and radii_mood[i] > radii_mood[i-1]):
            ax.annotate(notes[i],xy=(theta[i]+width/2,radii_mood[i]+1))
        else:
            ax.annotate(notes[i],xy=(theta[i]+width/2,radii_mood[i]-0.1))
                   
# set the lable go clockwise and start from the top
ax.set_theta_zero_location("N")
# clockwise
ax.set_theta_direction(-1)

# set the label
ticks = ['0:00', '3:00', '6:00', '9:00', '12:00', '15:00', '18:00', '21:00']
ax.set_xticklabels(ticks)
ax.yaxis.set_ticklabels([])

# legend
chartBox = ax.get_position()
ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.6, chartBox.height])
ax.legend(handles=legend_elements, loc='upper right',bbox_to_anchor=(1.45, 0.8),)

plt.savefig(str('./figures/'+date+'.png'), dpi=100,bbox_inches='tight', 
               transparent=True,
               pad_inches=0)
plt.show()