import requests
from bs4 import BeautifulSoup
from enum import Enum

from .models import MountainDates


class mountain_url(Enum):
    bigsky = 'https://www.bigskyresort.com/events'
    snowbowl = 'https://www.montanasnowbowl.com/winter-events/'
    discovery_ski = 'https://www.skidiscovery.com/'    

def mountain_rss():
    mountain_list = []
    headers = {
     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }  
    try:

        for mount in (mountain_url):         
            url = mount.value        
            req = requests.get(url, headers = headers)
            soup = BeautifulSoup(req.content, "html.parser")
                        
            if mount.name == 'bigsky':
                mountain = mount.name
                winter_season_open = soup.h4.get_text()
                url = ('https://bigskyresort.com/press-releases/big-sky-resort-to-open-for-summer-season-x21337')        
                req = requests.get(url, headers = headers)
                soup = BeautifulSoup(req.content, "html.parser")
                res = soup.find('span', attrs={'class':'text text_11 mix-text_subtitle'})
                txt = res.get_text()
                txt_list = txt.split(',')
                summer_season_open = txt_list[0]                
                winter_season_close = 'N/A'
                summer_season_close = 'N/A' 
                link = mount.value                                              
                scraped_details = {
                    'mountain' : mountain,
                    'winter_season_open' : winter_season_open,
                    'winter_season_close': winter_season_close,
                    'summer_season_open' : summer_season_open,
                    'summer_season_close' : summer_season_close,
                    'link':link                    
                }
                print(scraped_details)
                       
            
            if mount.name == 'snowbowl':
                mountain = mount.name
                winter_season_open = 'Dec 10'
                winter_season_close = 'Apr 4'
                summer_season_open = 'N/A'
                summer_season_close = 'N/A'
                link = mount.value

                scraped_details = {
                    'mountain' : mountain,
                    'winter_season_open' : winter_season_open,
                    'winter_season_close': winter_season_close,
                    'summer_season_open' : summer_season_open,
                    'summer_season_close' : summer_season_close,
                    'link':link                    
                }
                                  
            if mount.name == 'discovery_ski':#finds the details for Discovery ski resort
                mountain = mount.name
                link = mount.value
                res = soup.find_all('p', attrs={'class':'little-title'})
                for i in res:                    
                    if ('Thanksgiving' in i.get_text()):
                        txt = i.get_text()                        
                        txt_list = txt.split('-')                        
                        winter_season_open = txt_list[0]
                        winter_season_close = txt_list[1]                        
                    if ('May' in i.get_text()):
                        txt = i.get_text()
                        txt_list = txt.split('-')                        
                        summer_season_open = txt_list[0]
                        summer_season_close = txt_list[2]
                        print(summer_season_close)
                    
                scraped_details = {
                    'mountain' : mountain,
                    'winter_season_open' : winter_season_open,
                    'winter_season_close': winter_season_close,
                    'summer_season_open' : summer_season_open,
                    'summer_season_close' : summer_season_close,
                    'link': link                    
                }
                
                    
                
            mountain_list.append(scraped_details) 
            print(mountain_list)                       
            save_function(mountain_list)
            mountain_list.clear()
            

    except Exception as e:
        print("webscrape failed ")
        print(e)    

def save_function(mountain_list):
    
    winter_season_open = mountain_list[0]['winter_season_open']
    #winter_season_close = mountain_list[0]['winter_season_close']
    error = True
    
    try:
        latest_date = MountainDates.objects.filter(winter_season_open = winter_season_open).order_by('-id')[0]
        print(latest_date)
    except Exception as e:
        print(e)
        error = False
        pass
    finally:
        if error is not True:
            latest_date = None
    try:
        for details in mountain_list:
            if latest_date == None:
                try:
                    MountainDates.objects.create(
                       
                        mountain = details['mountain'],
                        winter_season_open = details['winter_season_open'],
                        winter_season_close = details['winter_season_close'],
                        summer_season_open = details['summer_season_open'],
                        summer_season_close = details['summer_season_close'],
                        link = details['link'],
                        

                     )
                except Exception as e:
                    print('failed')
                    print(e)
                    break
            else:
                return print("scrape failed")
    except Exception as e:
        print(e)
        error = False



