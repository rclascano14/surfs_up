# surfs_up
Module 9: Using SQLite, SQLAlchemy, and Flask to build on my knowledge of SQL database structures and querying methods.

## Resources
- Python
- Jupyter Notebook
- Visual Studio Code
- SQLite
- SQLAlchemy
- Flask
- Data: hawaii.sqlite

## Overview of Project

In this module, I have used SQLite to create databases, used SQLAlchemy to query requests from my SQLite databases, and used Flask to create Python applications and show them through the use of a webpage. With my familiarity of these tools established, I am brought to the Module 9 Challenge. Throughout this module, I have been analyzing the island of Oahu in regards to its suitability as a location for a surf shop based upon factors such as temperature or precipitation. I would then filter the data on these factors based upon conditions such as only data in the past year. Now that we have explored the location of Oahu and established that it is a good location for a surf shop, I am being asked to test the dates of June and December for temperature data to see if the surf shop will be sustainable year round. 

## Results

This Weeks Module consists of the following three deliverables:

- Deliverable 1: Determine the Summary Statistics for June

<img width="1111" alt="June Summary Statistics" src="https://user-images.githubusercontent.com/95828604/154902497-4f74cb64-d3c6-4a05-9228-e1c6cfadc8a8.png">

- Deliverable 2: Determine the Summary Statistics for December

<img width="1129" alt="December Summary Statistics" src="https://user-images.githubusercontent.com/95828604/154902547-5701b6c1-8beb-4283-aad9-7fef3d2bbe8a.png">

- Deliverable 3: A written report for the statistical analysis (README.md) (As seen here)

There are three key differences between the summary statistics for June and December which are pertinent in understanding the sustainability of the Oahu Surf Shop.
- The mean temperature for June is ~75 whereas the mean temperature for December is ~71. This means there is a differential of 4 degrees between the two months.
- Grouped into 20 bins, the histograms for the June and December summary statistics show the clusters of temperatures for the two months. Decemeber shows a far more symmetrical distribution while June shows a slightly skewed distribution to the left. 

<img width="1112" alt="June Temperature Histogram" src="https://user-images.githubusercontent.com/95828604/154906074-47b480c3-f033-41c7-b2a5-4db364e38a2d.png">

<img width="1118" alt="December Temperature Histogram" src="https://user-images.githubusercontent.com/95828604/154906114-3a9d6565-a63c-4bce-8326-29083b492a8f.png">

- While December may have a more symmetrical distribution, there is far less variance in temperatures in December as opposed to June. December has a large outlier in its frequency at ~71 degrees and June has a high frequency distribution from ~71 degrees to ~78 degrees. June also possesses far more outliers as compared to the average distribution of December. 

## Summary

To further enhance the results of my queries on June and December Temperature Data, I have also conducted two additional queries to ascertain the Precipitation Data for June and December. 

<img width="1108" alt="June Additional Query" src="https://user-images.githubusercontent.com/95828604/154908329-75f50ec3-8c48-4070-bb68-89fc390c0c48.png">

<img width="1115" alt="December Additional Query" src="https://user-images.githubusercontent.com/95828604/154908367-6f4cd1ee-2479-4ecb-ba1a-4d3466282028.png">

Despite there being several key differences between the months, my summary is that there should not be any issues regarding year round sustainability for the Oahu Surf Shop. The differential in mean temperature between the two months is 4 degrees, and the differential between the mean precipitation for the two months is less than 0.1 inches. Consequently, Oahu is incredibly consistent in its temperature throughout the year and as such, it should receive business throughout all months of the year. 
