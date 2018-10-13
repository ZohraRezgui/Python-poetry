# Poetry Generation

This repo is where I put my poetry generation experiments based on poems written by poets I admire :) . 

## Baudelaire Generation (french)

[BaudelairePoetry.py](https://github.com/ZohraRezgui/Python-poetry/blob/master/BaudelairePoetry.py)

A three-layer LSTM character-mapped model with 700 units in each layer. The training data is the very famous poetry volume "Les fleurs du mal"
(The Flowers of Evil) written by my all time favourite french poet Charles Baudelaire. It's available on [Project Gutenberg](https://www.gutenberg.org/) in french where you can also find plenty of other books in text format. I uploaded it to the repo as well
([fleursdumal.txt](https://github.com/ZohraRezgui/Python-poetry/blob/master/fleursdumal.txt) ) 

Here you'll find two samples of generated Baudelaire Poetry:
([BaudelaireSample1.txt](https://github.com/ZohraRezgui/Python-poetry/blob/master/BaudelaireSample1.txt) ) 
([BaudelaireSample2.txt](https://github.com/ZohraRezgui/Python-poetry/blob/master/BaudelaireSample2.txt) ) 

These were obtained after 30 epochs of training, with a loss of 0.3182.


## Resources

[Keras LSTM Text Generation Example](https://github.com/keras-team/keras/blob/master/examples/lstm_text_generation.py)
