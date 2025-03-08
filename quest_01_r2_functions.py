import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

# Read the Excel file, skipping the first 8 rows
df = pd.read_excel('page_spreadsheet.xlsx', sheet_name='Sheet 1', skiprows=8)

# Clean the DataFrame
df_cleaned = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df_cleaned.drop(index=[0, 1, 10] + list(range(32, 39)), inplace=True)
df_cleaned.rename(columns={'TIME': 'Country'}, inplace=True)
df_cleaned.reset_index(drop=True, inplace=True)

# Convert columns to numeric
columns_to_convert = [str(year) for year in range(2010, 2024)]
df_cleaned[columns_to_convert] = df_cleaned[columns_to_convert].apply(pd.to_numeric, errors='coerce')

# Calculate year-on-year percentage change
profitability = df_cleaned.set_index('Country').pct_change(axis=1) * 100
pre_pandemic = profitability.iloc[:, :10]
post_pandemic = profitability.iloc[:, 10:]

# Compute average profitability
comparison = pd.concat([pre_pandemic.mean(axis=1).rename("Avg Pre-Pandemic (%)"),
                        post_pandemic.mean(axis=1).rename("Avg Post-Pandemic (%)")], axis=1)
comparison['Difference'] = comparison['Avg Post-Pandemic (%)'] - comparison['Avg Pre-Pandemic (%)']

# Plotting top 10 countries with highest increase in profitability
top_10_countries = comparison[comparison['Difference'] > 0].nlargest(10, 'Difference').reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(data=top_10_countries, x='Country', y='Difference', palette='viridis')
plt.title('Top 10 Countries with Highest Increase in % After COVID-19')
plt.xlabel('Country')
plt.ylabel('Increase in Average %')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot profitability in 2020
df_cleaned['2020'] = pd.to_numeric(df_cleaned['2020'], errors='coerce')
df_cleaned.dropna(subset=['2020'], inplace=True)
plt.figure(figsize=(12, 6))
sns.barplot(x='Country', y='2020', data=df_cleaned, palette='Greens')
plt.title('Profitability in 2020 by Country')
plt.xlabel('Country')
plt.ylabel('Profitability (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Melt DataFrame for profitability comparison between 2019 and 2022
df_melted = df_cleaned.melt(id_vars=['Country'], value_vars=['2019', '2022'], var_name='Year', value_name='Profitability')
plt.figure(figsize=(12, 6))
sns.barplot(x='Country', y='Profitability', hue='Year', data=df_melted, palette='viridis')
plt.title('Profitability in 2019 vs. 2022 by Country')
plt.xlabel('Country')
plt.ylabel('Profitability (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Line plot for House Price Index (HPI)
df_long = df_cleaned.melt(id_vars=['Country'], var_name='Year', value_name='HPI')
df_long['Year'] = df_long['Year'].astype(int)
plt.figure(figsize=(14, 8))
sns.lineplot(data=df_long, x='Year', y='HPI', hue='Country', marker='o')
plt.title('House Price Index (HPI) from 2010 to 2023 for Various Countries')
plt.xlabel('Year')
plt.ylabel('House Price Index (HPI)')
plt.axhline(100, color='grey', linewidth=0.8, linestyle='--')
plt.xticks(rotation=45)
plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Calculate and plot maximum increases in HPI
hpi_changes = df_cleaned.set_index('Country').pct_change(axis=1) * 100
top_countries = hpi_changes.max(axis=1).nlargest(10).reset_index()
plt.figure(figsize=(12, 6))
sns.barplot(data=top_countries, x='Country', y=0, palette='viridis')
plt.title('Top 10 Countries with the Highest Increase in House Price Index')
plt.xlabel('Country')
plt.ylabel('Max Increase (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Web Scraping Operation
# Install necessary libraries
!pip install requests beautifulsoup4

# Import libraries
import requests
from bs4 import BeautifulSoup
from IPython.display import Image, display

# Define the URL to scrape
url = "https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20241003-2"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Print the prettified HTML (optional)
    print(soup.prettify())
    
    # Extract all paragraph tags
    paragraphs = soup.find_all("p")
    for p in paragraphs:
        print(p.get_text())  # Print the text of each paragraph

    # Extract all image tags
    images = soup.find_all("img")
    for img in images:
        print(img['src'])  # Print the source URL of each image

    # Define the URL of the specific image to download
    image_url = "https://ec.europa.eu/eurostat/documents/4187653/18051237/house-prices-rents-change-between-2010-q2-2024jpg.jpg/14395314-47a4-721e-37ef-ea84c8a10a28?t=1727940974598"

    # Download the image
    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        with open("house_prices_rents_change.jpg", "wb") as file:
            file.write(image_response.content)
        print("Image downloaded successfully.")
    else:
        print(f"Failed to download image. Status code: {image_response.status_code}")

    # Display the downloaded image
    display(Image(filename="house_prices_rents_change.jpg"))

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
