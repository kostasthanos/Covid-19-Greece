# Covid-19-Greece
Data and Plots about the pandemic progression. 
## Last Update : 04/06/20

<p align="center">
  <img width="300" height="200" src="imgs/flag.png">
</p>

The data comes from the local csv file : *covid-19_greece_data.csv*

**Important Informations**
|     |   Date   | Information |  
| --- |    ---   |     ---     |
|  1  | 29/03/20 | 1st case in Mount Athos |  
|  2  | 31/03/20 | 20 cases on a ship outside the port of Piraeus |  
|  3  | 02/04/20 | 23 cases in the Ritsona refugee and immigrant camp, 79 cases on the ship El. Venizelos |
|  4  | 21/04/20 |
|  5  | 23/04/20 |
|  6  | 04/05/20 |
|  7  | 06/05/20 |
|  8  | 12/05/20 |
|  9  | 15/05/20 |
| 10  | 22/05/20 |
| 11  | 27/05/20 |
| 12  | 31/05/20 |
| 13  | 02/06/20 |
| 14  | 03/06/20 |
 

In this project we load two dataframes from the above data-file. 
The first one contains informations about : 

1. Dates  
2. Number of Total Cases  
3. Number of Daily Cases  
4. Increase %  
5. Number of Total Recovered  
6. Number of Active Cases  

For example the tail (last 5 rows) of the first dataframe for the date 18/05/20 is:  
|       |     Dates   |	Total Cases |	Daily Cases |	Increase % | Total Recovered | Active Cases |  
|  ---  |      ---    |     ---     |     ---    |       ---       |      ---     |  --- |
|  78   |     14/5    |	   2770     |	    10     |	    0.36%      |	    1374   	| 1396 |  
|  79   |	    15/5    |	   2810     |	    40     |	    1.44%      |	    1374    |	1436 |  
|  80   |	    16/5    |	   2819     |	     9     |	    0.32%      |	    1374    |	1445 |  
|  81   |     17/5    |	   2834     |	    15     |	    0.53%      |	    1374    |	1460 |  
|  82   |	    18/5    |	   2836     |	     2     |	    0.07%      |	    1374    |	1462 |  

The second dataframe contains one extra column about :  

7. Max Temperatures per Day  

For example the tail (last 5 rows) of the second dataframe for the date 18/05/20 is:  
|       |     Dates   |	Total Cases |	Daily Cases |	Increase % | Total Recovered | Active Cases |  Max Temperatures |  
|  ---  |      ---    |     ---     |     ---    |       ---       |      ---     |  --- |   --- |  
|  77 	|     13/5    | 	 2760     |	    16     |     	0.58% 	   |      1374 	  | 1386 |	31.7 |  
|  78   |     14/5    |	   2770     |	    10     |	    0.36%      |	    1374   	| 1396 |  32.4 |  
|  79   |	    15/5    |	   2810     |	    40     |	    1.44%      |	    1374    |	1436 |  36.7 |  
|  80   |	    16/5    |	   2819     |	     9     |	    0.32%      |	    1374    |	1445 |  38.2 |  
|  81   |     17/5    |	   2834     |	    15     |	    0.53%      |	    1374    |	1460 |  38.7 |  

In the second dataframe we use data until yesterday (- 1 day) because the temperature data are not yet available.

Until **18/05/20** some of the plots of the data were :
<p align="center">
  <img width="750" height="370" src="imgs/TotalCases.png">
</p>
<p align="center">
  <img width="750" height="370" src="imgs/DailyCasesBars.png">
</p>
<p align="center">
  <img width="750" height="370" src="imgs/TotalDaily.png">
</p>
<p align="center">
  <img width="750" height="370" src="imgs/TotalCasesandRecovered.png">
</p>
<p align="center">
  <img width="750" height="370" src="imgs/TotalandActiveCases.png">
</p>
<p align="center">
  <img width="750" height="370" src="imgs/CasesTemps.png">
</p>

**Note:** To see the plots of an exact date, choose the corresponding folder from Plots_per_Date.

The sources been used to extract the data are : 
1. https://covid19.gov.gr/covid19-live-analytics/  
2. https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Greece  
3. http://www.meteoacharnes.gr/statistika/datasummary.htm  

## Author
* **Konstantinos Thanos**
