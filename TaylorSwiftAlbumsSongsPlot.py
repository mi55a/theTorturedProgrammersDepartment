# Taylor Swift Albums Songs Plot 
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
# importing packages

fig, ax = plt.subplots(figsize =(12,6))

# info 
albums = ["Taylor Swift", "Fearless", "Speak Now", "Red", "1989", "reputation", 
          "Lover", "folklore", "evermore", "Midnights", "TTPD"]
count = [15, 26, 22, 30, 22, 15, 18, 17, 17, 20, 31]
bar_labels = ["Debut", "Fearless", "Speak Now", "Red", "1989", "reputation",
              "Lover", "folklore", "evermore", "Midnights", "The Tortured Poets Department"]
bar_colors = ['tab:green', 'gold', 'tab:purple', 'tab:red', 'paleturquoise', 'tab:gray','tab:pink','silver', 'sienna', 'midnightblue','slategray']
ax.bar(albums, count, label=bar_labels, color = bar_colors)
# labelsss
ax.set_ylabel('Songs')
ax.set_title("Songs in every Taylor Swift album")
ax.set_xlabel('Album')
ax.legend(title="Era")

plt.show()