# Covid-19-Greece
Data and Plots about the pandemic progression in Greece. 

| Last Update |  Total Cases | Days |
|     ---     |      ---     |  --- |
|  19-02-21   |    177494    |  360 |

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

For example the tail (last 5 rows) of the dataframe for the date **19/02/21** were:  
|     | Dates    |   Total_Cases |   Daily_Cases |   Total_Losses |   Daily_Losses |   Intubated |   Total_Recovered |   Active_Cases |   Total_RTPCR_tests |   Total_RAPID_AG_tests |   Total_Tests |   Daily_Tests |
|----:|:---------|--------------:|--------------:|---------------:|---------------:|------------:|------------------:|---------------:|--------------------:|-----------------------:|--------------:|--------------:|
| 355 | 15/02/21 |        172824 |           698 |           6152 |             26 |         299 |             98312 |          68360 |             3389533 |                1337704 |       4727237 |         13304 |
| 356 | 16/02/21 |        173905 |          1121 |           6181 |             29 |         309 |             98312 |          69412 |             3411078 |                1356605 |       4767683 |         40446 |
| 357 | 17/02/21 |        174659 |           755 |           6194 |             13 |         313 |             98312 |          70153 |             3424721 |                1368686 |       4793407 |         25724 |
| 358 | 18/02/21 |        176059 |          1400 |           6221 |             27 |         320 |             98312 |          71526 |             3444687 |                1385729 |       4830416 |         37009 |
| 359 | 19/02/21 |        177494 |          1460 |            249 |             28 |         325 |             98312 |          78933 |             3467996 |                1408073 |       4876069 |         45653 |

and the plots until the same date (**19/02/21**) using the above dataframe were :
## Total Cases per day
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_19-02-21/TotalCases_19-02-21.png">
</p>

## Daily Cases
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_19-02-21/DailyCasesBars_19-02-21.png">
</p>

## Total & Daily Number of Cases
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_19-02-21/TotalDaily_19-02-21.png">
</p>

## Total Losses per day
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_19-02-21/TotalLosses_19-02-21.png">
</p>

## Daily Losses
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_19-02-21/DailyLossesBars_19-02-21.png">
</p>

## Total & Daily Losses
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_19-02-21/TotalDailyL_19-02-21.png">
</p>

## Intubated
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_19-02-21/Intubated_19-02-21.png">
</p>

## Total & Active Number of Cases
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_19-02-21/Total_ActiveCases_19-02-21.png">
</p>


## Total Cases per Month
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_19-02-21/PerMonth_19-02-21.png">
</p>

## Daily number of Tests
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_19-02-21/DailyTests_19-02-21.png">
</p>

## Total number of Tests
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_19-02-21/TotalTests_19-02-21.png">
</p>

## Total number of Tests (RT-PCR and RAPID AG)
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_19-02-21/Total_Tests_both_19-02-21.png">
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
