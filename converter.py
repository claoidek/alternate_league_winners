from bs4 import BeautifulSoup
import csv
import os

def html2list(filename):
    soup = BeautifulSoup(open(filename, "r").read(), features="html.parser")

    table = soup.find_all("table")[1]

    headings = []
    rows =[]

    for heading in table.find_all("th"):
        headings.append(heading.text.replace('\n', ' ').strip())

    headings = headings[6:7] + headings[8:11] + headings[18:20]

    for row in table.find_all("tr"):
        new_row = []
        for element in row.find_all("td"):
            new_row.append(element.text.replace('\n', ' ').strip())
        if len(new_row)>5:
            new_row[4] = int(new_row[4]) + int(new_row[9])
            new_row[5] = int(new_row[5]) + int(new_row[10])
            new_row[6] = int(new_row[6]) + int(new_row[11])
            new_row[14] = float(new_row[14])
            new_row[15] = int(new_row[15])
            new_row = new_row[2:3] + new_row[4:7] + new_row[14:16]
            rows.append(new_row)

    # The tables for 1957-1959 are stored differently and need to have the lower
    # divisions removed from the end
    if len(rows)>22:
        rows = rows[0:22]

    return [headings] + rows

def extract_data():
    tables = {}
    for year in range(1888,2021):
        if (year > 1914 and year < 1919) or (year > 1938 and year < 1946):
            continue
        filename = "f" + str(year) + "-" + str(((year+1)%100)).zfill(2) + ".html"
        tables[year] = html2list(os.path.join("html_league_tables",filename))
    return tables

def write_to_csv(tables):
    for year in tables:
        filename = str(year) + ".csv"
        filename = os.path.join("csv_league_tables",filename)
        with open(filename,"w") as f:
            write = csv.writer(f)
            write.writerows(tables[year])
    return


if __name__ == "__main__":
    tables = extract_data()
    write_to_csv(tables)
