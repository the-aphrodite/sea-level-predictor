import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    
    plt.scatter(x, y)
    
    slope, intercept, _, _, _ = linregress(x, y)
    years_extended = np.arange(x.min(), 2051)
    plt.plot(years_extended, intercept + slope * years_extended, 'r', label='Fit: All Data')
    
    recent_data = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    years_recent = np.arange(2000, 2051)
    plt.plot(years_recent, intercept_recent + slope_recent * years_recent, 'g', label='Fit: From 2000')
    
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.savefig('sea_level_plot.png')
    return plt.gca()
