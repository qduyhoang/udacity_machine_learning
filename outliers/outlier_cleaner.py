#!/usr/bin/env python3


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    ### your code goes here
    import math
    cleaned_data = []


    sorted_error = []
    for true_y, predicted_y in zip( net_worths, predictions ):
        sorted_error.append( abs( true_y - predicted_y ) )
    sorted_error.sort()

    #number of training data to be kept
    num_data_kept = int( math.floor( (len(sorted_error) * 0.9) ) )
    highest_error = sorted_error[num_data_kept:]


    for i in range(len(predictions)):
        err = abs( net_worths[i] - predictions[i] )
        if err not in highest_error:
            cleaned_data.append( ( ages[i], net_worths[i], err ) )
    
    return cleaned_data

