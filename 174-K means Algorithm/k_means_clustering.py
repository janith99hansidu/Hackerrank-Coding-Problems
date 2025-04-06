import random
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs

def k_means(k: int, num_samples: int):
    # generate 3 clusters
    X, y_true = make_blobs(n_samples=num_samples, centers=k, cluster_std=0.60, random_state=0)
    
    # step 1 get random k numbers as initial centers
    random_indices = random.sample(range(0, num_samples), k)
    random_centers = [X[idx] for idx in random_indices]

    for j in range(10):    
        # calculate the distance to one sample to each 
        y_pred = []
        cluster = -1
        y_pred_freq = {keyval:0 for keyval in range(k)}


        for i in range(num_samples):
            min_distance = float('inf')
            # calculate distances to each 
            for center in range(len(random_centers)):
                current_distance = np.sum((X[i] - random_centers[center])**2)
                # if calculated distance is smaller than current mark 
                if current_distance <= min_distance:
                    min_distance = current_distance
                    # add to a min distance cluster
                    cluster = center
                
            # add the minimum distance cluster as cluster
            y_pred.append(cluster)
            # make a frequency dictionary to calculate average at one iteration 
            y_pred_freq[cluster] += 1

        # plot the predicted values
        plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap='viridis')
        plt.title(f"Data with Predicted Cluster Labels for {j+1} th iteration")
        plt.xlabel("Feature 1")
        plt.ylabel("Feature 2")
        plt.show()

        # step 2 calculate the average center as new value of the center
        avg_centers = np.zeros((k, 2)) 

        for i in range(num_samples):
            avg_centers[y_pred[i]] += X[i]

        for j in range(k):
            if y_pred_freq[j] != 0:
                avg_centers[j] /= y_pred_freq[j]

        random_centers = avg_centers
    

    return

if __name__ == "__main__":
    k_means(3, 300)