import nbformat as nbf

# Create a new Jupyter notebook
nb = nbf.v4.new_notebook()

# Read the contents of the data_visualization.py script
with open('data_visualization.py', 'r') as f:
    code = f.read()

# Create a new code cell with the contents of the data_visualization.py script
code_cell = nbf.v4.new_code_cell(code)

# Add the code cell to the notebook
nb['cells'].append(code_cell)

# Write the notebook to a new file
with open('data_visualization.ipynb', 'w') as f:
    nbf.write(nb, f)

print("Conversion to Jupyter notebook completed successfully.")
