import re
from collections import defaultdict

articlesdata = {
    "Title1": 1000,
    "Title2/Subpage1": 500,
    "Title2/Subpage2": 700,
    "Title3": 800,
    "Title4/Subpage1": 600,
    "Title5": 1200,
    "Title5/Subpage1": 300,
}

def separatetitles(articlesdata):
    titlescounts = defaultdict(int)
    for title, count in articlesdata.items():
        match = re.match(r'(.+?)(?:/.+)?$', title)
        if match:
            maintitle = match.group(1)
            titlescounts[maintitle] += count
    return titlescounts

def displaytopprojects(titlescounts):
    sortedprojects = sorted(titlescounts.items(), key=lambda x: (-x[1], x[0]))
    for i, (project, views) in enumerate(sortedprojects[:100], start=1):
        print(f"{i}. {project}: {views} views")

titlescounts = separatetitles(articlesdata)

displaytopprojects(titlescounts)
