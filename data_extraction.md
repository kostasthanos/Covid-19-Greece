The procedure followed for the collection of the data from the daily reports about Covid-19 progression in Greece is the following :  

**Note:**  Every daily report is being saved as pdf file with a specific url containg the date

**[1]** Set the current (daily report) url for the pdf file.

```
eody_url = 'https://eody.gov.gr/wp-content/uploads/' + current_year + '/'  \
            + month + '/covid-gr-daily-report-' + current_year + month + day + '.pdf'
```
For example if we want the daily report for the date 13/07, the corresponding url will be:   
'https://eody.gov.gr/wp-content/uploads/2020/07/covid-gr-daily-report-20200713.pdf'

**[2]** Check if this url is valid or if it's returning any other problem like *page not found*.

```
from lxml.html import fromstring
pdf_file_check = fromstring(requests.get(eody_url).content)
test = pdf_file_check.findtext('.//title').split('-')[0].strip()
```
We can do this by checking the .//title from the page informations.  In this case we can try a different url format like the following.
```
 eody_url = 'https://eody.gov.gr/wp-content/uploads/2020/07/daily-report-COVID-19_' \
             + day + '.' + month + '.' + current_year + '.pdf'
```
**[3]** Return the status code from the web page by request.
```
pdf_file = requests.get(eody_url)
```

**[4]** Save as pdf the content from the page url. Create a new file with name *daily_report.pdf*.
```
open('daily_report.pdf', 'wb').write(pdf_file.content)
```

**[5]** Use **pdfminer** and **pdf2txt.py** to convert the above pdf file to a text file with name *pdf_to_txt*
```
!pdf2txt.py -o pdf_to_txt daily_report.pdf
```

**[6]** Open text file in read mode in order to read it's content and initialize an empty list in which the data will be saved.
```
newpath = 'pdf_to_txt' # Or pdf_to_txt.txt

data = []

with open(newpath, 'r') as report:
    report_content = report.read()
```

**[7]** Use regular expressions to find the necessary data from the text file and save them in the list.
```
init_data_a = re.findall(r'Τα νέα εργαστηριακά επιβεβαιωμένα κρούσματα της νόσου είναι (\d+)',  report_content)
init_data_b = re.findall(r'Ο συνολικός αριθμός των κρουσμάτων ανέρχεται σε (\d+)',  report_content)
init_data_c = re.findall(r'(\d+) θάνατοι', report_content)
data.append(int(init_data_a[0]))
data.append(int(init_data_b[0]))
data.append(int(init_data_c[0]))
report.close()
```    
