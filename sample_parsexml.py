import xml.etree.cElementTree as et

tree = et.parse("sample.xml")

root = tree.getroot()
Job_title = []
Company_name = []

for title in root.iter('job_title'):
    Job_title.append(title.text)

for company in root.iter('company_name'):
    Company_name.append(company.text)


print("Job Title", Job_title)
print("Company Name", Company_name)