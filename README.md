# Covid-19-Greece
Data and Plots about the pandemic progression. 
## Last Update : 18/05/20

<p align="center">
  <img width="300" height="200" src="flag.png">
</p>

The data comes from the local csv file : *covid-19_greece_data.csv*

In this project we load two dataframes from the above data-file. 
The first one contains informations about : 

1. Dates  
2. Number of Total Cases  
3. Number of Daily Cases  
4. Increase %  
5. Number of Total Recovered  
6. Number of Active Cases  

The second dataframe contains one extra column about :

7. Max Temperatures per Day

In the second dataframe we use data until yesterday (- 1 day) because the temperature data are not yet available.

The sources that been used to extract the data are : 
1. https://covid19.gov.gr/covid19-live-analytics/  
2. https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Greece  
3. http://www.meteoacharnes.gr/statistika/datasummary.htm  

There is also one extra .ods (Libre Office Calc) file (like Excel) in which we can see the same results as in the jupyter notebook.

## Author
* **Konstantinos Thanos**
