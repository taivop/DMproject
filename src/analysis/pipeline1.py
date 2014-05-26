import os, sys

# Add libsvm
sys.path.append(os.path.abspath("../../lib/libsvm-3.18/python"))

import mdp
import numpy as np
import mdp.nodes.libsvm_classifier

from helpers.datahandler import DataHandler

# --- READ DATA ---
handler = DataHandler()
genders, ages, diagnoses = handler.getAllData()
print("Data acquired.")
print("\tgenders: {0} x {1}".format(genders.shape[0],genders.shape[1]))
print("\tages: {0} x {1}".format(ages.shape[0],ages.shape[1]))
print("\tdiagnoses: {0} x {1}".format(diagnoses.shape[0],diagnoses.shape[1]))

num_rows = diagnoses.shape[0]
num_features = diagnoses.shape[1]

desired_explained_variance = 0.9

#TODO: take small subset of data for testing
num_ex = 95
diagnoses = diagnoses[1:num_ex, :]
genders = genders[1:num_ex, :]
ages = ages[1:num_ex, :]

# --- PCA ---

pcanode = mdp.nodes.PCANode(input_dim=diagnoses.shape[1],output_dim=desired_explained_variance)
print("Start training PCANode.")
print("\t# of rows: {0} \n\t# of features: {1}".format(num_rows, num_features))

# Do training in chunks so we don't fill memory
num_chunks = 10
print("\tStarted training in {0} chunks.".format(num_chunks))
for chunk_index in range(0, num_chunks):
    chunk_size = diagnoses.shape[0] // 10
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
print("variance explained {0}".format(pcanode.explained_variance))

pca_result = pcanode.get_projmatrix()


# --- SVM ---

# see doc here: http://mdp-toolkit.sourceforge.net/api/mdp.nodes.LibSVMClassifier-class.html
# and here: http://www.csie.ntu.edu.tw/~cjlin/libsvm/
svmnode = mdp.nodes.LibSVMClassifier(kernel="LINEAR")


