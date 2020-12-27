# Covid-19-Greece
Data and Plots about the pandemic progression in Greece. 

| Last Update |  Total Cases | Days |
|     ---     |      ---     |  --- |
|  27-12-20   |    135456    |  307 |

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

For example the tail (last 5 rows) of the dataframe for the date **27/12/20** were:  
|       |     Dates   |	Total Cases |	Daily Cases | Total Recovered | Active Cases | 
|  ---  |      ---    |     ---     |     ---     |       ---       |      ---     |
|  302  |    23/12    |   133365    |     937     |      98312      |     30651    |
|  303  |    24/12    |   134235    |     873     |      98312      |     31466    |
|  304  |    25/12    |   134852    |     617     |      98312      |     32033    |
|  305  |    26/12    |   135114    |     262     |      98312      |     32249    |
|  306  |    27/12    |   135456    |     342     |      98312      |     32538    |

and the plots until the same date (**27/12/20**) using the above dataframe were :

## Total Cases per day
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_27-12-2020/TotalCases_27-12-2020.png">
</p>

## Daily Cases
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_27-12-2020/DailyCasesBars_27-12-2020.png">
</p>

## Total Cases & Total Recovered
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_27-12-2020/TotalCases_Recovered_27-12-2020.png">
</p>

## Total & Active Number of Cases
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_27-12-2020/Total_ActiveCases_27-12-2020.png">
</p>

## Total & Daily Number of Cases
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_27-12-2020/TotalDaily_27-12-2020.png">
</p>

## (NEW) Total Cases per Month
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_27-12-2020/PerMonth_27-12-2020.png">
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
