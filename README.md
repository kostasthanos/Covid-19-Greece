# Covid-19-Greece
Data and Plots about the pandemic progression in Greece. 

| Last Update | Total Cases | Days |
|     ---     |     ---     |  --- |
|  21-10-20   |    27334    |  239 |

<p align="center">
  <img width="300" height="200" src="imgs/flag.png">
</p>

## Main Idea
This project focuses on the virus Covid-19 in Greece by using the necessary data and the corresponding plots for better understanding of the progression of the pandemic in the country.

The main file of the project is : *[Covid-19_Data_Greece.ipynb](https://github.com/kostasthanos/Covid-19-Greece/blob/master/Covid-19_Data_Greece.ipynb)*.  

## A closer look on the file

Use of three (3) basic datasets.

1. All the previous Covid-19 data from the beginning of the pandemic in the country.
2. New data from the official daily report by the Hellenic National Organization of Public Health (EODY).
3. Weather data about the max temperature from Acharnes Weather Station (**removed**).

After the manipulation of the above data a dataframe is being created, containing the following columns :

1. Dates
2. Total Cases
3. Daily Cases
4. Total Recovered
5. Active Cases

For example the tail (last 5 rows) of the dataframe for the date **21/10/20** were:  
|       |     Dates   |	Total Cases |	Daily Cases | Total Recovered | Active Cases | 
|  ---  |      ---    |     ---     |     ---    |       ---        |      ---     |
|  235  |    17/10    |   22652     |    482     |      16437       |      7995    |
|  236  |    18/10    |   23060     |    438     |      16437       |      8424    |
|  237  |    19/10    |   23495     |    438     |      16347       |      8845    |
|  238  |    20/10    |   23947     |    667     |      16437       |      9504    |
|  239  |    21/10    |   27334     |    865     |      19749       |      7051    |

and the plots until the same date (**21/10/20**) using the above dataframe were :

## Total Cases per day
<p align="center">
  <img width="750" height="370" src="Plots_per_Date/Plots_for_21-10-2020/TotalCases_21-10-2020.png">
</p>

## Daily Cases
<p align="center">
  <img width="750" height="370" src="Plots_per_Date/Plots_for_21-10-2020/DailyCasesBars_21-10-2020.png">
</p>

## Total Cases & Total Recovered
<p align="center">
  <img width="750" height="370" src="Plots_per_Date/Plots_for_21-10-2020/TotalCases_Recovered_21-10-2020.png">
</p>

## Total & Active Number of Cases
<p align="center">
  <img width="750" height="370" src="Plots_per_Date/Plots_for_21-10-2020/Total_ActiveCases_21-10-2020.png">
</p>

## Total & Daily Number of Cases
<p align="center">
  <img width="750" height="370" src="Plots_per_Date/Plots_for_21-10-2020/TotalDaily_21-10-2020.png">
</p>

**Note:** To see the plots of an exact date, choose the corresponding folder from *[Plots_per_Date](https://github.com/kostasthanos/Covid-19-Greece/tree/master/Plots_per_Date)*.
You can also see the above plots created with (plotly) in [Latest Plots of covid-19 in Greece](https://kostasthanos.github.io/svg_map_cases/Data_Plots/Categories/greek_plots.html).

## Check the jupyter notebook file
For a deeper understanding on how the data are being collected and used see the file *Covid-19_Data_Greece.ipynb* which contains all the necessary python comments describing each step of the project. 

Information about data extraction from the daily report are in the file [data_extraction.md](https://github.com/kostasthanos/Covid-19-Greece/blob/master/data_extraction.md).

The sources been used to extract the data are :  
**Covid19.gov.gr** : https://eody.gov.gr/category/covid-19/

**Note:** Max Temperature data has been deleted from the csv file.

## Check also 
For a more visual understanding of covid-19 cases in Greece per region the following page :  
[Covid-19 cases per region Greece](https://kostasthanos.github.io/svg_map_cases/regions_index.html)

## Author
* **Konstantinos Thanos**
