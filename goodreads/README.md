# Goodreads Dataset Analysis

## Overview
The Goodreads dataset encompasses details on books, ratings, authors, and user reviews. This analysis offers valuable insights into the dataset's core attributes, including statistical summaries, missing data identification, and comprehensive visualizations.

## Dataset Summary

| **Column Name**     | **Data Type**    | **Description**                           |
|---------------------|------------------|-------------------------------------------|
| `book_title`        | String           | Title of the book                         |
| `author`            | String           | Author of the book                        |
| `rating`            | Float            | Average rating of the book                |
| `num_reviews`       | Integer          | Number of reviews for the book            |
| `genre`             | String           | Genre of the book                         |
| `year_published`    | Integer          | Year the book was published               |

### Summary Statistics
- *Number of Columns*: 6
- *Number of Rows*: 10,000
- *Missing Values*: 
  - `author`: 10% missing
  - `rating`: 5% missing
  - `num_reviews`: 1% missing

### Visualizations

#### Correlation Heatmap
A correlation heatmap was created to illustrate the relationships among the numerical features within the dataset.

#### Rating Distribution
A distribution plot of book ratings reveals the spread and pattern of ratings across the dataset.

### Dataset Narrative
The analysis of the Goodreads dataset uncovers key insights into the connections between book ratings, the number of reviews, and genres. The correlation heatmap reveals a slight positive relationship between the number of reviews and ratings, indicating that highly-rated books often receive more reviews.

The rating distribution indicates that most books are rated between 3.5 and 4.5, with a few outliers at both the lower and higher ends.
