from bs4 import BeautifulSoup

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
        if len(new_row)>1:
            new_row[4] = int(new_row[4]) + int(new_row[9])
            new_row[5] = int(new_row[5]) + int(new_row[10])
            new_row[6] = int(new_row[6]) + int(new_row[11])
            new_row[14] = float(new_row[14])
            new_row[15] = int(new_row[15])
            new_row = new_row[2:3] + new_row[4:7] + new_row[14:16]
            rows.append(new_row)

    return [headings] + rows
