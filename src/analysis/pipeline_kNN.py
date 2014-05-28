import os, sys
from helpers.evaluator import Evaluator

import mdp
import numpy as np

from helpers.datahandler import DataHandler

# --- READ DATA ---
handler = DataHandler()
genders, ages, diagnoses = handler.getAllData()

# Take subset of rows
num_ex = 30000
diagnoses = diagnoses[0:num_ex, :]
genders = genders[0:num_ex, :]
ages = ages[0:num_ex, :]

print("Data acquired.")
print("Using {0} first rows.".format(num_ex))
print("\tgenders: {0} x {1}".format(genders.shape[0],genders.shape[1]))
print("\tages: {0} x {1}".format(ages.shape[0],ages.shape[1]))
print("\tdiagnoses: {0} x {1}".format(diagnoses.shape[0],diagnoses.shape[1]))

num_rows = diagnoses.shape[0]
num_features = diagnoses.shape[1]


# --- PCA ---

desired_explained_variance = 0.9

pcanode = mdp.nodes.PCANode(input_dim=diagnoses.shape[1],output_dim=desired_explained_variance)
print("Start training PCANode.")
print("\t# of rows: {0} \n\t# of features: {1}".format(num_rows, num_features))

# Do training in chunks so we don't fill memory
num_chunks = 10
print("\tStarted training in {0} chunks.".format(num_chunks))
for chunk_index in range(0, num_chunks):
    chunk_size = diagnoses.shape[0] // num_chunks
    begin_ind = chunk_size * chunk_index
    end_ind = min(num_rows, chunk_size * (chunk_index + 1))
    if chunk_index == num_chunks - 1:
        end_ind = num_rows
    chunk = diagnoses[begin_ind:end_ind, :].astype("float64")

    pcanode.train(chunk)
print()

# Tell the node that training is done
pcanode.stop_training()
print("PCANode trained.")

# Get the number of output components
print("\t# of components: {0}".format(pcanode.output_dim))
print("\tvariance explained {0}".format(pcanode.explained_variance))

pca_result = pcanode.execute(diagnoses)

print("\tArray resulting from PCA:\n\t{0} x {1}".format(pca_result.shape[0], pca_result.shape[1]))

# --- kNN classification ---
k = 1   # how many nearest neighbours

knn_node = mdp.nodes.KNNClassifier(k=k)

knn_node.n_neighbors = k
print("kNNNode created.")

knn_node.train(pca_result, genders)
print("kNNNode trained.")





input()