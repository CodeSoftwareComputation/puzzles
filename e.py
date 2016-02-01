import urllib2
import json
if __name__ == "__main__":
    contents = json.loads(urllib2.urlopen("http://www.google.com/finance/info?q=NSE:aapl").read()[3:])
    price = float(contents[0]['l_cur'])
    if price < 100:
        buy('aapl')
    if price > 100:
        sell('aapl')

