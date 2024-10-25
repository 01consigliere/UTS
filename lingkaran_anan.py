import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

st.title('Data Acak yang Berubah Setiap Tombol Ditekan')

def generate_data(n=50):
    """Generates random data for the scatter plot."""
    return np.random.rand(n, 2) - 0.5, np.random.rand(n) * 0.2 + 0.1  # Size is between 0.1 and 0.3


def plot_data(data, size, colors):
    """Plots the scatter plot with random circles."""
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(-1.05, 1.05)
    ax.set_ylim(-1.05, 1.05)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_aspect("equal")
    ax.grid(True, linestyle="--", color="lightgray")
    ax.add_patch(Circle((0, 0), 1, fill=False, color="lightcoral"))

    for i in range(len(data)):
        x, y = data[i]
        circle = Circle((x, y), size[i], color=colors[i], alpha=0.5)
        ax.add_patch(circle)
        ax.plot([0, x], [0, y], linestyle="--", color="green", alpha=0.5, linewidth=0.8)

    st.pyplot(fig)

if __name__ == "__main__":
    data, size = generate_data()
    colors = np.random.rand(len(data), 3)  # Generate random colors
    plot_data(data, size, colors)

    if st.button("Generate New Data"):
        data, size = generate_data()
        colors = np.random.rand(len(data), 3)  # Generate random colors
        plot_data(data, size, colors)
