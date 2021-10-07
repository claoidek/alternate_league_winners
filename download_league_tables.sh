#!/bin/bash

mkdir -p html_league_tables
cd html_league_tables

BASE_URL="http://www.englishfootballleaguetables.co.uk/final/f"

for year in {1888..2020}
do
    # Skip War Years
    if [[ "$year" > 1914 && "$year" < 1919 ]] || [[ "$year" > 1938 && "$year" < 1946 ]]; then
        continue
    fi
    printf -v next_year "%02d" $(($(($year+1))%100))
    wget "$BASE_URL""$year""-""$next_year"".html"
done
