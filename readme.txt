Using python scrapy to create a web crawler that crawls through a website to a given depth, extracting selected pieces of information in search of information matching our keywords.

Things I am trying to achieve:
1) extract some info and save to a csv
2) playing around with settings to scrape to a given depth (e.g., 3 clicks deep on pages starting with the initial domain name)
3) use keyword searches to select the info we extract


11/01/2016
Spider works by running “scrapy crawl kngs —output kngsddmmyy.csv” in terminal from this folder. This currently exports the html of every page to the csv - this is a test to see if we can extract the page html as we scrape and not a long term solution.