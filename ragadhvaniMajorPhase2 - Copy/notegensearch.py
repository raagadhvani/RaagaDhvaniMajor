import keras_tuner as kt
import keras
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import LSTM, Dense
from ast import literal_eval
from sklearn.model_selection import train_test_split

# Load data from CSV file
df = pd.read_csv('final_merged_numbers_skb.csv')  # Replace 'your_dataset.csv' with the actual filename

# Convert string representations of lists to actual lists
df['Input Sequence'] = df['Input Sequence'].apply(literal_eval)
df['Succeeding Sequence'] = df['Succeeding Sequence'].apply(literal_eval)

# Convert sequences to numpy arrays
input_sequences = np.array(df['Input Sequence'].tolist(), dtype=np.float32)
succeeding_sequences = np.array(df['Succeeding Sequence'].tolist(), dtype=np.float32)

# Reshape the input sequences to match LSTM input shape (samples, time steps, features)
input_sequences = input_sequences.reshape((input_sequences.shape[0], 1, input_sequences.shape[1]))

input_sequences_train, input_sequences_test, succeeding_sequences_train, succeeding_sequences_test = train_test_split(
    input_sequences, succeeding_sequences, test_size=0.2, random_state=42  # Adjust test_size and random_state as needed
)



# Function to build the model with hyperparameters
def build_model(hp):
    
    # Hyperparameters
    hp_units = hp.Int('units', min_value=16, max_value=64, step=16)
    hp_dense_units = hp.Int('dense_units', min_value=4, max_value=16, step=4)
    hp_learning_rate = hp.Choice('learning_rate', values=[1e-2, 1e-3, 1e-4])

    # Model architecture
    model = Sequential()
    model.add(LSTM(hp_units, activation='tanh', input_shape=(1, 8)))
    model.add(Dense(hp_dense_units, activation='relu'))
    model.add(Dense(8, activation='sigmoid'))

    # Compile the model
    optimizer = keras.optimizers.RMSprop(learning_rate=hp_learning_rate)
    model.compile(optimizer=optimizer, loss='mse')  # Replace loss if neede

    return model

tuner = kt.Hyperband(build_model, objective='val_loss', max_epochs=1000)  # Adjust max_epochs as needed

tuner.search(input_sequences, succeeding_sequences, epochs=1000, validation_split=0.2)  # Start the search

# Get the best hyperparameters after at least one trial has been completed
best_hps = tuner.get_best_hyperparameters(num_trials=1)[0]  # Now this should return a result
print(best_hps.values)  # Print the hyperparameter values

# Retrieve the best model
best_model = tuner.get_best_models(num_models=1)[0]