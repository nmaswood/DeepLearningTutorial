from sklearn import linear_model
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

from matplotlib import cm

from matplotlib.ticker import LinearLocator, FormatStrFormatter

def plot_quadratic(function, simple = False):

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Make data.
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)

    function = lambda m, b: ((X - ((Y * m) + b)) ** 2) / 2

    Z = function(X,Y) if not simple else X**2 + Y**2

    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)

    # Customize the z axis.
    ax.zaxis.set_major_locator(LinearLocator(10))
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()

def do_scikit_learn_regression(data, verbose = False):
    
    """
    
    Uses scikit learn as a black box to perform linear regression
    
    """
    
    
    regr = linear_model.LinearRegression()

    x = data['c'].values.reshape(100,1)
    y = data['f'].values.reshape(100,1)
    
    regr.fit(x, y)
    
    if verbose:

        string = '\n'.join((
            f'Coefficient of {regr.coef_[0][0]} compared to actual {9/5}',
            f'Intercept of {regr.intercept_[0]} compared to actual {32}'
        ))

        print (string)

    return regr.coef_[0][0], regr.intercept_[0]

def plot_and_compare(xs,ys, m,b):

    """
    Plot xs vs ys

    And also plt xs vs (line created with coefficent and intercept)

    """

    plt.scatter(xs, ys, color = 'blue')

    plt.plot(xs, (xs * m) + b, color = 'red')


def convert(temp_in_c):
    
    """ converts a temperature from celsius to farenheit
    
    Args:
        temp_in_c<int>
    
    Return:
        the temperature in farenheit<int>
    """
    
    return temp_in_c * (9/5) + 32

def measurements():
    
    """
    
    For number_of_days days declares the temperature and measures it with noise
    
    Return:
        A dataframe containing the actual temp in c the measured temp in f
    
    """
    
    number_of_days = 100


    # the temperature is usually 20 but can vary by 10 degrees at a time
    
    average_temperature, standard_deviation = 20, 10

    # ground truth temperature

    _c = np.random.normal(average_temperature, standard_deviation, number_of_days)

    # the therometer is usually 2 off but can be off by up to 4 degrees
    
    average_jankiness, standard_jankiness = 2, 2
    
    temperature_deviations = np.random.normal(average_jankiness, standard_jankiness, number_of_days)

    c  = _c + temperature_deviations
  
    _f = convert(_c)

    average_jankiness, standard_jankiness = 2.4, 3.3

    therometer_deviations = np.random.normal(average_jankiness, standard_jankiness, number_of_days)
    
    f = _f + therometer_deviations
        
    return pd.DataFrame({
        'c': c,
        'f': f,
    })
    
if __name__ == "__main__":


    f = lambda m, b: ((ys - ((xs * m) + b)) ** 2) / 2
    plot_quadratic(f)

