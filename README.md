# Handwriting Classifier
Using neural networks, this project can classify any image of a digit, from 0 through 9. This project gets a dataset, trains a deep learning model, and saves the model. It has an accuracy of 97.9%. The model alone is available as a saved TensorFlow model in `saved_model.pb`. 
This model is available as a game, where users can draw numbers as the AI tries to guess them. Instructions for running the program are below.

## Running the program
First, make sure you have Python 3 and pip installed on your computer and clone this repository. Then, open a terminal or command prompt window and `cd` to the directory you cloned to. Install the necessary dependencies by running `pip install -r requirements.txt`. To run the game, you can then type `python app.py`, wait for the TensorFlow model to load, and start playing when the drawing window appears. To play, start by drawing a number in the window. Then, use the `p` key make a prediction. Respond to the prompt in the terminal or command prompt to confirm if the guess was correct or incorrent. Use the `c` key to clear the window and redraw. When you are done, hit `q` to quit and get a summary of how accurate the model was.

## How to Train
To retrian the model on your own, you can run the Jupyter Notebook `Image_Classifier_Tf.ipynb`. A simpler version using SKLearn is also available at `Image_Classifier_Basic.ipynb`, but has a lower accuracy. After training, the saved model is used in `app.py`.