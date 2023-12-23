import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Function to generate sine wave
def generate_sine_wave(x, frequency, amplitude, phase):
    return amplitude * np.sin(frequency * x + phase)

# Set up the Streamlit app
st.title('Interactive Sine Wave Animation')

# Introduction
st.write("""
Welcome to the Interactive Sine Wave Animation tutorial! This tutorial will guide you through exploring different parameters of a sine wave using sliders.

Let's get started!
""")

# Educational Questions
questions = [
    "What is the effect of changing the amplitude of the sine wave?",
    "How does adjusting the phase impact the sine wave?",
    "What happens when you increase the frequency of the sine wave?",
    "How does changing the time parameter affect the animated sine wave?",
    "What is the role of the number of frames in the animation?",
    "Can you create a standing wave by combining multiple sine waves?",
    "How does the animation respond to simultaneous changes in amplitude and frequency?",
    "What is the impact of increasing the number of frames on animation quality?",
    "What happens when you set all frequencies to the same value?",
    "How does altering the phase affect the interference of multiple sine waves?"
]

# Tutorial for each question
for i, question in enumerate(questions, start=1):
    st.sidebar.subheader(f'Step {i}: {question}')
    st.sidebar.write(f"In this step, we'll explore the following question:\n\n*{question}*")

    # Sliders for interaction
    amplitude_slider = st.sidebar.slider('Select Amplitude', 0.1, 2.0, 1.0, step=0.1, key=f'amplitude_slider_{i}')
    frequency_slider = st.sidebar.slider('Select Frequency (Hz)', 1.0, 10.0, 1.0, step=0.1, key=f'frequency_slider_{i}')
    phase_slider = st.sidebar.slider('Select Phase', 0.0, 2*np.pi, 0.0, step=0.1, key=f'phase_slider_{i}')
    num_frames_slider = st.sidebar.slider('Number of Frames', 1, 100, 30, key=f'num_frames_slider_{i}')

    # Generate data for the animation frame
    x = np.linspace(0, 2 * np.pi, 1000)
    frame = generate_sine_wave(x, frequency_slider, amplitude_slider, phase_slider)

    # Create the plot for the current step
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=frame, mode='lines', name='Sine Wave'))
    fig.update_layout(title=f'Sine Wave Animation (Amplitude={amplitude_slider}, Frequency={frequency_slider}, Phase={phase_slider})',
                      xaxis=dict(title='Time (seconds)'), yaxis=dict(title='Amplitude'))
    st.plotly_chart(fig, use_container_width=True)

    # Next Step button
    if st.sidebar.button('Next Step'):
        st.sidebar.success(f'Step {i} completed! Move on to the next step.')

# End of the tutorial
st.write("""
Congratulations! You've completed the Interactive Sine Wave Animation tutorial. Feel free to ask any additional questions or explore the app further.
""")










