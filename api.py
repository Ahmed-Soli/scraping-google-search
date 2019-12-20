"""
will be using https://serpapi.com/search 
provides Real Time and Real Results with no captch or recaptch or limitations
you can run the script using any clould based service
"""

import requests
"""
the Search function will take three paramters 
1-the search word
2-the starting page number (fisrt page is 0 and so on )
3-how many results to retrieve per page (max 100)
"""
def Search(dork,start=0,num=10):
	print('Searching with {}'.format(dork))
	# dork=f'intext:{dork}' # for advanced search query
	payload = {
		'api_key': 'yout api key here',
		'engine': 'google', 'q': dork, 'start': start * 100, 'num': num}
	res = requests.get('https://serpapi.com/search', params=payload)
	if res.status_code == 200:
  		return res.json() # retrieve a json respnse 

def Catch(dork):
	try:
		JsonObj          = Search(dork)
		Data             = JsonObj.get('organic_results',[])
		if Data:
			links = []
			Current_page     = JsonObj['serpapi_pagination']['current']
			Total_Pages      = JsonObj['serpapi_pagination']['other_pages']
			print(f'you are currently in page {Current_page} out of {len(Total_Pages)+1}')
			for i in range(0,len(Total_Pages)+1):
				if i != 0 :
					JsonObj          = Search(dork,start=i)
					Data             = JsonObj.get('organic_results',[])
				print(f'\nGetting page {i+1} out of {len(Total_Pages)+1}')
				if Data:
					print(f'## Found {len(Data)} results in page {i+1}')
					for item in Data:
				  		if item not in links :
				  			search_result_link = item['link']
				  			links.append(search_result_link)
				  			print(search_result_link)
			print(f"Found {len(links)} Links \nSaving.....\nThat's all Good Bye")
			with open('links.txt','w')as f:
				f.write('\n'.join(links))
	except Exception as e:    print(e)

# to run the script Just pass the search word 
Catch('pass in search word')


"""
Example Catch('web scraping')

output:
Searching with web scraping
you are currently in page 1 out of 10

Getting page 1 out of 10
## Found 9 results in page 1
https://en.wikipedia.org/wiki/Web_scraping
https://www.webharvy.com/articles/what-is-web-scraping.html
https://blog.hartleybrody.com/web-scraping/
https://realpython.com/tutorials/web-scraping/
https://webscraper.io/
https://scrapinghub.com/what-is-web-scraping
https://www.scraperapi.com/blog/the-10-best-web-scraping-tools
https://www.parsehub.com/
https://www.guru99.com/web-scraping-tools.html
Searching with web scraping

Getting page 2 out of 10
## Found 10 results in page 2
https://www.makeuseof.com/tag/what-is-web-scraping/
https://www.thedataschool.co.uk/manuela-marolla/web-scraping-101-a-short-introduction/
https://stackabuse.com/introduction-to-web-scraping-with-python/
https://www.reddit.com/r/programming/comments/ecvc42/a_guide_to_web_scraping_without_getting_blocked/
https://github.com/codingforentrepreneurs/Web-Scraping
http://sergeyzhuk.me/2018/02/12/fast-webscraping-with-reactphp/
https://blog.floydhub.com/web-scraping-with-python/
https://ahrefs.com/blog/web-scraping-for-marketers/
https://quickleft.com/blog/is-web-scraping-ethical/
https://www.perimeterx.com/blog/how-web-scrapping-damages-business/
Searching with web scraping

Getting page 3 out of 10
## Found 2 results in page 3
http://zewr.physiotherapie-hahn.de/manual-web-scraping.html
http://txgi.physiotherapie-hahn.de/web-scraping-python-ppt.html

"""
