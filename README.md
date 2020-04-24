# RouteViews_BGP
A bot to download BGP data from route views, &amp; filter according to the required AS (optional)

## Syntax
python data.py  </br>
Input syntax -> "B IX YYYYMMDD.time AS" </br></br>
B = 1 for headless broswer, else 0 </br>
AS = 0, if no filtering required  </br>
IX = internet exchange from the list </br>
 

## Steps done by bot
1. Go to http://archive.routeviews.org/  (GUI/headless)
2. Search for the requested data & download it
3. Save it in cur dir, & quit the webdriver
4. Make a folder named after the IX (if not already there) & move the data
5. Decompress the x-bzip2 archive & run zebra-dump-parser on it
6. Filter AS if required, save it to new file & deleted the previous one



