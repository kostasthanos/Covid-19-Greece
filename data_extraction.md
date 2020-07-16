The procedure followed for the collection of the data from the daily reports about Covid-19 progression in Greece is the following :  

**Note:**  Every daily report is being saved as pdf file with a specific url containg the date

1. Set the current (daily) report url of the pdf file.

```
eody_url = 'https://eody.gov.gr/wp-content/uploads/' + current_year + '/' + month + '/covid-gr-daily-report-' + current_year + month + day + '.pdf'
```
e.g. For 13/07 : 'https://eody.gov.gr/wp-content/uploads/2020/07/covid-gr-daily-report-20200713.pdf'
