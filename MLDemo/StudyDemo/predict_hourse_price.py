# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 20:15:32 2016

@author: wang_wei52
"""


import pandas as pd
from sklearn import linear_model


def get_data(filename):
    data = pd.read_csv(filename)
    x_parameter = []
    y_parameter = []
    for single_square_feet, single_price_value in zip(data['square_feet'], data['price']):
        x_parameter.append([float(single_square_feet)])
        y_parameter.append(float(single_price_value))
    return x_parameter, y_parameter


def linear_model_main(x_parameters, y_parameters):
    # create linear regression object
    regression = linear_model.linearRegression()
    regression.fit(x_parameters, y_parameters)

