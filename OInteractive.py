import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

class SignalGenerator:
    """Base class for signal generation"""
    def __init__(self, frequency=1.0, amplitude=1.0, phase=0):
        self.frequency = frequency
        self.amplitude = amplitude
        self.phase = phase
    
    def generate(self, time):
        raise NotImplementedError("Subclasses must implement this method")
        
    def plot(self, time):
        signal = self.generate(time)
        plt.figure(figsize=(10, 4))
        plt.plot(time, signal)
        plt.title(f"{self.__class__.__name__} Signal")
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.show()

class SineWave(SignalGenerator):
    """Subclass for sine wave generation"""
    def generate(self, time):
        return self.amplitude * np.sin(2 * np.pi * self.frequency * time + self.phase)

class SquareWave(SignalGenerator):
    """Subclass for square wave generation"""
    def generate(self, time):
        return self.amplitude * np.sign(np.sin(2 * np.pi * self.frequency * time + self.phase))

# Create time vector
time = np.linspace(0, 1, 1000)

# Create and plot signals
sine = SineWave(frequency=5, amplitude=1.5)
square = SquareWave(frequency=2, amplitude=0.8)

sine.plot(time)
square.plot(time)