from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor

def train_model(df):

    x = df.drop(columns=['Total Price'])

    y = df['Total Price']

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.1,
        random_state=42
    )

    model = XGBRegressor(
        n_estimators=500,
        learning_rate=0.03,
        max_depth=10,
        subsample=0.9,
        colsample_bytree=0.9,
        random_state=42
    )

    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    return model, x_test, y_test, y_pred