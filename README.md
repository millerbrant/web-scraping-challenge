# web-scraping-challenge

# Time for me to admit defeat on the web scraping homework.  I've not been able to get my app to run the scrape with any consistency.
# I used the untitled juptyer notebook to test my scraping app. Sticking point was always the Mars News headline, which
# would error out because the BS object wouldn't be recognized and thus had no attribute: text.  Evening putting in a minute-long delay
# between browser navigation and soup object creation resulted in a 1 out of 5 success rate.

# I disabled the drop collection in app.py, this was causing the page to load blank data when the scrape app failed out. I had additional
# issues handling this with a try/except block.  I was also unable to render my mars facts dataframe as an html object that could be
# passed through to my flask app, every attempt would note that flask was unable to handle.

# Apologies for the late and incomplete submission, I've been banging my head against the same bs4 wall for the last week and it was time
# to submit what I had, I'm absolutely mystified by my scrape issues and my error handling attempts have complicated things even further.
