import pandas as pd

def get_weather_data(filename='weatherAUS.csv', 
                     location='C:/Users/kovus/Documents/Projects/Aussie-Rain/data/weatherAUS.csv'):
    """Get the Australian weather data and drop RISK_MM column to prevent data leakage
    Parameters
    ----------
    filename: string(optional)
        location to save the data
    location: string(optional)
        location of the csv file on my machine
        
    Returns
    -------
    data: pandas.DataFrame
        Fremont bridge data
    """
    # read in the data from local folder
    data = pd.read_csv('C:/Users/kovus/Documents/Projects/Aussie-Rain/data/weatherAUS.csv', index_col='Date')
    
    # drop RISK_MM to prevent data leakage
    # convert Date column to datetime format and use as index
    try:
        data.drop(['RISK_MM'], axis=1, inplace=True)
        data.index = pd.to_datetime(data.index, format='%Y-%m-%d')
    except ValueError:
        data.index = pd.to_datetime(data.index)
        print('Something is wrong with the dataset')
    
    return data