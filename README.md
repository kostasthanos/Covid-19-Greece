# Covid-19-Greece
Data and Plots about the pandemic progression in Greece. 

| Last Update | Total Cases | Days |
|     ---     |     ---     |  --- |
|  27-07-20   |     4227    |  153 |

<p align="center">
  <img width="300" height="200" src="imgs/flag.png">
</p>

## Main Idea
This project focuses on the virus Covid-19 in Greece by using the necessary data and the corresponding plots for better understanding of the progression of the pandemic in the country.

The main file of the project is : *Covid-19_Data_Greece.ipynb*.  

## A closer look on the file

We are focusing on three (3) basic datasets.

1. All the previous Covid-19 data from the beginning of the pandemic in the country.
2. New data from the official daily report by the Hellenic National Organization of Public Health (EODY).
3. Weather data about the max temperature from Acharnes Weather Station.

After the manipulation of the above data we create a dataframe containing the following columns :

1. Dates
2. Total Cases
3. Daily Cases
4. Total Recovered
5. Active Cases

For example the tail (last 5 rows) of the dataframe for the date **25/07/20** were:  
|       |     Dates   |	Total Cases |	Daily Cases | Total Recovered | Active Cases | 
|  ---  |      ---    |     ---     |     ---    |       ---        |      ---     |
|  146  |    21/07    |    4048     |     36     |       1374       |      2477    |
|  147  |    22/07    |    4077     |     32     |       1374       |      2503    |
|  148  |    23/07    |    4110     |     33     |       1374       |      2535    |
|  149  |    24/07    |    4135     |     26     |       1374       |      2560    |
|  151  |    25/07    |    4166     |     31     |       1374       |      2591    |


and some of the plots until the same date (**25/07/20**) using the above dataframe were :

## Total Cases per day
<p align="center">
  <img width="750" height="370" src="Plots_per_Date/Plots_for_25-07-2020/TotalCases_25-07-2020.png">
</p>

## Daily Cases
<p align="center">
  <img width="750" height="370" src="Plots_per_Date/Plots_for_25-07-2020/DailyCasesBars_25-07-2020.png">
</p>

## Total Cases & Total Recovered
<p align="center">
  <img width="750" height="370" src="Plots_per_Date/Plots_for_25-07-2020/TotalCases_Recovered_25-07-2020.png">
</p>

## Total & Active number of Cases
<p align="center">
  <img width="750" height="370" src="Plots_per_Date/Plots_for_25-07-2020/Total_ActiveCases_25-07-2020.png">
</p>

## Total & Daily Number of Cases
<p align="center">
  <img width="750" height="370" src="Plots_per_Date/Plots_for_25-07-2020/TotalDaily_25-07-2020.png">
</p>

**Note:** To see the plots of an exact date, choose the corresponding folder from *Plots_per_Date*.

## Check the jupyter notebook file
For a deeper understanding on how the data are being collected and used see the file *Covid-19_Data_Greece.ipynb* which contains all the necessary python comments describing each step of the project. 

Information about data extraction from the daily report are in the file [data_extraction.md](https://github.com/kostasthanos/Covid-19-Greece/blob/master/data_extraction.md)

The sources been used to extract the data are : 

**Covid19.gov.gr** : https://eody.gov.gr/category/covid-19/

**Note:** Max Temperature data has been deleted from the csv file.

## Check also 
For a more visual display of covid-19 cases in Greece per region the following page : 
[Covid-19 cases per region Greece](https://kostasthanos.github.io/svg_map_cases/regions_index.html)

## Author
* **Konstantinos Thanos**
