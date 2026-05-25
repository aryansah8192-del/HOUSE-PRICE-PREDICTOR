import matplotlib.pyplot as plt
import numpy as np

from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)

def evaluate_model(y_test, y_pred):

    print("R2 Score:", r2_score(y_test, y_pred))

    print("MAE:", mean_absolute_error(y_test, y_pred))

    print("MSE:", mean_squared_error(y_test, y_pred))

    print(
        "RMSE:",
        np.sqrt(mean_squared_error(y_test, y_pred))
    )

    print(
        "Model Accuracy:",
        r2_score(y_test, y_pred) * 100,
        "%"
    )

    # Scatter Plot
    plt.figure(figsize=(8,6))

    plt.scatter(y_test, y_pred)

    plt.plot(
        [y_test.min(), y_test.max()],
        [y_test.min(), y_test.max()],
        color='red',
        linewidth=2
    )

    plt.xlabel("Actual Price")

    plt.ylabel("Predicted Price")

    plt.title("Actual vs Predicted Prices")

    plt.grid(True)

    plt.show()