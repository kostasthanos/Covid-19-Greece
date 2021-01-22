# Covid-19-Greece
Data and Plots about the pandemic progression in Greece. 

| Last Update |  Total Cases | Days |
|     ---     |      ---     |  --- |
|  22-01-21   |    151041    |  332 |

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
2. Total_Cases
3. Daily_Cases 
4. Total_Losses
5. Daily_Losses
6. Intubated
7. Total_Recovered
8. Active_Cases
9. Total_RTPCR_tests
10. Total_RAPID_AG_tests
11. Total_Tests
12. Daily_Tests 

For example the tail (last 5 rows) of the dataframe for the date **22/01/21** were:  
|     | Dates    |   Total_Cases |   Daily_Cases |   Total_Losses |   Daily_Losses |   Intubated |   Total_Recovered |   Active_Cases |   Total_RTPCR_tests |   Total_RAPID_AG_tests |   Total_Tests |   Daily_Tests |
|----:|:---------|--------------:|--------------:|---------------:|---------------:|------------:|------------------:|---------------:|--------------------:|-----------------------:|--------------:|--------------:|
| 327 | 18/01/21 |        148925 |           320 |           5488 |             19 |         322 |             98312 |          45125 |             2966664 |                 840047 |       3806711 |          8173 |
| 328 | 19/01/21 |        149462 |           566 |           5518 |             30 |         320 |             98312 |          45632 |             2977596 |                 860714 |       3838310 |         31599 |
| 329 | 20/01/21 |        149973 |           516 |           5545 |             27 |         300 |             98312 |          46116 |             2989339 |                 879400 |       3868739 |         30429 |
| 330 | 21/01/21 |        150479 |           509 |           5570 |             25 |         293 |             98312 |          46597 |             3000313 |                 897881 |       3898194 |         29455 |
| 331 | 22/01/21 |        151041 |           585 |           5598 |             28 |         288 |             98312 |          47131 |             3012892 |                 917739 |       3930631 |         32437 |

and the plots until the same date (**22/01/21**) using the above dataframe were :
## Total Cases per day
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_22-01-21/TotalCases_22-01-21.png">
</p>

## Daily Cases
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_22-01-21/DailyCasesBars_22-01-21.png">
</p>

## Total & Daily Number of Cases
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_22-01-21/TotalDaily_22-01-21.png">
</p>

## Total Losses per day
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_22-01-21/TotalLosses_22-01-21.png">
</p>

## Daily Losses
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_22-01-21/DailyLossesBars_22-01-21.png">
</p>

## Total & Daily Losses
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_22-01-21/TotalDailyL_22-01-21.png">
</p>

## Intubated
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_22-01-21/Intubated_22-01-21.png">
</p>

## Total & Active Number of Cases
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_22-01-21/Total_ActiveCases_22-01-21.png">
</p>


## Total Cases per Month
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_22-01-21/PerMonth_22-01-21.png">
</p>

## Daily number of Tests
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_22-01-21/DailyTests_22-01-21.png">
</p>

## Total number of Tests
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_22-01-21/TotalTests_22-01-21.png">
</p>

## Total number of Tests (RT-PCR and RAPID AG)
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_22-01-21/Total_Tests_both_22-01-21.png">
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
