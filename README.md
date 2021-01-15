# Covid-19-Greece
Data and Plots about the pandemic progression in Greece. 

| Last Update |  Total Cases | Days |
|     ---     |      ---     |  --- |
|  15-01-21   |    147860    |  325 |

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
6. Total RTPCR tests
7. Total RAPID AG tests
8. Total Tests
9. Daily Tests


For example the tail (last 5 rows) of the dataframe for the date **15/01/21** were:  
|       |       Dates     |	Total Cases |	Daily Cases | Total Recovered | Active Cases | Total RTPCR tests | Total RAPID AG tests | Total Tests | Daily Tests |
|  ---  |        ---      |     ---     |     ---     |       ---       |      ---     |        ---        |          ---         |     ---     |      ---    |
|  321  |     11/01/21    |   145179    |     444     |      98312      |     41565    |      2897143      |         716066       |   3613209   |     16670   |
|  322  |     12/01/21    |   146020    |     866     |      98312      |     42379    |      2909699      |         745184       |   3654883   |     41674   |
|  323  |     13/01/21    |   146688    |     671     |      98312      |     43022    |      2921563      |         768300       |   3689863   |     34980   |
|  324  |     14/01/21    |   147283    |     599     |      98312      |     43584    |      2933838      |         791064       |   3724902   |     35039   |
|  325  |     15/01/21    |   147860    |     610     |      98312      |     44127    |      2945406      |         812024       |   3757430   |     32528   |

and the plots until the same date (**15/01/21**) using the above dataframe were :
## Total Cases per day
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_15-01-21/TotalCases_15-01-21.png">
</p>

## Daily Cases
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_15-01-21/DailyCasesBars_15-01-21.png">
</p>

## Total Cases & Total Recovered
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_15-01-21/TotalCases_Recovered_15-01-21.png">
</p>

## Total & Active Number of Cases
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_15-01-21/Total_ActiveCases_15-01-21.png">
</p>

## Total & Daily Number of Cases
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_15-01-21/TotalDaily_15-01-21.png">
</p>

## Total Cases per Month
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_15-01-21/PerMonth_15-01-21.png">
</p>

## Daily number of Tests
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_15-01-21/DailyTests_15-01-21.png">
</p>

## Total number of Tests
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_15-01-21/TotalTests_15-01-21.png">
</p>

## Total number of Tests (RT-PCR and RAPID AG)
<p align="center">
  <img width="950" height="468" src="Plots_per_Date/Plots_for_15-01-21/Total_Tests_both_15-01-21.png">
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
