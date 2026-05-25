import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(df):

    # Boxplot
    plt.figure(figsize=(8,5))

    sns.boxplot(x=df['Price per sqft'])

    plt.title("Price per sqft Distribution")

    plt.show()

    # Heatmap
    plt.figure(figsize=(12,8))

    sns.heatmap(
        df.select_dtypes(include=['number']).corr(),
        annot=True,
        cmap='coolwarm'
    )

    plt.title("Correlation Heatmap")

    plt.show()