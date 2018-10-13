


import numpy as np
import pandas as pd

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint




file = 'fleursdumal.txt'
poetry = open(file, encoding = "utf8").read().lower()




import re
special_chars = ['0','\ufeff','-','_']
poetry = re.sub('|'.join(special_chars), "", poetry)
chars =  sorted(list(set(poetry)))
char_to_num = dict((char,n) for n,char in enumerate(chars))
num_to_char = dict((n, char) for n,char in enumerate(chars))




X = []
Y = [] 
whole_length = len(poetry)
seq_len = 100
for i in range(0, whole_length - seq_len):
    sequence = poetry[i:i + seq_len]
    target = poetry[i + seq_len]
    Y.append(char_to_num[target])
    
    X.append([char_to_num[char] for char in sequence])




X_shaped = np.reshape(X, (len(X), seq_len, 1))
#scaling
X_shaped = X_shaped/float(len(chars))
Y_target = np_utils.to_categorical(Y)




model = Sequential(
[LSTM(700, input_shape=(X_shaped.shape[1], X_shaped.shape[2]), return_sequences=True),
Dropout(0.2),
LSTM(700, return_sequences = True),
Dropout(0.2),
 LSTM(700),
 Dropout(0.2),
Dense(Y_target.shape[1], activation='softmax')]
)

model.compile(loss = 'categorical_crossentropy', optimizer = 'adam')




filepath="weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
checkpoints = [checkpoint]
model.fit(X_shaped, Y_target, epochs = 30, batch_size = 264, callbacks = checkpoints)




filename = "weights-improvement-30-0.3182.hdf5"
model.load_weights(filename)
model.compile(loss='categorical_crossentropy', optimizer='adam')
start_point = np.random.randint(0, len(X_shaped)-1)
string = X_shaped[start_point]
Poem = ''
for i in range(800):
    x = np.reshape(string,(1,len(string), 1))
    x = x / float(len(chars))
    pred_index = np.argmax(model.predict(x, verbose=0))
    result = num_to_char[pred_index]
    print(result)
    Poem = Poem + result
    string.append(pred_index)
    string = string[1:len(string)]
        
f = open("Poem.txt", "w+")
f.write(Poem)
f.close()  

