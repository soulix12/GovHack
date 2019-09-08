from flask import Flask
import pandas as pd
import numpy as np 

app = Flask(__name__)

@app.route('/')
def hello_world():

    df1 = pd.read_excel("", usecols = "B, H", header=1, skipfooter=3)
    
    return 'Hello, World! Hello darkness my old friend.' 

if __name__ == '__main__':
    app.run()
    app1.run() 
