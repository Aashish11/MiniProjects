import yfinance as yf
import pandas as pd
import numpy as np

class QuantData:
    def __init__(self):
        self.ticker = yf.Tickers('SNOW')
        self.data = yf.download(tickers=('SNOW'),period='1y',interval='1d',group_by='ticker',auto_adjust=True,prepost=False)
        print(self.data)
        self.df = pd.DataFrame(self.data)
        print(self.df.tail(1))
        
        
    def find_z(self):
        mean = self.df['Close'].mean()
        z_from_mean = (self.df['Close'].tail(1) - mean) / np.std(self.df['Close'])
        print("BTC-USD",self.df['Close'].tail(1),z_from_mean)
    
    
    
if __name__ == '__main__':
    
    QGD = QuantData()
    QGD.find_z()    