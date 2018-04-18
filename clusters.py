import copy
import random
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from datetime import datetime


df = pd.DataFrame({
    'x': [5.1
,
4.9
,
4.7
,
4.6
,
5
,
5.4
,
4.6
,
5
,
4.4
,
4.9
,
5.4
,
4.8
,
4.8
,
4.3
,
5.8
,
5.7
,
5.4
,
5.1
,
5.7
,
5.1
,
5.4
,
5.1
,
4.6
,
5.1
,
4.8
,
5
,
5
,
5.2
,
5.2
,
4.7
,
4.8
,
5.4
,
5.2
,
5.5
,
4.9
,
5
,
5.5
,
4.9
,
4.4
,
5.1
,
5
,
4.5
,
4.4
,
5
,
5.1
,
4.8
,
5.1
,
4.6
,
5.3
,
5
,
7
,
6.4
,
6.9
,
5.5
,
6.5
,
5.7
,
6.3
,
4.9
,
6.6
,
5.2
,
5
,
5.9
,
6
,
6.1
,
5.6
,
6.7
,
5.6
,
5.8
,
6.2
,
5.6
,
5.9
,
6.1
,
6.3
,
6.1
,
6.4
,
6.6
,
6.8
,
6.7
,
6
,
5.7
,
5.5
,
5.5
,
5.8
,
6
,
5.4
,
6
,
6.7
,
6.3
,
5.6
,
5.5
,
5.5
,
6.1
,
5.8
,
5
,
5.6
,
5.7
,
5.7
,
6.2
,
5.1,],
    'y': [3.5
,
3
,
3.2
,
3.1
,
3.6
,
3.9
,
3.4
,
3.4
,
2.9
,
3.1
,
3.7
,
3.4
,
3
,
3
,
4
,
4.4
,
3.9
,
3.5
,
3.8
,
3.8
,
3.4
,
3.7
,
3.6
,
3.3
,
3.4
,
3
,
3.4
,
3.5
,
3.4
,
3.2
,
3.1
,
3.4
,
4.1
,
4.2
,
3.1
,
3.2
,
3.5
,
3.1
,
3
,
3.4
,
3.5
,
2.3
,
3.2
,
3.5
,
3.8
,
3
,
3.8
,
3.2
,
3.7
,
3.3
,
3.2
,
3.2
,
3.1
,
2.3
,
2.8
,
2.8
,
3.3
,
2.4
,
2.9
,
2.7
,
2
,
3
,
2.2
,
2.9
,
2.9
,
3.1
,
3
,
2.7
,
2.2
,
2.5
,
3.2
,
2.8
,
2.5
,
2.8
,
2.9
,
3
,
2.8
,
3
,
2.9
,
2.6
,
2.4
,
2.4
,
2.7
,
2.7
,
3
,
3.4
,
3.1
,
2.3
,
3
,
2.5
,
2.6
,
3
,
2.6
,
2.3
,
2.7
,
3
,
2.9
,
2.9
,
2.5,]
})

random.seed(datetime.now())
k = 3
centroids = {
    i+1: [np.random.randint(0, 15), np.random.randint(0, 15)]
    for i in range(k)
}

fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'], df['y'], color='k')
colmap = {1: 'r', 2: 'g', 3: 'b'}
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 15)
plt.ylim(0, 15)

def assignment(df, centroids):
    for i in centroids.keys():
        # sqrt((x1 - x2)^2 - (y1 - y2)^2)
        df['distance_from_{}'.format(i)] = (
            np.sqrt(
                (df['x'] - centroids[i][0]) ** 2
                + (df['y'] - centroids[i][1]) ** 2
            )
        )
    centroid_distance_cols = ['distance_from_{}'.format(i) for i in centroids.keys()]
    df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
    df['closest'] = df['closest'].map(lambda x: int(x.lstrip('distance_from_')))
    df['color'] = df['closest'].map(lambda x: colmap[x])
    return df

df = assignment(df, centroids)
print(df.head())

fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 15)
plt.ylim(0, 15)

old_centroids = copy.deepcopy(centroids)

def update(k):
    for i in centroids.keys():
        centroids[i][0] = np.mean(df[df['closest'] == i]['x'])
        centroids[i][1] = np.mean(df[df['closest'] == i]['y'])
    return k

centroids = update(centroids)

fig = plt.figure(figsize=(5, 5))
ax = plt.axes()
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 15)
plt.ylim(0, 15)
for i in old_centroids.keys():
    old_x = old_centroids[i][0]
    old_y = old_centroids[i][1]
    dx = (centroids[i][0] - old_centroids[i][0]) * 0.75
    dy = (centroids[i][1] - old_centroids[i][1]) * 0.75
    ax.arrow(old_x, old_y, dx, dy, head_width=0.2, head_length=0.3, fc=colmap[i], ec=colmap[i])

df = assignment(df, centroids)

# Plot results
fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 15)
plt.ylim(0, 15)


# Continue until all assigned categories don't change any more
while True:
    closest_centroids = df['closest'].copy(deep=True)
    centroids = update(centroids)
    df = assignment(df, centroids)
    if closest_centroids.equals(df['closest']):
        break

fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 15)
plt.ylim(0, 15)

plt.show()
