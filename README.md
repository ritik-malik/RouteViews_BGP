# RouteViews_BGP
A bot to download BGP data from route views, &amp; filter according to the required AS (optional)

## Imput syntax
B = 1 for headless broswer, else 0 </br>
AS = 0, if no filtering required  </br>
IX = internet exchange from the list </br>
Syntax -> "B IX YYYYMMDD.time AS" 

## Steps done by bot
1. Go to http://archive.routeviews.org/  (GUI/headless)
2. Search for the requested data
3. Download the data, save it in cur dir, & quit the webdriver
4. Make a folder named after the IX (if not already there) & move the data
5. Decompress the data & run zebra-dump-parser on it
6. Filter AS if required, save it to new file & deleted the previous one



