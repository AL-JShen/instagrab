import requests
import urllib
import urllib.request
import os
import errno

username = input('Who\'s images to retrieve? ')
resp_id = requests.get('https://api.instagram.com/v1/users/search?q=%s&access_token=INSERTACCESSTOKENHERE' % username).json()
id = resp_id['data'][0]['id']
print('Retrieving images from ' + resp_id['data'][0]['full_name'].encode('utf-8').decode('ascii', 'ignore') + ' ' + '(%s)' % username + '.')

urllist = []

def retrieve(link):

	resp_links = requests.get(link).json()

	for i in resp_links['data']:
		urllist.append(i['images']['standard_resolution']['url'])

	if resp_links['pagination']:
		next_page = input('There are more images. Currently at %s images. Get more? y/n: ' % len(urllist))
	
	if resp_links['pagination'] and next_page == 'y':
		retrieve(resp_links['pagination']['next_url'])
			
	else:
		verify = input('About to download %s images. Proceed?\ny/n: ' % len(urllist))
		
		if verify == 'y':
			
			dirpath = os.path.join('./', username)
			try:
				os.makedirs(dirpath)
			except OSError as e:
				if e.errno != errno.EEXIST:
					raise

			for url in range(len(urllist)):
				urllib.request.urlretrieve(urllist[url], str(dirpath) + '/' + str(url) + '.jpg')
				print((str(url) + ' of ' + str(len(urllist)) + 'retrieved...'), end='\r')
				
retrieve('https://api.instagram.com/v1/users/%s/media/recent/?access_token=6727674825.ba4c844.f0bba8641ea8460c889dea0a08984740&count=9999999' % id)





