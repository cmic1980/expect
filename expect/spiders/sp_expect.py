import scrapy
import json
import tushare as ts
import expect.settings as settings
from expect.items import ExpectItem

class SpExpect(scrapy.Spider):
    name = "sp_expect"
    allowed_domains = ["gw.datayes.com"]
    start_urls = ["https://r.datayes.com/"]
    root_url = "https://gw.datayes.com/rrp_adventure/web/stockModel/v3/consensus?ticker={}"
    pass

    def __init__(self):
        pass

    def parse(self, response):
        # 获取 股票列表
        ts.set_token(settings.TUSHARE_TOKEN)
        pro = ts.pro_api()
        data = pro.stock_basic(exchange='', list_status='L', fields='symbol')
        for symbol in data["symbol"]:
            cookies = {'cloud-sso-token': settings.CLOUD_SSO_TOKEN}
            url = self.root_url.format(symbol)
            yield scrapy.Request(url, cookies=cookies, callback=self.parse_ticker, cb_kwargs={"symbol": symbol})

    def parse_ticker(self, response, symbol):
        body = response.body.decode('utf-8')
        json_object = json.loads(body)
        data = json_object["data"]

        item = ExpectItem()
        item["symbol"] = symbol
        item["type"] = type

        l = len(data)
        item["r0"] = data[l-3]
        item["r1"] = data[l-2]
        item["r2"] = data[l-1]
        
        return item