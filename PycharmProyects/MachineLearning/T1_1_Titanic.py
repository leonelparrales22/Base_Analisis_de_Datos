import pandas as pd
from IPython.display import display, HTML

##PATH RELATIVO
data = pd.read_csv('../../datasets/titanic/titanic3.csv', sep=',')

display(data)
