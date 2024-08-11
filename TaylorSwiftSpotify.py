# Spotify data (taylor_swift_spotify_data,csv) is thanks to adashofdata on Github! 
import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# libraries 

# reads file 

TSwiftFile = pd.read_csv('taylor_swift_spotify_data.csv')
# finds unique album names in the data 
album_order = TSwiftFile['Album'].unique()
# Categorical variable
TSwiftFile['Album'] = pd.Categorical(TSwiftFile['Album'], categories=album_order, ordered=True)
# Groups by album name (Taylor Swift, Fearless, Speak Now.. etc) and counts the song of each album 
grouped = TSwiftFile.groupby('Album')
song_count = grouped.size()
# Gets the average duration (ms) from grouped 
mean_duration = grouped['Duration_ms'].mean()
# Figureeee, colors, defining those colors 
plt.figure(figsize=(12,8))
bar_colors = ['tab:green', 'gold', 'tab:purple', 'tab:red', 'paleturquoise', 'tab:gray','tab:pink','silver', 'sienna', 'midnightblue']
bar_colors = bar_colors[:len(mean_duration)]
# content of bar graph 
plt.bar(mean_duration.index, mean_duration.values, color= bar_colors)
# labels 
plt.xlabel('Album')
plt.ylabel('Mean (ms)')
plt.title('Mean duration in Each Taylor Swift Album (Before TV, deluxe, and TTPD)')
plt.xticks(rotation=45, ha='right')
plt.show()



# Figure for number of songs in each album 

plt.figure(figsize=(12,8))
# Eras colors!!!!!!
bar_colors = ['tab:green', 'gold', 'tab:purple', 'tab:red', 'paleturquoise', 'tab:gray','tab:pink','silver', 'sienna', 'midnightblue']
# Defining those colors 
bar_colors = bar_colors[:len(song_count)]
# Content of bar graph 
plt.bar(song_count.index, song_count.values, color= bar_colors)
plt.xlabel('Album')
plt.ylabel('Amount of Songs')
plt.title('Number of Songs in Each Taylor Swift Album (Before TV, deluxe, and TTPD)')
plt.xticks(rotation=45, ha='right')
plt.show()




