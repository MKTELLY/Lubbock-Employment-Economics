### Project Overview

For this project, I analyzed the economic landscape of **Lubbock, Texas**, focusing on workforce dynamics, recognizing it as a driving force of economic prosperity. I selected datasets on **average hourly wage, hours worked, and employment statistics** to offer a comprehensive view across all employment sectors in Lubbock.

My goal was to combine these datasets to identify correlations and extract actionable insights. This empowers **residents, policymakers, and business owners** with data to support informed decisions, drive growth, and navigate the job market.



### Data Domains

I used three datasets: **average hours worked**, **average wages**, and **employment stats**. While they covered all industries without specific detail, they provided a broad picture of the workforce. Despite limited granularity, they helped monitor workforce trends over time.



### Data Analysis

I focused on the following key variables:
- **Average Wage Per Hour**
- **Average Hours Worked Monthly**
- **Labor Force**
- **Employment**
- **Unemployment Rate**

I sourced the data from the **U.S. Bureau of Labor Statistics**. While survey-based and somewhat variable, it provided a solid foundation for analysis.

The three most valuable variables were **average wage**, **hours worked**, and **unemployment rate**, each offering insights into wage trends, labor productivity, and market health.



### Data Cleaning

The datasets were mostly complete, except for **2024**, which I trimmed to data available through **February**. Instead of using code to clean, I manually edited the CSVs—removing extra headers, links, and metadata for simplicity.



### Data Merging & Feature Engineering

I merged all datasets using the common key **‘DATE’**, which aligned mostly on a monthly basis. I:
- Calculated **monthly hours** from weekly values.
- Created a new feature: **Average Monthly Income** = average wage × monthly hours.
- Aggregated data yearly for a more digestible view of trends.

The merged dataset gave me a clearer view of workforce patterns and supported more informed analysis.



### Visualizations & Insights

I used **line graphs, bar charts, and scatter plots** to show:
- A **steady wage increase** from 2014–2024, with pandemic-related spikes.
- **Hours worked** showed more fluctuation—typically declining when wages rose.
- An **inverse relationship** between wage and hours worked.
- A **negative correlation** between wage and unemployment—except during the pandemic, higher wages often correlated with lower unemployment.

- 
![WAGEPERHR](https://github.com/user-attachments/assets/4291989b-ab3d-4546-a60e-433807b59365)
![AVGMNTHLYICM](https://github.com/user-attachments/assets/a293299f-54b3-4ee0-8c34-461533587810)
![WGHRSWRKD](https://github.com/user-attachments/assets/20ffeca2-fc43-481e-9639-94f460add68b)
![CORRELATION](https://github.com/user-attachments/assets/2d711879-07bb-4bff-adb5-a844d3342064)




### How to Run the Code

1. **Download all `.csv` files** in the repo.
2. Update the **`data_dir`** in the script to match your local file path.
3. Run lines **1–12** to load dependencies and set paths.
4. Run **15–32** to merge datasets and create both monthly and yearly DataFrames.
5. Use the **Variable Explorer** to verify creation.
6. Run **36–41** to export the final DataFrames to `.csv`.
