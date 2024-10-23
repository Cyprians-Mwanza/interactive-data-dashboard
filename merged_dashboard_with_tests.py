import panel as pn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load Panel extension
pn.extension()

# Example dataset (Replace with your own data)
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
df = pd.read_csv(url)

# Widgets for user interaction
dropdown = pn.widgets.Select(name='Select Column', options=list(df.columns))
slider = pn.widgets.IntSlider(name='Bins', start=5, end=50, step=5, value=10)
checkbox_grid = pn.widgets.Checkbox(name='Show Gridlines', value=True)
multi_select = pn.widgets.MultiSelect(name='Columns', options=list(df.columns), size=4)

# Plotting function for histogram
@pn.depends(dropdown, slider, checkbox_grid)
def create_histogram(column, bins, grid):
    plt.figure(figsize=(8, 6))
    df[column].hist(bins=bins, grid=grid)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    return plt.gcf()

# Plotting function for line graph
@pn.depends(dropdown)
def create_line_graph(column):
    plt.figure(figsize=(8, 6))
    df[column].plot(kind='line')
    plt.title(f'Line Graph of {column}')
    plt.xlabel('Index')
    plt.ylabel(column)
    return plt.gcf()

# Plotting function for pie chart
@pn.depends(dropdown)
def create_pie_chart(column):
    plt.figure(figsize=(8, 6))
    df[column].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
    plt.title(f'Pie Chart of {column}')
    plt.ylabel('')  # Hide the y-label
    return plt.gcf()

# Plotting function for doughnut chart
@pn.depends(dropdown)
def create_doughnut_chart(column):
    plt.figure(figsize=(8, 6))
    wedges, texts, autotexts = plt.pie(df[column].value_counts(), autopct='%1.1f%%', startangle=90)
    plt.setp(autotexts, size=10, weight="bold")
    plt.setp(texts, size=10)
    center_circle = plt.Circle((0, 0), 0.70, fc='white')  # Create center circle for doughnut chart
    fig = plt.gcf()
    fig.gca().add_artist(center_circle)
    plt.title(f'Doughnut Chart of {column}')
    plt.ylabel('')  # Hide the y-label
    return plt.gcf()

# Plotting function for bar graph
@pn.depends(dropdown)
def create_bar_graph(column):
    plt.figure(figsize=(8, 6))
    df[column].value_counts().plot(kind='bar')
    plt.title(f'Bar Graph of {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    return plt.gcf()

# Function to show correlations based on multi-select columns
@pn.depends(multi_select)
def show_correlations(selected_columns):
    if len(selected_columns) > 1:
        corr = df[selected_columns].corr()
        return pn.pane.DataFrame(corr)
    else:
        return "Please select at least two columns."

# Organize into tabs
dashboard = pn.Tabs(
    ('Overview', pn.Column(df.head(), df.describe())),
    ('Histogram', pn.Column(dropdown, slider, checkbox_grid, pn.panel(create_histogram))),
    ('Line Graph', pn.Column(dropdown, pn.panel(create_line_graph))),
    ('Pie Chart', pn.Column(dropdown, pn.panel(create_pie_chart))),
    ('Doughnut Chart', pn.Column(dropdown, pn.panel(create_doughnut_chart))),
    ('Bar Graph', pn.Column(dropdown, pn.panel(create_bar_graph))),
    ('Correlation Matrix', pn.Column(multi_select, show_correlations))
)

# Show dashboard layout (use dashboard.show() for deployment)
dashboard.servable()

# Test functions from 'test_dashboard_projects.py'
import unittest

class TestDashboardProjects(unittest.TestCase):

    def test_data_loading(self):
        # Test if dataset has been loaded successfully
        self.assertFalse(df.empty, "The dataframe should not be empty")
        self.assertIn('survived', df.columns, "The dataframe should contain a 'survived' column")

    def test_widget_defaults(self):
        # Test if widgets have expected default values
        self.assertEqual(dropdown.value, 'survived', "The default value of the dropdown should be 'survived'")
        self.assertEqual(slider.value, 10, "The default value of the slider should be 10")
        self.assertTrue(checkbox_grid.value, "The checkbox for gridlines should be checked by default")

    def test_create_histogram(self):
        # Test if create_histogram function runs without errors
        fig = create_histogram('age', 10, True)
        self.assertIsNotNone(fig, "The figure returned by create_histogram should not be None")
        self.assertEqual(fig.get_axes()[0].get_xlabel(), 'age', "The x-axis label should be 'age'")

if __name__ == '__main__':
    import sys
    if 'test' in sys.argv:
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
    else:
        # Launch dashboard
        dashboard.show()
