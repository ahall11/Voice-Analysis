import tensorflow as tf
import os

def train(training_path):
  labels = [x[0] for x in os.walk(training_path)]
  print(lables)

