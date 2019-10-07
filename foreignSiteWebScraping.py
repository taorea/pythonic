import requests
from bs4 import BeautifulSoup
import csv
def get_html(bas_url,headers):
    r = requests.get(bas_url,headers = headers)
    print(r.status_code)
    r.encoding = r.apparent_encoding
    return r.text

def parse_html(html):
    soup = BeautifulSoup(html,"html.parser")
    return soup

def abstract(soup):
    table = soup.find('table',attrs = {'class':"tableSorter"})
    results = table.find_all('tr')
    print("numbers of results:",len(results))
    rows = []
    #表头
    rows.append(['rank','company','website',"location","yearend","2-years growth","international sales","total sales","staff","comment"])
    print(rows)
    for result in results:
        data = result.find_all('td')
        if data == []:
            continue
        #print(data)
        rank = data[0].getText()
        company = data[1].find('span',attrs={"class":"company-name"}).getText()
        #获取company的公司官网
        href = data[1].find("a").get("href")
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'}
        html_com = get_html(href,headers)
        soup2 = parse_html(html_com)
        try:
            tr = soup2.find_all("tr")[-1]
            website = tr.find('a').get('href')
        except:
            website = None
        # print(website)
        location = data[2].getText()
        yearend = data[3].getText()
        growth = data[4].getText()
        internationalSales = data[5].getText().strip("*").strip("†").strip("*").replace(",","")
        totalsales = data[6].getText().strip("*").strip("†").strip("*").replace(",","")
        staff = data[7].getText()
        comment = data[8].getText()
        rows.append([rank,company,website,location,yearend,growth,internationalSales,totalsales,staff,comment])
    return rows

def save_csv_file(rows):
    with open("fasttrack100.csv",'w',newline='',encoding="utf-8") as f_output: #不加newline=""会有空行
        csv_output = csv.writer(f_output)
        csv_output.writerows(rows)

def main():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'}
    bas_url = "https://www.fasttrack.co.uk/league-tables/sme-export-track-100/league-table/"
    total_html = get_html(bas_url,headers)
    soup = parse_html(total_html)
    rows_info = abstract(soup)
    save_csv_file(rows_info)
if __name__ == "__main__":
    main()