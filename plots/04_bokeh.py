import numpy as np
from bokeh.plotting import figure, show, output_file

x = np.linspace(0, 4 * np.pi, 200)

output_file("04_bokeh.html")
p = figure(title="Damped oscillator", x_axis_label="time (s)",
           y_axis_label="position (m)", width=700, height=400)
p.line(x, np.exp(-0.2 * x) * np.cos(2 * x), line_width=2, legend_label="damped")
p.line(x, np.cos(2 * x), line_width=1, line_dash="dashed", color="gray", legend_label="no damping")
show(p)
