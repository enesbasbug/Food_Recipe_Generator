import pandas as pd 
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns
import os
from keras.models import load_model
import tensorflow as tf
from tensorflow import keras
import re
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM,Dense,Embedding,Dropout, Bidirectional
from tensorflow.keras import regularizers
from tensorflow.keras.losses import sparse_categorical_crossentropy
#...
def chicken_meal():

    def split_input_target(chunk):
        input_TEXT = chunk[:-1]
        target_TEXT = chunk[1:]
        return input_TEXT, target_TEXT

    def loss(y_true,y_pred):
        return sparse_categorical_crossentropy(y_true, y_pred, from_logits=True)

    def build_model(vocab_size, embedding_dim, rnn_units, batch_size):
        model = Sequential()
        model.add(Embedding(vocab_size, embedding_dim,batch_input_shape=[batch_size, None]))
        model.add(LSTM(rnn_units,return_sequences=True,stateful=True,recurrent_initializer='glorot_uniform'))
        model.add(Dropout(0.2))
        # model.add(LSTM(rnn_units,return_sequences=True,stateful=True,recurrent_initializer='glorot_uniform'))
        # model.add(Dropout(0.2))
        # Final Dense Layer to Predict
        model.add(Dense(vocab_size))
        model.compile(optimizer='adam', loss=loss) 
        # print(model.summary())
        return model

    def generate_text(model, start_string,t):
        # Evaluation step (generating text using the learned model)
        # Number of characters to generate
        num_generate = 1000
        # Converting our start string to numbers (vectorizing)
        input_eval = [char2idx[s] for s in start_string]
        input_eval = tf.expand_dims(input_eval, 0)
        # Empty string to store our results
        text_generated = []
        # Low temperature results in more predictable text.
        # Higher temperature results in more surprising text.
        # Experiment to find the best setting.
        temperature = t
        # Here batch size == 1
        model.reset_states()
        for i in range(num_generate):
            predictions = model(input_eval)
            # remove the batch dimension
            predictions = tf.squeeze(predictions, 0)
            # using a categorical distribution to predict the character returned by the model
            predictions = predictions / temperature
            predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()
            # Pass the predicted character as the next input to the model
            # along with the previous hidden state
            input_eval = tf.expand_dims([predicted_id], 0)
            text_generated.append(idx2char[predicted_id])
        return (start_string + ''.join(text_generated))



    # TEXT_chicken = open('chicken.txt', 'rb').read().decode(encoding='utf-8')
    TEXT_chicken = open('data/chicken.txt', 'rb').read().decode(encoding='utf-8')
    # TEXT_fish = open('fish.txt', 'rb').read().decode(encoding='utf-8')
    TEXT_ingredients = open('data/ingredients.txt', 'rb').read().decode(encoding='utf-8')
    # The length of texts is the number of characters in it
    BATCH_SIZE = 64

    # Buffer size to shuffle the dataset
    # (TF data is designed to work with possibly infinite sequences,
    # so it doesn't attempt to shuffle the entire sequence in memory. Instead,
    # it maintains a buffer in which it shuffles elements).
    BUFFER_SIZE = 10000
    # The embedding dimension
    embedding_dim = 256
    # Number of RNN units
    rnn_units = 1024
    EPOCHS = 35

    # Directory where the checkpoints will be saved
    checkpoint_dir = './training_checkpoints'
    # Name of the checkpoint files
    checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt_{epoch}")
    checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
        filepath=checkpoint_prefix,
        save_weights_only=True)

    # The unique characters in the file
    vocab = sorted(set(TEXT_chicken))

    # Creating a mapping from unique characters to indices
    char2idx = {u:i for i, u in enumerate(vocab)}
    idx2char = np.array(vocab)
    TEXT_as_int = np.array([char2idx[c] for c in TEXT_chicken])
    seq_length = 100

    # Create training examples / targets
    char_dataset = tf.data.Dataset.from_tensor_slices(TEXT_as_int)
    sequences = char_dataset.batch(seq_length+1, drop_remainder=True)
    dataset = sequences.map(split_input_target)
    dataset = dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder=True)

    # Length of the vocabulary in chars
    vocab_size = len(vocab)

    model = build_model(vocab_size=len(vocab), embedding_dim=embedding_dim, rnn_units=rnn_units, batch_size=BATCH_SIZE)

    # history = model.fit(dataset, epochs=EPOCHS, callbacks=[checkpoint_callback])
    # model.save("chicken_model.h5")
    model = build_model(vocab_size, embedding_dim, rnn_units, batch_size=1)
    model.load_weights("models/chicken_model.h5")
    # model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))
    model.build(tf.TensorShape([1, None]))
    text_file_c = generate_text(model, start_string=u"chicken ",t=0.1)
    # text_file_m
    def word_extraction(text):
        ignore = ["a", "the", "is", "to", "until","about","with","and","as","add","on","in","at","of","over","around","knife","sharp","pairing","once","comes","for","minutes","hours"]
        words = re.sub("[^\w]", " ",  text).split()
        cleaned_text = [w.lower() for w in words if w not in ignore]
        output_ingredients = ["".join(a) for a in cleaned_text if a in TEXT_ingredients]
        return output_ingredients

    ingredients_c = word_extraction(text_file_c)
    output = ingredients_c, text_file_c
    return output


