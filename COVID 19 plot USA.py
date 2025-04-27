import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons
from datetime import datetime, timedelta

# Generate synthetic data without pandas
def generate_covid_data():
    np.random.seed(42)
    n_days = 365 * 3  # 3 years of data
    dates = [datetime(2020, 1, 1) + timedelta(days=i) for i in range(n_days)]
    
    # Simulate wave-like cases
    t = np.linspace(0, 6*np.pi, n_days)
    cases = (np.sin(t) + 1) * 50000 + 10000 + np.random.normal(0, 5000, n_days)
    cases = np.cumsum(np.abs(cases)).astype(int)
    
    deaths = (cases * 0.02).astype(int) + np.random.poisson(50, n_days)
    hospitalizations = (cases * 0.1).astype(int) + np.random.poisson(200, n_days)
    
    return {
        'date': np.array(dates),
        'cases': cases,
        'deaths': deaths,
        'hospitalizations': hospitalizations
    }

class CovidVisualizer:
    def __init__(self, data):
        self.data = data
        self.fig, self.ax = plt.subplots(figsize=(12, 6))
        plt.subplots_adjust(bottom=0.25)
        
        # Create widgets
        ax_slider = plt.axes([0.2, 0.1, 0.6, 0.03])
        ax_radio = plt.axes([0.2, 0.15, 0.15, 0.1])
        
        self.slider = Slider(ax_slider, 'Days', 30, 365, valinit=180)
        self.radio = RadioButtons(ax_radio, ('cases', 'deaths', 'hospitalizations'))
        
        self.metric = 'cases'
        self.update_plot()
        
        self.slider.on_changed(self.update_days)
        self.radio.on_clicked(self.update_metric)
    
    def update_plot(self):
        self.ax.clear()
        days = self.slider.val
        end_idx = len(self.data['date'])
        start_idx = max(0, end_idx - int(days))
        
        dates = self.data['date'][start_idx:end_idx]
        values = self.data[self.metric][start_idx:end_idx]
        
        self.ax.plot(dates, values, 'b-')
        self.ax.set_title(f"USA COVID-19 {self.metric} (Last {int(days)} Days)")
        self.ax.grid(True)
        plt.xticks(rotation=45)
        self.fig.canvas.draw_idle()
    
    def update_days(self, val):
        self.update_plot()
    
    def update_metric(self, label):
        self.metric = label
        self.update_plot()

# Run the visualization
data = generate_covid_data()
viz = CovidVisualizer(data)
plt.show()