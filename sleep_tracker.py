import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib.dates as mdates
from datetime import datetime


# read in timetable

dates = []
sleep = []
for file in os.listdir("./data"):
    if file.endswith(".txt"):
        dates.append(file.rstrip('.txt'))
        with open(str('./data/'+file), "r") as filestream:
            tick = []
            radii = []
            radii_mood = []
            notes = []
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
        sleep.append(radii.count('sleep'))
        
dates_format = [datetime.strptime(d, "%Y%m%d") for d in dates]



# Create figure and plot a stem plot with the date
fig, ax = plt.subplots(figsize=(8.8, 4))
ax.set(title="SLEEP TRACKER")

markerline, stemline, baseline = ax.stem(dates_format, sleep,
                                         linefmt="C3-", basefmt="k-")

plt.setp(markerline, mec="k", mfc="w", zorder=3)
# ax.get_xaxis().set_major_formatter(mdates.WeekdayLocator(byweekday=MO))
ax.get_xaxis().set_major_locator(mdates.DayLocator(interval=3))
ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%a, %d %b"))


plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
plt.savefig(str('./figures/'+'sleep_tracker.png'), dpi=100,bbox_inches='tight', 
               transparent=True,
               pad_inches=0)
plt.show()