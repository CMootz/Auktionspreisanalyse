from urllib.request import urlopen
import json
import requests

search_term = "8700"
url = ('http://svcs.ebay.com/services/search/FindingService/v1\
?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.1\
&SECURITY-APPNAME=ABCDE12f3-gh45-67i8-9012-jk345lm6789\
&RESPONSE-DATA-FORMAT=JSON\
&REST-PAYLOAD=true\
&GLOBAL-ID=EBAY-DE\
&paginationInput.entriesPerPage=5\
&paginationInput.pageNumber=1\
&keywords=' + search_term +'\
&itemFilter(0).name=ListingType\
&itemFilter(0).value(0)=FixedPrice')

api_result = requests.get(url)
parseddoc = api_result.json()

