import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Function to generate sine wave
def generate_sine_wave(x, frequency, amplitude, phase=0.0):
    return amplitude * np.sin(frequency * x + phase)

# Set up the Streamlit app
st.title('Interactive Sine Wave Animation')

# Introduction
st.write("""
Welcome to the Interactive Sine Wave Animation tutorial! This tutorial will guide you through exploring different parameters of a sine wave using sliders and user inputs.

Let's get started!
""")

# User input for multiple frequencies
selected_frequencies = st.multiselect('Select Frequencies (Hz)', [1.0, 2.0, 3.0], [1.0, 2.0])

# User input for amplitude
amplitude = st.slider('Select Amplitude', 0.1, 2.0, 1.0, step=0.1)

# Create the plot
x = np.linspace(0, 2 * np.pi, 1000)
fig = go.Figure()

# Initial plot with default frequencies
y = sum([generate_sine_wave(x, freq, amplitude) for freq in selected_frequencies])
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Combined Sine Wave'))

fig.update_layout(title=f'Sine Wave Animation (Amplitude={amplitude}, Frequencies={selected_frequencies})',
                  xaxis=dict(title='Time (seconds)'), yaxis=dict(title='Amplitude'))

# Display the animated plot
plotly_chart = st.plotly_chart(fig, use_container_width=True)

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

# Create the animated plot with Plotly Express
for i, question in enumerate(questions, start=1):
    unique_id = f"{i}_{question.replace(' ', '')}"  # Create a unique ID without underscores
    
    st.sidebar.subheader(f'Step {i}: {question}')
    st.sidebar.write(f"In this step, we'll explore the following question:\n\n*{question}*")

    # Sliders for interaction
    phase_slider = st.sidebar.slider('Select Phase', 0.0, 2*np.pi, 0.0, step=0.1, key=f'phase_slider_{unique_id}')
    num_frames_slider = st.sidebar.slider('Number of Frames', 1, 100, 30, key=f'num_frames_slider_{unique_id}')

    # Generate data for the animation frame
    y = sum([generate_sine_wave(x, freq, amplitude, phase_slider) for freq in selected_frequencies])

    # Update the plot for the current step
    fig.data = []  # Clear previous traces
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Combined Sine Wave'))
    fig.update_layout(title=f'Sine Wave Animation (Amplitude={amplitude}, Frequencies={selected_frequencies}, Phase={phase_slider})',
                      xaxis=dict(title='Time (seconds)'), yaxis=dict(title='Amplitude'))

    # Update the chart in the main content area
    plotly_chart.plotly_chart(fig)

    # Next Step button
    if i < len(questions):
        if st.sidebar.button(f'Next Step {i}'):
            st.sidebar.success(f'Step {i} completed! Move on to the next step.')
    else:
        if st.sidebar.button(f'Finish Tutorial'):
            st.sidebar.success('Congratulations! You\'ve completed the tutorial.')














