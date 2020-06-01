# Dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd

def scrape():
    # define browser object
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit mars news url
    mars_news_url = 'https://mars.nasa.gov/news/'
    browser.visit(mars_news_url)
    html = browser.html
    soup = bs(html, 'html.parser')

    # Scrape mars news info
    # Headline text
    headline_exp = soup.find('div', class_="article_teaser_body").text

    # Headline link and url
    headline_link = soup.find('div', class_='list_text').find('div', class_='content_title')
    headline_text = headline_link.text
    headline_url = 'https://mars.nasa.gov/'+headline_link.a['href']

    # Checks JPL image
    jpl_img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_img_url)
    html = browser.html
    soup = bs(html, 'html.parser')
    jpl_image_url_out = 'https://www.jpl.nasa.gov/'+soup.footer.find('a', class_='button fancybox')['data-fancybox-href']

    # Link to mars facts
    mars_facts_url = 'https://space-facts.com/mars/'
    browser.visit(mars_facts_url)
    html = browser.html
    soup = bs(html, 'html.parser')

    # stores mars facts table as two separate lists
    x = 1
    labels =[]
    values = []
    mars_table = soup.find('table', class_='tablepress tablepress-id-p-mars')
    for z in range(1,19):
        mars_table = mars_table.find_next('td')
        if x % 2 ==0:
            values.append(mars_table.text)
        else:
            labels.append(mars_table.text)
        x+=1
    facts_dict ={'Type':labels,'Fact':values}
    facts_df = pd.DataFrame(facts_dict)
    facts_html = facts_df.to_html

        # List of hemispheres
    hemis = ['Cerberus','Schiaparelli','Syrtis','Valles']

    # Empty list of img urls
    hemi_url_list = []

    # Open browser and visit main page
    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(hemi_url)

    # For loop to pull hemi images
    for h in hemis:
        browser.links.find_by_partial_text(h).first.click()
        html = browser.html
        soup = bs(html, 'html.parser')
        img_url = soup.find('div', class_='downloads').ul.li.a['href']
        hemi_url_list.append(img_url)
        browser.back

    # list of dictionaries containing image name and urls
    cerb_img = hemi_url_list[0]
    schi_img = hemi_url_list[1]
    syrt_img = hemi_url_list[2]
    valles_img = hemi_url_list[3]

    # Twitter open and setup
    twitter_url = 'https://twitter.com/marswxreport?lang=en'
    #browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(twitter_url)
    html = browser.html
    soup = bs(html, 'html.parser')

    # Finds all text and searches for first weather string, assigning it to weather_str variable
    mars_weather = soup.find_all(text=True)
    for w in mars_weather:
        if w.find('InSight sol')!=-1:
            weather_str = w
            break

    mars_dict = {
    'headline': headline_text,
    'paragraph': headline_exp,
    'currentimage': jpl_image_url_out,
    'weather': weather_str,
    'cerb': cerb_img,
    'schi': schi_img,
    'syrt' : syrt_img,
    'valles': valles_img
    #'table': facts_html,
    }
    return mars_dict