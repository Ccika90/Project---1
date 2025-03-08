# Project---1
First Project of Data Analysis Boot Camp
House Price Index (HPI) Analysis
This project focuses on analyzing the House Price Index (HPI) data for various countries from 2010 to 2023. The analysis includes data cleaning, exploratory data analysis (EDA), visualization, and insights into trends and changes in house prices over time, particularly before and after the COVID-19 pandemic.

==============================================================================================================================================================
Table of Contents
Part 1. Analysis
1. Project Overview
2. Data Source
3. Data Cleaning and Preparation
4. Exploratory Data Analysis (EDA)
5. Key Insights
6. Visualizations
7. Features
8. How to Use This Code
9. Dependencies
10. License

Part 2. Web Scraping 

12. Overview
13. Features
   1. Image Downloading
   2. Image Display
13. Requirements
14. Code Explanation
    1. Downloading the image
    2. Displaying the image
15. How to use
    1. Run the script
    2. Output
16. Potential Use Cases
17. Error Handling
18. Notes

--------------------------------------------------------------------------------------------------------------------------------------------------------------
PART ONE (1)
1. Project Overview
   The goal of this project is to analyze the House Price Index (HPI) data for multiple countries over the years 2010 to 2023. The analysis includes:
   Cleaning and preparing the dataset.
   Calculating year-on-year percentage changes in HPI.
   Comparing pre-pandemic (2010-2019) and post-pandemic (2020-2023) trends.
   Visualizing the data to identify key trends and insights.

--------------------------------------------------------------------------------------------------------------------------------------------------------------
2. Data Source
   The dataset is sourced from an Excel file (page_spreadsheet.xlsx), which contains HPI data for various countries from 2010 to 2023. The data is organized       with countries as rows and years as columns.

--------------------------------------------------------------------------------------------------------------------------------------------------------------
3. Data Cleaning and Preparation
   The following steps were taken to clean and prepare the data:
   Reading the Data: The Excel file was read, skipping unnecessary rows.
   Dropping Unnamed Columns: Columns with "Unnamed" patterns were removed.
   Dropping Rows: Specific rows and a range of rows were dropped to clean the dataset.
   Resetting the Index: The index was reset for better data handling.
   Renaming Columns: The TIME column was renamed to Country.
   Converting Data Types: Columns for each year were converted to numeric values.
   Handling Missing Values: Rows with missing values in key columns were dropped.

--------------------------------------------------------------------------------------------------------------------------------------------------------------
4. Exploratory Data Analysis (EDA)
   The EDA process included:
   Shape of the Dataset: Checking the number of rows and columns.
   Column Names: Listing all columns in the dataset.
   Duplicates: Identifying and removing duplicate rows.
   Missing Values: Checking for NaN values in each column.
   Data Types: Ensuring the data types of columns are appropriate.
   Year-on-Year Percentage Change: Calculating percentage changes in HPI for each year.
   Pre- and Post-Pandemic Analysis: Separating data into pre-pandemic (2019) and post-pandemic (2022) periods and calculating average profitability.

--------------------------------------------------------------------------------------------------------------------------------------------------------------
5. Key Insights
   Top 10 Countries with Highest Increase in Profitability After COVID-19:
   Identified countries with the highest increase in average profitability post-pandemic.
   Visualized the results using a bar chart.
   Profitability Trends by Country:
   Analyzed profitability trends for specific years (e.g., 2019, 2022).
   Created bar charts to compare profitability across countries.
   House Price Index (HPI) Trends:
   Plotted HPI trends for specific countries over the years.
   Visualized HPI trends for multiple countries in a single line plot.
   Year-on-Year Percentage Change:
   Calculated the maximum increase in HPI for each country.
   Identified the top 10 countries with the highest increase in HPI.

--------------------------------------------------------------------------------------------------------------------------------------------------------------
6. Visualizations
   The following visualizations were created:
   Pie Chart: Top 10 countries with the highest increase in profitability after COVID-19.
   Bar Chart: Profitability comparison between 2019 and 2022.
   Line Plot: House Price Index (HPI) trends for specific countries.
   Line Plot: HPI trends for multiple countries from 2010 to 2023.
   Bar Chart: Top 10 countries with the highest increase in HPI.

--------------------------------------------------------------------------------------------------------------------------------------------------------------
7. How to Use This Code
   Install Dependencies: Ensure you have the required libraries installed (see Dependencies).
   Download the Dataset: Place the Excel file (page_spreadsheet.xlsx) in the working directory.
   Run the Code: Execute the provided Python script to perform the analysis and generate visualizations.
   Customize: Modify the code to analyze specific countries or time periods.

--------------------------------------------------------------------------------------------------------------------------------------------------------------
8. Dependencies
   The following Python libraries are required to run the code:
   pandas
   numpy
   matplotlib
   seaborn
   openpyxl (for reading Excel files)

   You can install the dependencies using the following command:
   pip install pandas numpy matplotlib seaborn openpyxl

---------------------------------------------------------------------------------------------------------------------------------------------------------------
9. License
   This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as needed.

---------------------------------------------------------------------------------------------------------------------------------------------------------------
Contact
    For questions or feedback, please contact [Claudio Do Prado] at [claudiodoprado@hotmail.com].
                                              [Zenari Sint Jago] at [data.zenalyst@gmail.com]
                                              [Chika Ikenna Umeh] at [umehchikaikenna@gmail.com]

===============================================================================================================================================================
PART TWO (2)

12. Overview
    This Python script demonstrates how to download an image from a given URL and save it locally, as well as how to display the image directly from the URL        using the IPython.display module. The script is particularly useful for tasks involving image retrieval and visualization in Python.
--------------------------------------------------------------------------------------------------------------------------------------------------------------
14. Features
   1. Image Downloading
      The script uses the requests library to send an HTTP GET request to the specified image URL.
      If the request is successful (status code 200), the image is saved locally in binary format with the filename house_prices_rents_change.jpg.

   3. Image Display
      The script uses the IPython.display.Image and display functions to render the image directly from the URL in a Jupyter Notebook or similar environment.
--------------------------------------------------------------------------------------------------------------------------------------------------------------
13. Requirements
To run this script, ensure the following Python libraries are installed:
    requests: For sending HTTP requests to fetch the image.
    IPython: For displaying the image directly in a notebook environment.
You can install these libraries using pip:
    pip install requests
    pip install ipython
--------------------------------------------------------------------------------------------------------------------------------------------------------------
15. Code Explanation
    1. Downloading the image
       The script defines the URL of the image (image_url) and sends a GET request using requests.get().
       If the response status code is 200 (indicating success), the image data is written to a local file named house_prices_rents_change.jpg in binary mode           (wb).
Example:
    response = requests.get(image_url)
if response.status_code == 200:
    with open("house_prices_rents_change.jpg", "wb") as file:
        file.write(response.content)
    print("Image downloaded successfully.")
else:
    print(f"Failed to download image. Status code: {response.status_code}")
    3. Displaying the image
       The script uses the IPython.display.Image function to load the image directly from the URL and the display() function to render it in the output cell of        a Jupyter Notebook.
Example:
    from IPython.display import Image, display
    display(Image(url=image_url))

--------------------------------------------------------------------------------------------------------------------------------------------------------------
16. How to use
    1. Run the script
       Copy the script into a Python file or Jupyter Notebook and execute it.
       Ensure you have an active internet connection to fetch the image from the URL.

    3. Output
       The image will be saved locally as house_prices_rents_change.jpg in the same directory as the script.
       If running in a Jupyter Notebook, the image will also be displayed directly in the notebook.

--------------------------------------------------------------------------------------------------------------------------------------------------------------
17. Potential Use Cases
    a. Automating the retrieval and storage of images from the web.
    b. Visualizing images directly in a Jupyter Notebook for data analysis or presentations.
    c. Integrating image downloading and display functionality into larger Python projects.

--------------------------------------------------------------------------------------------------------------------------------------------------------------
19. Error Handling
    The script checks the HTTP response status code to ensure the image is successfully retrieved. If the status code is not 200, an error message is printed:
        print(f"Failed to download image. Status code: {response.status_code}")
    Ensure the URL provided is valid and accessible. If the URL is incorrect or the server is down, the script will fail to download the image.

--------------------------------------------------------------------------------------------------------------------------------------------------------------
20. Notes
    The script is designed for educational and demonstration purposes. For production use, consider adding more robust error handling and logging.
    The image URL used in this script points to a Eurostat resource. Ensure compliance with any applicable terms of use or copyright restrictions when             downloading and using images from external sources.

Presentation:
https://prezi.com/view/XJu6BhVgT8qdSYxYea4f/