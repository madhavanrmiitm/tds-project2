# tds-project2

## Automated Data Analysis Tool  

### **Overview**  
*Automated Analysis* is an advanced data analysis tool designed to automatically process datasets, generate insights, and visualize results with minimal user input. This tool handles diverse datasets and produces comprehensive reports that include statistical summaries, correlation analysis, and visualizations. It leverages Python and integrates OpenAI's models to create narrative insights based on the analysis outcomes.

### **Datasets Analyzed**  
The tool has been applied to the following datasets:  

- *Goodreads Dataset:* Analysis of books, ratings, authors, and genres.  

- *Media Dataset:* Examination of media views, ratings, and genres.  

- *Happiness Dataset:* Evaluation of happiness scores, income, education, and social support by country.

### **Key Features**  
- *Automated Data Loading:* Upload a dataset, and the system automatically loads and analyzes it.  

- *Summary Statistics:* Provides detailed statistical summaries for both numerical and categorical data.  

- *Data Visualizations:* Generates insightful visualizations such as correlation heatmaps and distribution plots, which are saved as PNG files.  

- *Narrative Generation:* Uses OpenAI’s API to produce detailed, human-readable narratives based on the analysis results.

### **Repository Structure**  
The repository is organized into the following structure:  

```
/tds-project2
├── goodreads/
│   ├── README.md
│   ├── book_id_distribution.png
│   ├── correlation_heatmap.png
│   └── ratings_distribution.png
├── happiness/
│   ├── README.md
│   ├── correlation_heatmap.png
│   └── year_distribution.png
├── media/
│   ├── README.md
│   ├── correlation_heatmap.png
│   └── overall_distribution.png
├── LICENSE
├── README.md
├── autolysis.py
└── overall_distribution.png
```

### **How to Use**  
1. Run the analysis script using:  
   ```bash
   python autolysis.py <dataset1.csv> <dataset2.csv> ...
   ```  
2. View the generated reports and visualizations in the respective folders for each dataset.

### **Conclusion**  
*Automated Analysis* streamlines data analysis by combining automation with narrative generation, providing users with actionable insights and high-quality visualizations in an easy-to-access format.
