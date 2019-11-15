import sys
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import subprocess

date = str(sys.argv[1]) 
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
# prepare palette that shows up in legend based on unique agenda items #nippon color; morandi#curl 'http://colormind.io/list/'
transparency = 0.9
MyOut = subprocess.Popen(['curl', 'http://colormind.io/api/', '--data-binary', '{"model":"default"}'], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT)
stdout,stderr = MyOut.communicate()

print(stdout)
temp = (stdout.decode('ASCII')).split('result":',1)[1] 
temp = temp.rstrip('}\n')
text = temp.split('],[')
try1 = [list(map(int,((text[i].strip("[]")).split(',')))) for i in range(len(text))]
MyOut = subprocess.Popen(['curl', 'http://colormind.io/api/', '--data-binary', '{"model":"ui"}'], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT)
stdout,stderr = MyOut.communicate()

print(stdout)
temp = (stdout.decode('ASCII')).split('result":',1)[1] 
temp = temp.rstrip('}\n')
text = temp.split('],[')
try2 = [list(map(int,((text[i].strip("[]")).split(',')))) for i in range(len(text))]
palette_rgb = try1 + try2
transparency = 1
palette = []
for color in palette_rgb:
    rgb = [c/255 for c in color]
    rgb.append( transparency)
    palette = palette + [rgb]


# palette = [[0.8784,0.2353,0.5412, transparency],
#             [0.9686,0.3608,0.1843, transparency],
#           [0.3922,0.2118,0.2353, transparency],
#           [0.9843,0.8863,0.3176, transparency],
#           [0.5686,0.6784,0.4392, transparency],
#           [0.0667,0.1961,0.5216, transparency],
#           [0,0.5373,0.6549, transparency],
#           [0.6941,0.5882,0.5765, transparency]]

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