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

By analyzing this graph, you can see there is a general increasing trend over the years. From 2014 to 2024, there is an upward trajectory indicating a positive growth in the average wages for workers in Lubbock. While there are fluctuations, the overall trend is upward. Noticing starting in 2020 to 2022, you can see peaks in the graph. Due to the pandemic that took place during these years, it caused the average wage to spike. Following that peak in 2022, there is a slight decline. This decline can be attributed to the workforce going back down to a normal state following the pandemic. With averages dropping from $21.44 to $21.16 in 2024, shows a new decline and is setting up the year to be decreased. In summary, the graph shows an overall positive trend over the years, with fluctuations and spikes due to outside factors and market conditions.

![AVGMNTHLYICM](https://github.com/user-attachments/assets/a293299f-54b3-4ee0-8c34-461533587810)

Looking at this graph,  you can notice many more fluctuations in comparison to the average wage graph. There are more downward trends. From 2014 to 2017, there is a constant decline. In 2018, you can see the first increase in the graph. If you look back at the average wage graph,  you can notice that in 2018 the average wage increased almost $1, so this can show why the increase happens and remains steady through 2019. Looking at the years affected by the pandemic, you can see once again how those numbers are inflated. Following those years and a return to normalcy, the declining trend is present once again. After analyzing the graph, we attributed these declines and fluctuations to the relationship between average hours worked and average wage.

![WGHRSWRKD](https://github.com/user-attachments/assets/20ffeca2-fc43-481e-9639-94f460add68b)

So, following my analysis of the previous graph, I can understand how the relationship between hours worked and average wage directly affects the average monthly income. There is an inverse relationship between the data. In years where the average wage per hour is higher, the average hours worked per month tend to be lower, and vice versa. Outside of the pandemic years where both wage and hours worked were at a high due to demand, you can see as the wage increased the hours worked dropped. For instance, the years 2023 and 2024 are the highest average wage years (disregarding the pandemic years) the average hours worked are at an all-time low. The relationship between average hours worked per month and average wage per hour has implications for overall income. Higher hourly wages can compensate for fewer hours worked, resulting in similar monthly incomes.

![CORRELATION](https://github.com/user-attachments/assets/2d711879-07bb-4bff-adb5-a844d3342064)

Another analysis I made is how the unemployment rate correlates with the average wage. Overall, there is a correlation that when wage goes up the unemployment rate drops. From 2014 to 2019 you can see as the wage increases, the unemployment rate drops. The years 2020 through 2022 once again show a large fluctuation due to the pandemic. You can see how in 2020 while the wage is at its highest yet, the unemployment rate is at its highest. Again, this is simply just due to how the pandemic affected the workforce. Besides, that looking at 2023 to 2024, you can see as the wages decrease the unemployment rate rises. This solidifies our idea that as wage increases/decreases the unemployment rate follows in the opposite direction





