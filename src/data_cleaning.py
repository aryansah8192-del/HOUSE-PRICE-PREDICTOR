import pandas as pd

def clean_data(df):

    cols_to_drop = [
        'facing',
        'Description',
        'overlooking',
        'Society',
        'Car Parking',
        'Plot Area',
        'Super Area',
        'Dimensions'
    ]

    df = df.drop(columns=cols_to_drop)

    df = df.rename(columns={
        "Amount(in rupees)": "Total Price",
        "Price (in rupees)": "Price per sqft"
    })

    # Fill missing Price per sqft
    price_mean = df['Price per sqft'].mean()

    df['Price per sqft'] = df['Price per sqft'].fillna(price_mean)

    # Carpet Area cleaning
    df['Carpet Area'] = (
        df['Carpet Area']
        .str.replace("sqft", "")
        .str.strip()
    )

    df['Carpet Area'] = pd.to_numeric(
        df['Carpet Area'],
        errors='coerce'
    )

    carpet_mean = df['Carpet Area'].mean()

    df['Carpet Area'] = df['Carpet Area'].fillna(carpet_mean)

    return df