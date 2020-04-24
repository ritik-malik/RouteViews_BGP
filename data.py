from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
import time
import os


def process_DATA(x,path):
    
    if(x[1]=='1'):
        folder = 'Chicago'
    elif(x[1]=='2'):
        folder = 'Chile'
    elif(x[1]=='3'):
        folder = 'Equinix'
    elif(x[1]=='4'):
        folder = 'FL-IX'
    elif(x[1]=='5'):
        folder = 'Gorex'
    elif(x[1]=='6'):
        folder = 'PAIX'
    elif(x[1]=='7'):
        folder = 'KIXP'
    elif(x[1]=='8'):
        folder = 'JINX'
    elif(x[1]=='9'):
        folder = 'LINX'
    elif(x[1]=='10'):
        folder = 'NAPAfrica'
    elif(x[1]=='11'):
        folder = 'NWAX'
    elif(x[1]=='12'):
        folder = 'PhOpenIX'
    elif(x[1]=='13'):
        folder = 'TELXATL'
    elif(x[1]=='14'):
        folder = 'DIXIE'
    elif(x[1]=='15'):
        folder = 'SYDNEY'
    elif(x[1]=='16'):
        folder = 'SAOPAULO'
    elif(x[1]=='17'):
        folder = 'SAOPAULO_2'
    elif(x[1]=='18'):
        folder = 'SINGAPORE'
    elif(x[1]=='19'):
        folder = 'PERTH'
    elif(x[1]=='20'):
        folder = 'SFMIX'
    elif(x[1]=='21'):
        folder = 'Serbia'
    elif(x[1]=='22'):
        folder = 'MWIX'
    elif(x[1]=='23'):
        folder = 'RIO'
    elif(x[1]=='24'):
        folder = 'FORTALEZA'
    else:
        folder = 'GIXA'
    
    print('Making required folder, & shifting the data\n')
    
    temp = 'mkdir -p '+folder
    os.system(temp)                         # create new dir
    
    move = 'mv ' + path + ' ' + folder
    os.system(move)                     # mv the archive
    
    os.chdir(folder)       # cd
    
    print('decompressing the archive...\n')
    temp = 'bzip2 -d '+path
    os.system(temp)             # decompress


    print('running zebra-dump parser...\n')
    os.system('format=2')
    temp = 'cat '+path[:-4]+' | '+'perl ../zebra-dump-parser/zebra-dump-parser.pl >'+path[:-4]+'_dumps'+' 2>dump_errors'
    os.system(temp)
    temp = 'rm '+path[:-4]
    os.system(temp)
    
    path = path[:-4] + '_dumps'

    if(x[3]=='0'):
        print('No AS provided for filtering, quitting...\n')
        quit()
    else:
        print('Filtering ',x[3])

        # awk '$2=="37611"' rib_dumps
        temp="awk '$2=="+'"'+x[3]+'"'+"' "+path+" > "+path+'_filtered'

        os.system(temp)
        os.remove(path)
        print('filtered the given AS, quitting...\n')
        
        
def download_DATA(x):

    print('Setting up firefox profile...\n')

    profile = FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.panel.shown", False)
    profile.set_preference("browser.helperApps.neverAsk.openFile","application/x-bzip2")
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-bzip2")
    profile.set_preference("browser.download.dir", os.getcwd())
  
    # profile.set_preference()

    options = Options()
    if(x[0]=='1'):
        options.headless = True
    else:
        options.headless = False    

    pwd = os.getcwd()
    pwd=pwd+'/geckodriver'
    driver = webdriver.Firefox(options=options, executable_path=pwd, firefox_profile=profile)
    driver.get("http://archive.routeviews.org/")

    path = '/html/body/ul/ul[1]/li[1]/a['+str(int(x[1])+5)+']'      # add 5 to x[1]
    driver.find_element_by_xpath(path).click()                      # click on IX

    path = x[2][:4]+'.'+x[2][4:6]+'/'                               # Make yyyy.mm
    driver.find_element_by_xpath('//a[@href="'+path+'"]').click()   # click on YYYY.MM

    driver.find_element_by_xpath('//a[@href="'+'RIBS/'+'"]').click()     # click on RIBS


    path = 'rib.'+x[2]+'.bz2'
    driver.find_element_by_xpath('//a[@href="'+path+'"]').click()
    
    print('Downloading data')
    
    temp = path+'.part'
    while(temp in os.listdir('.')):     # wait till it downloads
        time.sleep(5)

    print('Download complete, closing the driver\n')    
    driver.close()
    
    process_DATA(x,path)
    


def intro():

    print('MRT format RIBs and UPDATEs from -')
    print('1  - Chicago     \t   2  - Chile      ')
    print('3  - Equinix     \t   4  - FL-IX      ')
    print('5  - Gorex       \t   6  - PAIX       ')
    print('7  - KIXP        \t   8  - JINX       ')
    print('9  - LINX        \t   10 - NAPAfrica ')
    print('11 - NWAX        \t   12 - PhOpenIX  ')
    print('13 - TELXATL     \t   14 - DIXIE     ')
    print('15 - SYDNEY      \t   16 - SAOPAULO  ')
    print('17 - SAOPAULO_2  \t   18 - SINGAPORE ')
    print('19 - PERTH       \t   20 - SFMIX     ')
    print('21 - Serbia      \t   22 - MWIX      ')
    print('23 - RIO         \t   24 - FORTALEZA ')
    print('25 - GIXA \n')

    print('B = 1 for headless broswer, else 0')
    print('AS = 0, if no filtering required\n')
    x = input('Syntax -> "B IX YYYYMMDD.time AS" : ').split()

    download_DATA(x)

    # 0 18 20160307.1800 9737
    
intro()