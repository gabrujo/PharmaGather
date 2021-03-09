import urllib.request
import urllib
params = {
'username':'fati5481',
'password':'1y3n0lz9',
'to':'+12034466750',
'from':'D7SMS',
'content':'Hi',
}
urllib.request.urlopen("http://smsc.d7networks.com:1401/send?%s"
% urllib.parse.urlencode(params)).read()
