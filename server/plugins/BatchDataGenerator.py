
import json
import numpy as np
import tensorflow as tf

from PIL import Image
from tqdm.notebook import tqdm


class BatchDataGenerator(tf.keras.utils.Sequence):
    def __init__(self, data, data_dir, batch_size, seq_len, shuffle=True):
        """
            Class to generate data in batch for training
            ----------------------------------------------------------------
            Parameters:
                - filename: path to the file containing the data
                - batch_size: batch size
                - seq_len: sequence length
                - shuffle: shuffle data or not
        """
        self.data = data
        self.DATA_DIR = data_dir
        self.batch_size = batch_size
        self.seq_len = seq_len
        self.shuffle = shuffle
        self.n_samples = len(self.data) 
        self.n_batches = self.n_samples // self.batch_size
        self.on_epoch_end()

    
    def __len__(self):
        """
            Return number of batches per epoch
        """
        return self.n_batches
    

    def __getitem__(self, idx):
        """
            Return batch at position idx
        """
        if idx >= self.n_batches:
            raise IndexError
        batch = self.data[idx * self.batch_size:(idx + 1) * self.batch_size]
        X, y = self.__data_generation(batch)
        return X, y


    def __data_generation(self, batch):
        """
            Generates data containing batch_size samples
        """
        X = []
        y = []
        for i in tqdm(batch):
            img, f = self.load_image(f"{self.DATA_DIR}/{i[1]}")
            f.close()
            X.append(np.array(img))
            y.append(i[2])
        return X, y


    def load_image(self, image_path):
        """
            Load images from given path
        """
        with open(image_path, "rb") as f:
            img = Image.open(f)
            return img.convert('RGB'), f


    def on_epoch_end(self):
        """
            Shuffle data after each epoch
        """
        if self.shuffle:
            self.data = np.random.shuffle(self.data)
