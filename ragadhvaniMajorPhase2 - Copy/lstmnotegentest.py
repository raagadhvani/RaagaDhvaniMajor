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

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Best Parameters
param_combination = {
    'Dense_units': 8,
    'LSTM_units': 16,
    'activation': 'tanh',
    'optimizer': 'adam'
}

# Build model with current parameters
model = Sequential()
model.add(LSTM(param_combination['LSTM_units'], activation=param_combination['activation'], input_shape=(1, 8)))
model.add(Dense(param_combination['Dense_units'], activation=param_combination['activation']))
model.add(Dense(8))

model.compile(optimizer=param_combination['optimizer'], loss='mse')


input_sequences_train, input_sequences_test, succeeding_sequences_train, succeeding_sequences_test = train_test_split(
    input_sequences, succeeding_sequences, test_size=0.2, random_state=42  # Adjust test_size and random_state as needed
)

# Train the model on the training set
model.fit(input_sequences_train, succeeding_sequences_train, epochs=1000, verbose=2)  # Adjust epochs as needed



# evaluate_model(model, input_sequences, succeeding_sequences)
import numpy as np

import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

def evaluate_model(model, input_sequences, succeeding_sequences):
    """Evaluates model performance and saves selected configuration and metrics to a text file."""

    loss = model.evaluate(input_sequences, succeeding_sequences, verbose=0)
    predictions = model.predict(input_sequences)

    # Calculate additional metrics
    mae = np.mean(np.abs(predictions - succeeding_sequences))
    mse = mean_squared_error(predictions, succeeding_sequences)
    r2 = r2_score(predictions, succeeding_sequences)

    # Print and save results
    print("Evaluation results:")
    print("- Loss:", loss)
    print("- Mean Absolute Error:", mae)
    print("- Mean Squared Error:", mse)
    print("- R-squared:", r2)

    with open("evaluation_results_new.txt", "a") as f:
        f.write("----- Model Configuration -----\n")

        # Save selected hyperparameters
        f.write(f"Number of neurons in LSTM layer: {model.layers[0].units}\n")  # Assuming LSTM is the first layer
        f.write(f"Number of hidden layers: {len(model.layers) - 2}\n")  # Subtracting input and output layers
        f.write(f"Number of neurons in Dense layers: {model.layers[-1].units}\n")  # Assuming Dense is the last layer
        f.write(f"Activation functions: {', '.join([layer.activation.__name__ for layer in model.layers])}\n")
        f.write(f"Learning rate: {model.optimizer.lr.numpy()}\n")  # Assuming model is compiled with an optimizer
        f.write(f"Batch size: {model.input_shape[0]}\n")  # Assuming batch size is stored in input_shape
        f.write(f"Epochs: {model.optimizer.iterations.numpy()}\n")  # Assuming epochs are tracked in optimizer

        f.write("----- Evaluation Metrics -----\n")
        f.write(f"Loss: {loss:.4f}\n")
        f.write(f"Mean Absolute Error: {mae:.4f}\n")
        f.write(f"Mean Squared Error: {mse:.4f}\n")
        f.write(f"R-squared: {r2:.4f}\n")

# Evaluate model performance on the testing set
evaluate_model(model, input_sequences_test, succeeding_sequences_test)


# Save Model
model.save("notegenerationlstmmodelbvptest1.keras")
