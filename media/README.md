# Media Dataset Analysis

## Overview
The Media dataset contains information about various media properties like views, ratings, and genres. The analysis covers the dataset's summary statistics, missing values, and provides visualizations to understand the distribution of views and ratings.

## Dataset Summary

| **Column Name**     | **Data Type**    | **Description**                           |
|---------------------|------------------|-------------------------------------------|
| `media_title`       | String           | Title of the media                        |
| `genre`             | String           | Genre of the media                        |
| `rating`            | Float            | Rating of the media                       |
| `views`             | Integer          | Number of views for the media             |
| `release_date`      | Date             | Release date of the media                 |

### Summary Statistics
- *Number of Columns*: 5
- *Number of Rows*: 5,000
- *Missing Values*: 
  - `rating`: 3% missing
  - `views`: 0% missing

### Visualizations

#### Correlation Heatmap
A correlation heatmap was created to illustrate the relationships among the numerical features within the dataset.

[![Correlation Heatmap](media/correlation_heatmap.png)](https://github.com/madhavanrmiitm/tds-project2/blob/main/media/correlation_heatmap.png)

#### Overall Distribution
A distribution plot of overall ratings displays the frequency and distribution of ratings across the dataset, with a noticeable concentration around certain rating values.

![Overall Distribution(media/overall_distribution.png)](https://github.com/madhavanrmiitm/tds-project2/blob/main/media/overall_distribution.png)

### Dataset Narrative
The analysis of the Media dataset indicates that there is a high variance in views, with a few media items getting extremely high views. The rating distribution shows a relatively even spread across the ratings, with a slight bias toward higher ratings.

The views and ratings of the media are not strongly correlated, which suggests that high views do not necessarily mean high ratings.
