def list_of_teams(tables):
    teams = set()
    for year in tables:
        num_teams = len(tables[year]) - 1
        for team in range(1,num_teams + 1):
            teams.add(tables[year][team][0])
            if tables[year][team][0] == "Darwen":
                print(year)
    return teams

