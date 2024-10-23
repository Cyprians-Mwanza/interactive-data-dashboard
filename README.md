<img width="959" alt="Linegrapgh" src="https://github.com/user-attachments/assets/62fb0bdd-32c0-4b7c-81a2-a5d93dfd7800">**Interactive Data Dashboard**
This project is an interactive data visualization dashboard built using Python's Panel library. It allows users to explore a dataset and generate various visualizations, such as histograms and line graphs, with interactive controls like dropdowns, sliders, and checkboxes.

**Features**
Dataset: Titanic dataset is used as an example, but the code can be adapted to other datasets.
**Interactive Widgets:**
![Overview](https://github.com/user-attachments/assets/4872426b-50ea-4bf6-8e7a-cb5df9f5445a)
**Dropdown to select a column for plotting.**
Slider to adjust the number of bins for histograms.
Checkbox to toggle gridlines in the plots.
Multi-select widget to choose multiple columns.
**Visualizations:**
**Histogram:** Displays the distribution of a selected column.
<img width="959" alt="Histogram" src="https://github.com/user-attachments/assets/82d171e6-caec-4cda-94d1-1253c3b47fbf">
**Line Graph:** Plots the values of a selected column over time or in sequence.
<img width="959" alt="Linegrapgh" src="https://github.com/user-attachments/assets/3badbe26-a6e9-40a5-87e2-00431dd058ca">
**PieChart**
<img width="959" alt="Piechart" src="https://github.com/user-attachments/assets/27f822c1-4f2d-4307-937f-76ddb2a11714">
**DoughNut Chart**
![DoughNut Chart](https://github.com/user-attachments/assets/2114917a-89c4-4f39-acda-a10e9816c23b)
**BarGraph**
<img width="959" alt="BarGraph" src="https://github.com/user-attachments/assets/ac6875eb-37cf-4bf5-a0c4-25ae2d0826f0">
**Correlation Matrix**
<img width="959" alt="Correlation Matrix" src="https://github.com/user-attachments/assets/ca25a7b4-7654-40f5-9629-943b47f2b9a7">




Requirements
The code requires the following Python libraries:

**pandas
panel
matplotlib
numpy**
You can install the required packages using:
pip install pandas panel matplotlib numpy
**Running the Dashboard**
Clone the repository and navigate to the project directory:

git clone https://github.com/your-username/interactive-data-dashboard.git
cd interactive-data-dashboard
Ensure you have the required packages installed (as listed in the requirements section).

**Run the dashboard using:**
python merged_dashboard_with_tests.py
Open your web browser and navigate to the local server address (usually http://localhost:5006).

Usage
Select Column: Choose the column of the dataset for plotting.
Bins Slider: Adjust the number of bins in the histogram.
Show Gridlines: Toggle gridlines on the plot.
Multi-Select: Choose multiple columns for custom visualization needs.
The code uses the Titanic dataset as an example, visualizing data like age, fare, and class distributions.
The histogram shows the distribution of a selected column, while the line graph visualizes changes over time.
Customization
To use a different dataset, replace the URL in the following section of the code:

python
Copy code
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
df = pd.read_csv(url)
Replace the URL with the path to your own dataset.

Testing
The script also includes basic testing functions to verify the functionality of the dashboard.
