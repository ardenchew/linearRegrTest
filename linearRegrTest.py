# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:05:06 2017

@author: arden
"""

def linearFit(xData, yData):
    """A linear fitting method for a given data set.
    
    Paramaters:
        xData - The x argument data.
        yData - The y argument data.
        
        NOTE - xData and yData should be ordered so that data pairs match given
        positions.
        
    Returns:
        slope - The slope of the ideal linear fit.
        yInt - The y-intercept of the ideal linear fit.
        r2 - The R-squared value between the data and fitted linear model.
    """
    pass

def fittedLinearRegr(xTrain, yTrain):
    """A method to create an skl LinearRegression object from training data.
    
    Paramaters:
        xTrain - The x argument data to train the model.
        yTrain - The y argument data to train the model.
        
        NOTE - trainX and trainY should be ordered so that data pairs match given
        positions.
        
    Returns:
        regr - The trained regression object.
        
        NOTE - This object is of type sklearn.linear_model.LinearRegression()
    """
    pass

def regrYPredict(regr, xData):
    """A method to predict yData using a linear regression model, given xData.
    
    Paramaters:
        regr - The linear regression model to use.
        xData - The x argument data to base the prediction off of.

    Returns:
        yData - The predicted y argument data based off the passed xData.
    """
    pass
 

def main():
    """Creating, testing, and plotting a linear regression model.
    
    Should be called as follows:
        $>python linearRegrTest.py xTrain yTrain xTest yTest
    
    This will print out statistical data about the test data,
    while also coomparing the data to the prediction based off of the trained
    regression model.
    
    """
    
    #store input variables, error if incorrect number of arguments
    from sys import argv
    if (len(argv) != 5):
        raise ValueError("4 Input datasets expected.")
    xTrain, yTrain = argv[1], argv[2]
    xTest, yTest = argv[3], argv[4]

    pass

if __name__ == '__main__':
    main()
    
    
    
    
        