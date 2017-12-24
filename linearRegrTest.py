# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:05:06 2017

@author: arden
"""
from sklearn import linear_model

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
    #finding a linear fit for the given model
    regr = linear_model.LinearRegression()
    regr.fit(xData, yData)
    
    slope = regr.coef_[0]
    yInt = regr.intercept_
    
    #solving r2
    from sklearn.metrics import r2_score
    r2 = r2_score(yData, regr.predict(xData))
    
    return slope, yInt, r2

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
    regr = linear_model.LinearRegression()
    regr.fit(xTrain, yTrain)
    
    return regr

def regrYPredict(regr, xData):
    """A method to predict yData using a linear regression model, given xData.
    
    Paramaters:
        regr - The linear regression model to use.
        xData - The x argument data to base the prediction off of.

    Returns:
        yData - The predicted y argument data based off the passed xData.
    """
    yData = regr.predict(xData)
    return yData
 

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
    
    import matplotlib.pyplot as plt
    from sklearn.metrics import mean_squared_error, r2_score
    
    #initiate test data variables
    slope, yInt, r2 = linearFit(xTest, yTest)
    print("Test data initial statistics:")
    print("\tSlope:", slope)
    print("\tY-intercept:", yInt)
    print("\tR-squared:", r2)
    
    #get training based regression object
    regr = fittedLinearRegr(xTrain, yTrain)
    print("\nTraining based model statistics:")
    print("\tSlope:", regr.coef_[0])
    print("\tY-intercept:", regr.intercept_)
    
    #gather regression based precition
    yPred = regrYPredict(regr, xTest)
    print("\nEvaluation of model:")
    print("\tMean squared error:", mean_squared_error(yTest, yPred))
    print("\tVariance:", r_2(yTest, yPred))
    
    
    #plotting the regressin prediction
    plt.scatter(xTest, yTest, color='black')
    plt.plot(xTest, yPred, color='blue')
    
    plt.xticks(())
    plt.yticks(())
    plt.show()


if __name__ == '__main__':
    main()
    
    
    
    
        