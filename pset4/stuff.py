def generate_models(x, y, degs):
    """
    Generate regression models by fitting a polynomial for each degree in degs
    to points (x, y).
    Args:
        x: a list with length N, representing the x-coords of N sample points
        y: a list with length N, representing the y-coords of N sample points
        degs: a list of degrees of the fitting polynomial
    Returns:
        a list of numpy arrays, where each array is a 1-d array of coefficients
        that minimizes the squared error of the fitting polynomial
    """
    ourClimate = Climate('data.csv')
    for year in x:
        y.append(np.mean(ourClimate.get_yearly_temp('CHICAGO', year)))
    np_y = np.array(y)

    models = []
    for degree in degs:
        model = pylab.polyfit(x, y, degree)
        models.append(model)
    return models
