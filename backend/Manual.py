import scrapy
import re

class Manual(scrapy.Spider):
    name = 'manual'
    start_urls =['https://gadgets360.com/mobiles/best-phones']

    def parse(self, response) :
        for products in response.css('div.pdimg'):
            yield response.follow(products.css('a.pdthmb').attrib['href'],callback=self.prasecat)

    def prasecat(self,response) :
        products = response.css('div._gry-bg._spctbl._ovfhide')
        n=response.css('div._thd._shins')
        name=n.css('h1::text').get()
        im=response.css('div._pdmimg.__arModalBtn._flx')
        image=im.css('img').attrib['src']
        res={}
        rating=[]
        rating_res={}
        rate=response.css('ul._flx._rwrtng._ovfhide')
        classes=rate.css('._sp').xpath('@class').extract()
        aatrib=rate.css('span::text').getall()
        #to extract rating from phone
        for c in classes:
            sa=re.findall('[0-9]+', c)
            rating.append(int(sa[0]))
        for i in range(len(rating)) : 
            rating_res[aatrib[i].replace(" ","_")]=rating[i]
            
        # to extract specs from phone
        specs=[]
        tr=products.css('tr')
        CLEANR = re.compile('<.*?>')
        for i in range(len(tr)):
            li=tr[i].extract().split("</td>")
            cleantext = re.sub(CLEANR, '', li[0].strip())
            cleantext1 = re.sub(CLEANR, '', li[1].strip())
            if "Price in India" in cleantext:
                price=cleantext1.replace("\u20b9", "")
                price= int(price.replace(",", ""))
            elif (cleantext1.isnumeric()) or (cleantext1.isdecimal()) :
                res[cleantext.strip().replace(" ","_")]=int(cleantext1)
            else :    
                res[cleantext.strip().replace(" ","_")]=cleantext1    
            
            # for i in range(0,len(p.css('td::text').getall())):
            #     if i % 2 ==0:
            #         res[p.css('td::text')[i].extract()]=p.css('td::text')[i+1].extract()
                
        
        
        yield {
            'name' : name,
            'price': price,
            'image':image,
            'spec': res,
            'rating': rating_res

        }
            #   'name'  : title,
            #   'price' : price
                
            

