# Covid-19-Greece
Data and Plots about the pandemic progression in Greece. 

| Last Update | Total Cases | Days |
|     ---     |     ---     |  --- |
|  15-07-20   |     3910    |  140 |

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

For example the tail (last 5 rows) of the dataframe for the date **13/07/20** were:  
|       |     Dates   |	Total Cases |	Daily Cases | Total Recovered | Active Cases | 
|  ---  |      ---    |     ---     |     ---    |       ---        |      ---     |
|  134  |    09/07    |	   3672     |	    50     |	     1374     	|     2105     |
|  135  |	   10/07    |	   3732     |	    60     |	     1374       |	    2165     | 
|  136  |	   11/07    |	   3772     |	    41     |	     1374       |	    2205     |
|  137  |    12/07    |	   3803     |	    31     |	     1374       |	    2236     |
|  138  |	   13/07    |	   3826     |	    24     |	     1374       |	    2259     |


and some of the plots until the same date (**13/07/20**) using the above dataframe were :

## Total Cases per day
<p align="center">
  <img width="750" height="370" src="Plots_per_Date/Plots_for_13-07-2020/TotalCases_13-07-2020.png">
</p>

## Daily Cases
<p align="center">
  <img width="750" height="370" src="Plots_per_Date/Plots_for_13-07-2020/DailyCasesBars_13-07-2020.png">
</p>

## Total Cases & Total Recovered
<p align="center">
  <img width="750" height="370" src="Plots_per_Date/Plots_for_13-07-2020/TotalCases_Recovered_13-07-2020.png">
</p>

## Total & Active number of Cases
<p align="center">
  <img width="750" height="370" src="Plots_per_Date/Plots_for_13-07-2020/Total_ActiveCases_13-07-2020.png">
</p>

## Total & Daily Number of Cases
<p align="center">
  <img width="750" height="370" src="Plots_per_Date/Plots_for_13-07-2020/TotalDaily_13-07-2020.png">
</p>

**Note:** To see the plots of an exact date, choose the corresponding folder from *Plots_per_Date*.

## Check the jupyter notebook file
For a deeper understanding on how the data are being collected and used see the file *Covid-19_Data_Greece.ipynb* which contains all the necessary python comments describing each step of the project.

The sources been used to extract the data are : 

**Covid19.gov.gr** : https://eody.gov.gr/category/covid-19/

**Note:** Max Temperature data has been deleted from the csv file.

## Author
* **Konstantinos Thanos**
