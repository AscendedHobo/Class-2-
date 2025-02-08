import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_event_data(csv_path, event_type=None):
    """
    Load CSV data and filter by event type if provided.
    """
    df = pd.read_csv(csv_path)
    
    if event_type:
        df = df[df['event type'] == event_type]
    
    return df.dropna(subset=["X coord", "Y coord"])  # Drop rows that still have no coordinates

def plot_scatter(df, title="Event Scatter Plot"):
    """
    Generate a scatter plot for event locations.
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(df['X coord'], df['Y coord'], alpha=0.5, c='red', label='Events')
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_heatmap(df, title="Event Heatmap"):
    """
    Generate a heatmap for event density.
    """
    plt.figure(figsize=(8, 6))
    sns.kdeplot(x=df['X coord'], y=df['Y coord'], cmap='Reds', fill=True, alpha=0.7)
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.title(title)
    plt.grid(True)
    plt.show()

# Example usage
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get directory of this script
    csv_path = os.path.join(script_dir, "filtered_combat_log.csv")  # Relative path to CSV
    event_type = "UNIT_DIED"  # Example: Change to any event type to filter
    
    df = load_event_data(csv_path, event_type)
    
    if not df.empty:
        plot_scatter(df, title=f"Scatter Plot for {event_type}")
        plot_heatmap(df, title=f"Heatmap for {event_type}")
    else:
        print(f"No events found for type: {event_type}")
