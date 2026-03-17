import numpy as np
import pandas as pd





def Simplify_split(df):
    df.loc[df.Gender == "male", ['Gender']] = "1"
    df.loc[df.Gender == "female", ['Gender']] = "0" # Managing Gender

    season = {
    "summer" : "0",
    "winter" : "1",
    "monsoon" : "2",
    "spring" : "3"

    } # Managing Seasons

    df['Season'] = df['Season'].replace(season) # Season Replaced

    # Managing Geographical Location
    df['Geographical locations'] = df['Geographical locations'].replace({
    "plains" : "0",
    "mountains" : "1",
    "coastal" : "2"
    })

    # Managing Holidays
    df['Holiday'] = df['Holiday'].replace({
        "Yes" : "1",
        "No" : "0"
    })

    
    brands = {'PUMA': '0', 'Lee': '1', 'Head Hunters': '2', 'Johnson & Johnson': '3', 'Wakefit': '4', 'Dabur Chyawanprash': '5', 'Manyavar Mohey': '6', 'Pepperfry': '7', 'Lee Cooper': '8', 'Libram': '9', 'Flying Machine': '10', 'SleepyCat': '11', 'Streax': '12', 'Lakme Ayurveda': '13', 'Forest Essentials': '14', 'Dove Hair': '15', 'Pepe Jeans London': '16', 'The Moms Co.': '17', 'Himalaya Liv.52': '18', 'Wildcraft': '19', 'Godrej Interio': '20', 'Patanjali Ayurved (Health Care)': '21', 'Lijoba': '22', 'Moov': '23', 'Kama Ayurveda': '24', 'Urban Ladder': '25', 'Allen Solly Woman': '26', 'Max': '27', 'Head & Shoulders': '28', 'Fastrack': '29', 'Sugar Cosmetics': '30', 'Parachute': '31', 'Dettol': '32', 'AmazonBasics': '33', 'U.S. Polo Assn. Women': '34', 'Khadi Essentials': '35', 'Whisper': '36', 'Levis Strauss & Co.': '37', 'Wild Stone': '38', 'Biovea': '39', 'Vero Moda': '40', 'Zandu': '41', 'HRX': '42', 'Mothercare': '43', 'Duroflex': '44', 'Spyker': '45', 'Stayfree': '46', 'Baidyanath': '47'}

    # Companies SUpported
    # replacing

    

    df['Brand of the product'] = df['Brand of the product'].replace(brands)

    return df.astype(float)



def Simplify_split_arr(array_2d):
    columnss = ['Number of clicks on similar products',
    'Number of similar products purchased so far',
    'Average rating given to similar products',
    'Gender',
    'Median purchasing price (in rupees)',
    'Rating of the product',
    'Brand of the product',
    'Customer review sentiment score (overall)',
    'Price of the product',
    'Holiday',
    'Season',
    'Geographical locations']

    df = pd.DataFrame(array_2d.reshape(-1, 1).T, columns=columnss)
    
    return Simplify_split(df)

    

def Simplify_pred(predictions : np.array) -> np.array:
    predictions = predictions.reshape(-1)
    predictions = np.where(predictions > 0.5, 1, 0)

    return predictions
