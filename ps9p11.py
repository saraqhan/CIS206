import re

url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"

pattern = re.compile(r'/(\d{4})/(\d{2})/(\d{2})/')
match = pattern.search(url)

year, month, date = match.groups() if match else (None, None, None)

print("Year:", year)
print("Month:", month)
print("Date:", date)

