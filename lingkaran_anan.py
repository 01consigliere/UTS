import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random

st.title(':chipmunk: FISIKA KOMPUTASI AWAN :chipmunk:')
st.header('Anan Maulana (21022607255)')

# Fungsi untuk membuat grafik
def plot_data():
    # Generate random data
    n = 50
    x = np.random.uniform(-2, 2, n)
    y = np.random.uniform(-2, 2, n)
    radius = np.random.uniform(0.05, 0.2, n)
    colors = [plt.cm.get_cmap('tab20')(i) for i in range(n)]

    # Create plot
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(-2.1, 2.1)
    ax.set_ylim(-2.1, 2.1)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True, linestyle='--', color='lightgray')
    ax.set_aspect('equal')
    ax.set_facecolor('whitesmoke')
    for i in range(n):
        circle = plt.Circle((x[i], y[i]), radius[i], color=colors[i], alpha=0.5)
        ax.add_patch(circle)

    # Draw lines from the center of the circle to the edge of the plot
    for i in range(n):
        ax.plot([0, x[i]], [0, y[i]], color='lightgreen', linestyle='--', alpha=0.5)

    # Draw a circle with a radius of 1
    circle = plt.Circle((0, 0), 1, color='lightpink', fill=False, alpha=0.5)
    ax.add_patch(circle)

    return fig

# Create a button
button = st.button('Coba Tekan')

fig = plot_data()
st.pyplot(fig)
# If the button is pressed, plot the data
if button:
    fig = plot_data()
    st.write('Gambarnya Berubah kan? Coba Tekan Lagi')


