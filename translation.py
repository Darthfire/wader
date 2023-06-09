# -*- coding: utf-8 -*-
"""translation for semeval.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Kqdk442vAfazQXxVDJNr4NLy48TocCnP
"""

!pip install googletrans==3.1.0a0

from googletrans import Translator
from google.colab import files
import pandas as pd

translator= Translator()

#  load df from csv file
df = pd.read_csv('/content/train.csv')

#  translate function to translate a sentence "sent" from src language to target language
#  src and dest must be language codes like en es hi etc

def translate(sent, src, dest):
  return translator.translate(sent, dest=dest).text

translate('What up', 'en', 'ar')

#  complete function
def translation(df,src,dest):
  df_copy = df.copy()


  df_copy['text'] = df_copy['text'].map(lambda x:translate(x,src,dest))

  filename=dest+"_from_"+src+".csv"

  df_copy.to_csv(filename)
  files.download(filename)

  # df_copy['text'] = df_copy['text'].map(lambda x:translate(x,dest,src))

  # filename=src+"_via_"+dest+".csv"

  # df_copy.to_csv(filename)
  # files.download(filename)

#  Apply function:

#  1. use 5-6 intermeidate languages (choose any) and conver "en"--> "intermeidate like hindi (hi) or spanish (es)"--> "en" in that case function will look like translation(df,src, dest, intermediate)
#  2. translate current src to all target languages in the dataset "en"--> "es" etc in that case function will look like translation(df,src, dest)

#  sometimes rate limits apply in that case use different gmail ids to run the code

# We have to make the dataset for english
# we will do two things:
# 1. spanish, french, chinese etc---> english
# 2. english ---> (intermediate) german ---> english ]]--> This is called back translation
#. Chinese (zh), english(en), french (fr), portugese (pt), spanish(es), italian (it)

#  source language 
#  use language codes: eg for english its "en"

lang = "Chinese"
code = "training"

# score threshold
score = 3.2

#  select sentences
df_to_trans = df.query('language == "Chinese" and label > 3.2 ')

langs= ["fr","es","it","pt","zh-CN","en"]

for l in langs:
  if l!=code:
    translation(df_to_trans,code,l)

translation(df,code,'ar')

