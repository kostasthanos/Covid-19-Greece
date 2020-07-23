The procedure followed for the collection of the data from the daily reports about Covid-19 progression in Greece is the following :  

**Note:**  Every daily report is being saved as a pdf file with a specific url containg the date

**[1]** Set the current (daily report) url for the pdf file.

```
eody_url = 'https://eody.gov.gr/wp-content/uploads/' + current_year + '/' + month +\
           '/covid-gr-daily-report-' + current_year + month + day + '.pdf'
```
For example if we want the daily report for the date 23/07, the corresponding url will be:   
'https://eody.gov.gr/wp-content/uploads/2020/07/covid-gr-daily-report-20200723.pdf'

**[2]** Return the status code from the web page by request.
```
pdf_file = requests.get(eody_url)
```

**[3]** Save as pdf the content from the page url. Create a new file with name *daily_report.pdf*.
```
open('daily_report.pdf', 'wb').write(pdf_file.content)
```

**[4]** Use **pdfminer** and **pdf2txt.py** to convert the above pdf file to a text file with name *pdf_to_txt*
```
!pdf2txt.py -o pdf_to_txt daily_report.pdf
```

**[5]** Open text file in read mode in order to read it's content and initialize an empty list in which the data will be saved.
```
newpath = 'pdf_to_txt' # Or pdf_to_txt.txt

data = []

with open(newpath, 'r') as report:
    report_content = report.read()
```

**[6]** Use regular expressions to find the necessary data from the text file and save them in the list.
```
init_data_a = re.findall(r'Τα νέα εργαστηριακά επιβεβαιωμένα κρούσματα της νόσου είναι (\d+)',  report_content)
init_data_b = re.findall(r'Ο συνολικός αριθμός των κρουσμάτων ανέρχεται σε (\d+)',  report_content)
init_data_c = re.findall(r'(\d+) θάνατοι', report_content)
data.append(int(init_data_a[0]))
data.append(int(init_data_b[0]))
data.append(int(init_data_c[0]))
report.close()
```    
