import re
import requests

# Set curret pdf url
eody_url = 'https://eody.gov.gr/wp-content/uploads/' + current_year + '/' + month + '/covid-gr-daily-report-' + current_year + month + day + '.pdf'

# Check if the above page url has any problem (not exists) 
# Check the .//title from this url
from lxml.html import fromstring
pdf_file_check = fromstring(requests.get(eody_url).content)
test = pdf_file_check.findtext('.//title').split('-')[0].strip()

# Try the below url format in case of problem
if test=='Η σελίδα δεν βρέθηκε':
    eody_url = 'https://eody.gov.gr/wp-content/uploads/2020/07/daily-report-COVID-19_' + day + '.' + month + '.' + current_year + '.pdf'
    
pdf_file = requests.get(eody_url)

# Save daily report pdf
open('daily_report.pdf', 'wb').write(pdf_file.content)

# Save daily_report.pdf content to text file using pdminer and pdf2txt.py
# pdf2txt.py [-o output_file] initial_pdf_file
!pdf2txt.py -o pdf_to_txt daily_report.pdf

# Set name of text file
newpath = 'pdf_to_txt' # Or pdf_to_txt.txt

data = []

with open(newpath, 'r') as report:
    report_content = report.read()
    
    # Use of regular expressions to find needed data
    init_data_a = re.findall(r'Τα νέα εργαστηριακά επιβεβαιωμένα κρούσματα της νόσου είναι (\d+)',  report_content)
    init_data_b = re.findall(r'Ο συνολικός αριθμός των κρουσμάτων ανέρχεται σε (\d+)',  report_content)
    init_data_c = re.findall(r'(\d+) θάνατοι', report_content)
    data.append(int(init_data_a[0]))
    data.append(int(init_data_b[0]))
    data.append(int(init_data_c[0]))
    
    report.close()
