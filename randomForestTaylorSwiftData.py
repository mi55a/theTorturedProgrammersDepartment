
# Important libraries for the program 
# Spotify data (taylor_swift_spotify_data.csv) is thanks to adashofdata on Github! 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, mean_squared_error, classification_report, confusion_matrix

# Classifies if a song is a hit or not hit (energy) based on danceability and loudness 

# Cleaning data set from irrelevant columns and converting columns with string values to numeric values

data_tswift = 'taylor_swift_spotify_data.csv'

df_swift = pd.read_csv(data_tswift, header=0)

df_swift = pd.get_dummies(df_swift, columns=['Album', 'Song Name'], drop_first=True)

df_swift = df_swift.drop(columns= ['Playlist ID', 'URI'], errors='ignore')

df_swift = df_swift.apply(pd.to_numeric, errors="coerce")

df_swift.to_csv('taylor_swift_spotify_data_cleaned.csv', index=False)

# Input for target variable, two inputs for random tree. Output for outcome variable, what's predicted on the input

df_swift['DanceabilityClass'] = df_swift['Danceability'].apply(lambda x: 1 if x >= .400 else 0)

df_swift['LoudnessEnergy'] = df_swift['Loudness'].apply(lambda l: 1 if l >= -4.00 else 0)

df_swift['HitClassification'] = df_swift['Energy'].apply(lambda y: 1 if y >= .400 else 0)

X = df_swift[['DanceabilityClass', 'LoudnessEnergy']]

y = df_swift['HitClassification']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.3, random_state=42)

# Random forest with 100 decision trees (omg a forest!!!)

rf = RandomForestClassifier(n_estimators=100, random_state=42)

rf.fit(X_train,y_train)

y_pred = rf.predict(X_test)

# Accuracy score 

accurate = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accurate:.2f}")

# Classification report 

print(classification_report(y_test, y_pred))

# Confusion matrix hehe

cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d", xticklabels=["Not Hit Song", "Hit Song"], yticklabels=["Not Hit Song", "Hit Song"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Hit Song or Not Hit Song")
plt.show()

'''

WIP: Print song and album title for each of the songs

df_swift.info()
RangeIndex: 147 entries, 0 to 146
Columns: 168 entries, Danceability to Song Name_‘tis the damn season
dtypes: bool(155), float64(13)

features_important = rf.feature_importances_
feature_df_swift = pd.DataFrame({"Feature": albumAndSong, 'Importance': features_important})
feature_df_swift = feature_df_swift.sort_values(by='Importance', ascending=False)

print(feature_df_swift)

147, 168 df_swift.shape

'''