#!/usr/bin/python

import sys
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches


date = str(sys.argv[1])
tick = []
radii = []
radii_mood = []
notes = []

with open(str('./data/'+date+'.txt'), "r") as filestream:
    for line in filestream:
        currentline = line.rstrip('\n')
        currentline = currentline.split(',')
        tick.append(int(currentline[0]))
        radii.append(int(currentline[1]))
        radii_mood.append(int(currentline[2]))

        notes.append(currentline[3].strip())



legend_elements = [mpatches.Patch(facecolor=[0.8, 0.8, 0.2, 0.6],
                         label='chore'),
                   mpatches.Patch(facecolor=[0.5, 0.2, 0.2, 0.6],
                         label='food'),
                   mpatches.Patch(facecolor=[1, 0.1, 0.5, 0.6],
                         label='fun'),
                   mpatches.Patch(facecolor=[0.5, 0.1, 0.5, 0.6],
                         label='meeting'),
                   mpatches.Patch(facecolor=[0.2, 0.4, 0.6, 0.6],
                         label='sleep'),
                  mpatches.Patch(facecolor=[1, 0.5, 0.2, 0.6],
                         label='surf'),
                  
                  
                  mpatches.Patch(facecolor=[0.2, 0.8, 0.2, 0.6],
                         label='text'),
                  mpatches.Patch(facecolor=[0.1, 0.8, 1, 0.6],
                         label='work')
                  ]
N = 24
bottom = 2

# create theta for 24 hours
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False) + np.pi / N



# make the histogram that bined on 24 hour
# radii, tick = np.histogram(arr, bins = 23)

# colors = np.array(['b']*len(radii))
colors = np.array([(0.2, 1, 0.6, 0.6)]*len(radii))


mask = [i == 1 for i in radii] # chore
colors[mask] = (0.8, 0.8, 0.2, 0.6)
mask = [i == 2 for i in radii]# food
colors[mask] = (0.5, 0.2, 0.2, 0.6)
mask = [i == 3 for i in radii] # fun
colors[mask] = (1, 0.1, 0.5, 0.6)
mask = [i == 4 for i in radii]  # meeting
colors[mask] = (0.5, 0.1, 0.5, 0.6)
mask = [i == 5 for i in radii] # sleep
colors[mask] = (0.2, 0.4, 0.6, 0.6)
mask = [i == 6 for i in radii]# surf
colors[mask] = (1, 0.5, 0.2, 0.6)
mask = [i == 7 for i in radii]  # text
colors[mask] = (0.2, 0.8, 0.2, 0.6)
mask = [i == 8 for i in radii] # work
colors[mask] = (0.1, 0.8, 1, 0.6)



# width of each bin on the plot
width = (2*np.pi) / (N)

# make a polar plot
plt.figure(figsize = (12, 8))
ax = plt.subplot(111, polar=True)
# radii_mood, tick = np.histogram(mood, bins = 23)
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

# ax.get_yaxis().set_visible(False)
# ax.get_yaxis().set_ticks([])
ax.yaxis.set_ticklabels([])

# legend
handles = [colors[i] for i in np.unique(radii)]


chartBox = ax.get_position()
ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.6, chartBox.height])

ax.legend(handles=legend_elements, loc='upper right',bbox_to_anchor=(1.45, 0.8),)

# plt.legend(handles, labels)
# ax.legend(bars,['sleep'])
plt.savefig(str('./figures/'+date+'.png'), dpi=100,bbox_inches='tight', 
               transparent=True,
               pad_inches=0)
