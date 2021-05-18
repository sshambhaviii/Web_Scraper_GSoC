import csv

filename='gsoc2021.csv'
with open(filename,'w',encoding='utf8') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(['Name','Organisation','Project'])

    from requests_html import HTML
    with open('sitedata.html',encoding='utf8') as html_file:
        source=html_file.read()
        info=HTML(html=source)

    lists=info.find('li.project-card')
    for list in lists:
        data=list.find('div.pos-rel',first=True)
        name=data.find('h2',first=True).text
        org=data.find('a.md-soc-theme')
        csvwriter.writerow([name,org[1].text,org[0].text])


csvfile.close()
