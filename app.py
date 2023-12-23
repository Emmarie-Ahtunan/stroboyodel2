import streamlit as st
import numpy as np
import plotly.graph_objects as go
import os

# Function to generate a sine wave
def generate_sine_wave(x, frequency, amplitude=1, phase=0):
    return amplitude * np.sin(2 * np.pi * frequency * x + phase)


# Set up the Streamlit app
st.title('Interactive Sine Wave Animation')

# Explanation
st.sidebar.title('Explanation')
st.sidebar.write("""
This Streamlit app generates an interactive animation of a sine wave. 
Adjust the sliders to explore different parameters and observe the changes in the animated sine wave.

- **Time:** Determines the position in time, influencing the phase of the sine wave.
- **Frequency:** Controls the frequency of the sine wave.
- **Amplitude:** Adjusts the amplitude of the sine wave, determining its height.
- **Phase:** Modifies the phase of the sine wave, influencing its starting point.
- **Number of Frames:** Specifies the duration of the animation by setting the number of frames.

The animated sine wave is visualized using Plotly.
""")

# Create sliders for time, frequency, amplitude, phase, and number of frames
time_slider = st.sidebar.slider('Select Time (seconds)', 0.0, 10.0, 5.0, step=0.1, key='time_slider')
frequency_slider1 = st.sidebar.slider('Select Frequency 1 (Hz)', 1.0, 10.0, 1.0, step=0.1, key='frequency_slider1')
frequency_slider2 = st.sidebar.slider('Select Frequency 2 (Hz)', 1.0, 10.0, 2.0, step=0.1, key='frequency_slider2')
frequency_slider3 = st.sidebar.slider('Select Frequency 3 (Hz)', 1.0, 10.0, 3.0, step=0.1, key='frequency_slider3')
amplitude_slider = st.sidebar.slider('Select Amplitude', 0.1, 2.0, 1.0, step=0.1, key='amplitude_slider')
phase_slider = st.sidebar.slider('Select Phase', 0.0, 2*np.pi, 0.0, step=0.1, key='phase_slider')
num_frames_slider = st.sidebar.slider('Number of Frames', 1, 100, 30, key='num_frames_slider')

# Generate data for the animation frames
x = np.linspace(0, 2 * np.pi, 1000)
frames = [
    generate_sine_wave(x, frequency_slider1, amplitude_slider, phase_slider + time_slider),
    generate_sine_wave(x, frequency_slider2, amplitude_slider, phase_slider + time_slider),
    generate_sine_wave(x, frequency_slider3, amplitude_slider, phase_slider + time_slider)
]

# Create the animated plot with Plotly Express
fig = go.Figure()
for i in range(num_frames_slider):
    t = i / (num_frames_slider - 1)  # Normalize time from 0 to 1
    combined_frame = sum([frame * np.sin(t * np.pi + np.pi/2) for frame in frames])  # Combine frames with a sine function
    fig.add_trace(go.Scatter(x=x, y=combined_frame, mode='lines', name=f'Frame {i+1}'))

# Update layout to center the graph
fig.update_layout(
    title=f'Sine Wave Animation (Amplitude={amplitude_slider}, Phase={phase_slider}, Time={time_slider} seconds)',
    xaxis=dict(title='Time (seconds)'), yaxis=dict(title='Amplitude'),
    width=800, height=500,  # Set the width and height of the graph
    margin=dict(l=20, r=20, t=40, b=20),  # Adjust margin
)

# Display the animated plot in the center of the main content area
st.plotly_chart(fig, use_container_width=True)


# Display the animated plot
st.plotly_chart(fig)









