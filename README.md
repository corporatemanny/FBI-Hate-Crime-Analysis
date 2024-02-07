# Hate Crime Analysis README

## Team Members: 
Rossie Jimenez, Emanuel Diaz-Berrios and Steven Carrasquillo-Merly
 
## Scope of Research:
The scope of research involves a comprehensive analysis of hate crime data, with a specific focus on changes in hate crime categories before and after 9/11, using statistical methods to discern meaningful patterns and trends.

## Dependencies
1. Pandas
2. Pathlib
3. Numpy
4. Matplotlib
5. Scipy

## Code Stucture

1. Data Loading and Initial Exploration: Reads the hate crime dataset using Pandas. Selects relevant columns for analysis.

2. Data Preprocessing: Splits entries in the 'bias_desc' column into individual categories.
Categorizes hate crime descriptions into broader categories.

3. Visualization - Scatter Line Plot:Creates a scatter line plot representing the count and years of each hate crime category.

4. Visualization - Bar Plot (Before and After 9/11):Generates a bar plot showing the percentage of each category before and after September 11, 2001.

5. Visualization - Filled Bar Plot (Over Time): Produces a filled bar plot illustrating the percentage of each category over the years.

6. Chi-Square Test: Conducts a Chi-Square test to assess the significance of hate crime percentage changes before and after 9/11 for each category.

7. Results Summary: Prints Chi-Square values and p-values for each hate crime category.

## Figures
The script generates visualizations in the 'Analysis' folder:

'Hate Crime Categories Over 31 Years (1991-2022).png'
'Bar Plot- Hate Crime Categories Over Time.png'
'Filled Bar Plot- Hate Crime Categories Over Time in Years.png'
The processed data is saved as 'output_file.csv'.

### Datasets used for our topic: 
FBI Hate Crime dataset(CSV).

Hypothesis: Hate crimes that happened 10 years before 9/11 targeted different population than hate crimes 10 years after 9/11.

Null-Hypothesis: There is no difference in targeted population.

