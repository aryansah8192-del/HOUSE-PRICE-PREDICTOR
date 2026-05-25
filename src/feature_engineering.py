import pandas as pd

def convert_price(x):

    if pd.isna(x):
        return None

    x = str(x).replace(",", "").strip()

    if x.lower() in ["call for price", "price on request"]:
        return None

    if "Cr" in x:
        return float(x.replace("Cr", "").strip()) * 10000000

    elif "Lac" in x:
        return float(x.replace("Lac", "").strip()) * 100000

    else:
        return float(x)

def feature_engineering(df):

    # Status Encoding
    df['Status'] = df['Status'].apply(
        lambda x: 1 if x == "Ready to Move" else 0
    )

    # Floor splitting
    df['Floor'] = df['Floor'].astype(str)

    split_df = df['Floor'].str.split(
        " out of ",
        expand=True,
        n=1
    )

    df['Floor'] = split_df[0]
    df['Total_Floors'] = split_df[1]

    df['Floor'] = pd.to_numeric(
        df['Floor'],
        errors='coerce'
    )

    df['Total_Floors'] = pd.to_numeric(
        df['Total_Floors'],
        errors='coerce'
    )

    df['Floor'] = df['Floor'].fillna(df['Floor'].median())

    df['Total_Floors'] = df['Total_Floors'].fillna(
        df['Total_Floors'].median()
    )

    # Transaction Encoding
    df['Transaction'] = df['Transaction'].fillna('Unknown')

    df = pd.get_dummies(
        df,
        columns=['Transaction']
    )

    # Furnishing Encoding
    df['Furnishing'] = df['Furnishing'].map({
        'Unfurnished': 0,
        'Semi-Furnished': 0.5,
        'Furnished': 1
    })

    df['Furnishing'] = df['Furnishing'].fillna(0.5)

    # Bathroom
    df['Bathroom'] = df['Bathroom'].replace(">10", 10.5)

    df['Bathroom'] = pd.to_numeric(
        df['Bathroom'],
        errors='coerce'
    )

    df['Bathroom'] = df['Bathroom'].fillna(
        df['Bathroom'].median()
    )

    # Balcony
    df['Balcony'] = df['Balcony'].replace("> 10", 10.5)

    df['Balcony'] = pd.to_numeric(
        df['Balcony'],
        errors='coerce'
    )

    df['Balcony'] = df['Balcony'].fillna(
        df['Balcony'].median()
    )

    # Ownership Encoding
    own_map = {
        "Freehold": 4,
        "Leasehold": 3,
        "Co-operative Society": 2,
        "Power of Attorney": 1,
        "Unknown": 0
    }

    df['Ownership'] = df['Ownership'].fillna("Unknown")

    df['Ownership'] = df['Ownership'].map(own_map)

    # Convert Total Price
    df['Total Price'] = df['Total Price'].apply(convert_price)

    df['Total Price'] = pd.to_numeric(
        df['Total Price'],
        errors='coerce'
    )

    # Location Encoding
    df['location'] = df['location'].fillna("Unknown")

    df = pd.get_dummies(
        df,
        columns=['location'],
        drop_first=True
    )

    # Drop unwanted columns
    df = df.dropna(subset=['Total Price'])

    df = df.drop(columns=[
        'Price per sqft',
        'Index',
        'Title'
    ])

    return df