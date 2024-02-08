import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn import metrics
import matplotlib.pyplot as plt

def execute_linear_regression():

    # Loading dataset
    data = pd.read_csv('sleep_data.csv')

    features = data[['Physical Activity Level', 'Stress Level']]
    target = data['Quality of Sleep']

    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    model = LinearRegression()

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    rs = metrics.r2_score(y_test, y_pred)*100

    coefficients = model.coef_
    intercept = model.intercept_
    #print(coefficients)
    #print(intercept)
    line_equation = f"{coefficients[0]:.2f} * Physical Activity + {coefficients[1]:.2f} * Stress Level + {intercept:.2f}"
    print("Line Equation:", line_equation)

    plt.scatter(X_test['Physical Activity Level'], y_test, color='blue', label='Actual')
    plt.scatter(X_test['Physical Activity Level'], y_pred, color='red', label='Predicted')

    x_range = np.linspace(X_test['Physical Activity Level'].min(), X_test['Physical Activity Level'].max(), 100)
    y_range = coefficients[0] * x_range + coefficients[1] * X_test['Stress Level'].mean() + intercept
    plt.plot(x_range, y_range, color='green', label='Linear Regression Line')
    plt.xlabel('Physical Activity Level')
    plt.ylabel('Quality of Sleep')
    plt.legend()
    plt.title('Linear Regression: Actual vs. Predicted with Regression Line')
    plt.show()
    return {'coefficient': model.coef_.tolist(), 'intercept': model.intercept_, 'rs':rs, 'line_equation':line_equation}

#execute_linear_regression()