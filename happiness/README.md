# Happiness Dataset Analysis

## Overview
The Happiness dataset contains data on various factors influencing happiness, including income, education, and social support. This analysis examines summary statistics, identifies missing values, and provides visualizations to explore the distribution of happiness scores.

## Dataset Summary

| **Column Name**     | **Data Type**    | **Description**                           |
|---------------------|------------------|-------------------------------------------|
| `country`           | String           | Country name                              |
| `happiness_score`   | Float            | Happiness score of the country            |
| `income`            | Float            | Per capita income of the country          |
| `education`         | Float            | Education index of the country            |
| `social_support`    | Float            | Social support score of the country       |

### Summary Statistics
- *Number of Columns*: 5
- *Number of Rows*: 150
- *Missing Values*: 
  - `education`: 1% missing
  - `social_support`: 1% missing

### Visualizations

#### Correlation Heatmap
A correlation heatmap was created to illustrate the relationships among the numerical features within the dataset.

[Correlation Heatmap(happiness/correlation_heatmap.png)](https://github.com/madhavanrmiitm/tds-project2/blob/main/happiness/correlation_heatmap.png)

#### Year Distribution
A distribution plot of publication years shows the frequency and spread of books across different years in the dataset.

![Year Distribution(happiness/year_distribution.png)](https://github.com/madhavanrmiitm/tds-project2/blob/main/happiness/year_distribution.png)

### Dataset Narrative
The analysis of the Happiness dataset reveals that countries with higher income levels tend to have higher happiness scores, though some exceptions exist. Social support and education scores are also positively correlated with happiness, suggesting that these factors play a significant role in a country's overall happiness.

The distribution of happiness scores indicates that most countries fall within the 5.0 to 7.5 range, with only a few countries surpassing this range.
