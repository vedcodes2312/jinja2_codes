from jinja2 import Environment, FileSystemLoader
import numpy as np; 
import matplotlib.pyplot as plt
from scipy.stats import skew,kurtosis

# numpy data

x = np.linspace(0,10,100)
y = np.sin(x) + 0.5 * np.random.randn(100)

# dictionary for statistical methods
stats = {
    "mean":float(np.mean(y)),
    "std":float(np.std(y)),
    "min":float(np.min(y)),
    "max":float(np.max(y)),
    "median":float(np.median(y)),
    "var":float(np.var(y)),
     "skew":float(skew(y)),            
    "kurt":float(kurtosis(y)),
#     "q1":float(np.percentile(y,25)),
#     "q3":float(np.percentile(y,75)),
#     "iqr":float(np.percentile(y,75) - np.percentile(y,25)),
#     "iqr":float(np.percentile(y,75) - np.percentile(y,25)),
}

# matplotlib part 
plt.figure(figsize=(10,5))
plt.plot(x,y,color="blue",linewidth=2)
plt.title("numpy signal")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid(True)
plt.tight_layout()
plt.savefig("numpy_signal.png")
plt.close()

# jinja rendering
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("report.html")

output = template.render(
    title = "numpy matplotlib demonstration",
    stats = stats,
    image_path = "numpy_signal.png"
)

# file writing
with open("output.html","w",encoding="utf-8") as f:
    f.write(output)
