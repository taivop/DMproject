import mdp
import numpy as np

from helpers.datahandler import DataHandler

handler = DataHandler()

genders, ages, diagnoses = handler.getTrainingData()

num_rows = diagnoses.shape[0]
num_features = diagnoses.shape[1]

desired_explained_variance = 0.9

pcanode = mdp.nodes.PCANode(input_dim=diagnoses.shape[1],output_dim=desired_explained_variance)
print("BEFORE training PCANode")
print("# of rows: {0} \n# of features: {1}".format(num_rows, num_features))

# Do training in chunks so we don't fill memory
num_chunks = 10
for chunk_index in range(0, num_chunks):
    chunk_size = num_rows // 10
    begin_ind = chunk_size * chunk_index
    end_ind = min(num_rows, chunk_size * (chunk_index + 1))
    if chunk_index == num_chunks - 1:
        end_ind = num_rows
    chunk = diagnoses[begin_ind:end_ind, :].astype("float64")

    pcanode.train(chunk)


# Tell the node that training is done
pcanode.stop_training()
print("AFTER TRAINING PCANODE")

# Get the number of output components
num_components = pcanode.output_dim
print("# of components: {0}".format(num_components))