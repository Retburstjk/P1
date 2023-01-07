import  numpy  as np
import pandas as pd
from  sklearn import datasets
from  sklearn import linear_model
from  sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt


for df in pd.read_csv('OCRDF.csv' , chunksize=1000):
  print("CHUNK DF")
  print(df)


def index_o (object  , name=""):
  iteration = 0
  for i in object :
    if (i == name) and (i < len(object)):
      return iteration
    elif i ==len(object):
      print(f"{name} not found,try another name")
      break
    else:
      iteration += 1

