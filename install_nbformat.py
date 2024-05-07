import subprocess
import sys

# Function to install packages using pip
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install nbformat
install('nbformat')

print("nbformat installed successfully.")
