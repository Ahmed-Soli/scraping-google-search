
# will be using https://serpapi.com/search

import requests
def Search(dork='',start=0,num=100):
  dork=f'intext:{dork}'
  payload = {
        'api_key': your api token here,
        'engine': 'google', 'q': dork, 'start': start * 100, 'num': num}
  res = requests.get('https://serpapi.com/search', params=payload)
  if res.status_code == 200:
    return res.json()

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
                links.append(item['link'])
        print("Saving\nThat's all Good Bye")
		    with open('links.txt','w')as f:
		        f.write('\n'.join(links))
  except Exception as e:
    print(e)

  




 Catch('pass in the search word')
