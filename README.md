##  Problem Statement

Scrape the website https://www.houseofindya.com/ for list of necklace sets under jewelry and corresponding description, price and image urls. </br>
You must use scrapy for this and create output in csv and json formats.

## Downloads and installations

Python 2 </br>
https://www.python.org/downloads/release/python-2718/

Python 3 </br>
https://www.python.org/downloads/release/python-392/

➜ pip3 install scrapy

➜ pip3 install Pillow

## Folder creation

scrapy startproject web_scraping_service

You can start your first spider with:
    
    cd web_scraping_service
    
    scrapy genspider example example.com

## Crawl the web page and create csv/json

cd web_scraping_service

<hr>

Case 1: To get data in csv format:

➜ rm -rf images 

➜ rm -rf tmp

➜ scrapy crawl necklacesetbot

<hr>
<hr>

Case 2: To get data in json format, uncomment the following block of code:

custom_settings = {
    'FEED_FORMAT': 'json',
    'FEED_URI' : 'jsonfiles/necklaceset.json'
}

➜ rm -rf images 

➜ rm -rf jsonfiles

➜ scrapy crawl necklacesetbot

## Pre-requisites

➜ pip3 --version

pip 20.2.3 from /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pip (python 3.9)

➜ python3 --version

Python 3.9.2

➜ pip3 install scrapy

## Trial runs

➜ scrapy shell
> fetch("https://www.houseofindya.com/")

```
2021-03-23 00:32:06 [scrapy.core.engine] INFO: Spider opened
2021-03-23 00:32:14 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.houseofindya.com/> (referer: None)
```

* This will open a new tab on the browser:

> view(response)
```
True
```

> print(response.text)

```
<!DOCTYPE html><html lang=en><head><meta charset=utf-8><meta name=viewport content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"><link rel=dns-prefetch href=https://img.faballey.com><link rel=preconnect href=https://static.criteo.net><link rel=preconnect href=https://www.googletagmanager.com><link rel=preconnect href=https://www.googleadservices.com><link rel=dns-prefetch href=https://static.bytedance.com><link rel=preconnect href=https://s0.ipstatp.com><link rel=preconnect href=https://www.google-analytics.com><link rel=preconnect href=https://static.faballey.com><link rel=dns-prefetch href=https://gum.criteo.com><link rel=preconnect href=https://sslwidget.criteo.com><link rel=preconnect href=https://dis.as.criteo.com><link rel=preconnect href=https://connect.facebook.net><link rel="shortcut icon" href=data:image/x-icon;base64,AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA><link href="/themes/default/css/fontawesomePro.css?v=8.1.1" rel=stylesheet><link href="https://static.faballey.com/themes/default/css/indya/mainstyle.min.css?v=6.7" rel=stylesheet><script src="https://static.faballey.com/themes/default/javascript/jquery-3.2.1.min.js?v=6.7"></script><script src="https://static.faballey.com/themes/default/javascript/mainjs.min.js?v=6.7"></script><meta name=viewport content="width=device-width"><link rel=canonical href="https://www.houseofindya.com/"><meta name=canonical content="https://www.houseofindya.com/"><meta property=twitter:card content=""><meta name=twitter:site content=@houseofindya><meta property=twitter:title content="Indian Designer Wear - Online Fashion Shopping Site for Women - Indya"><meta property=twitter:description content="Online Shopping Site for Women Fashion Wear - Buy Women Designer Wear Online in India. Shop latest collection of Indian ethnic wear tops, dresses, skirts, bottoms, tunics, kurtis &amp; kurtas online at Indya."><meta property=twitter:image content=https://img.faballey.com/images/indya/logo.png><meta property=og:title content="Indian Designer Wear - Online Fashion Shopping Site for Women - Indya"><meta property=og:type content=website><meta property=og:url content=https://www.houseofindya.com><meta property=og:image content=https://img.faballey.com/images/indya/logo.png><meta property=og:description content="Online Shopping Site for Women Fashion Wear - Buy Women Designer Wear Online in India. Shop latest collection of Indian ethnic wear tops, dresses, skirts, bottoms, tunics, kurtis &amp; kurtas online at Indya."><meta property=og:site_name content=Houseofindya><meta name=robots content="INDEX, FOLLOW"><title>Indian Designer Wear - Online Fashion Shopping Site for Women - Indya</title><meta name=description content="Online Shopping Site for Women Fashion Wear - Buy Women Designer Wear Online in India. Shop latest collection of Indian ethnic wear tops, dresses, skirts, bottoms, tunics, kurtis &amp; kurtas online at Indya."><script>try{dataLayer=[{'userIDHit':'6de21f99-fe42-4a59-8b1e-0fe2d430badb'}];}
``` 

<hr>
<hr>

Since, we need to find data w.r.t. necklace-sets under jewelry, our target URL would be:

https://www.houseofindya.com/zyra/necklace-sets/cat

> fetch("https://www.houseofindya.com/zyra/necklace-sets/cat")

```
2021-03-23 00:54:17 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.houseofindya.com/zyra/necklace-sets/cat> (referer: None)
```

> view(response)

```
True
```

> print(response.text)

```
<!DOCTYPE html><html lang=en><head><meta charset=utf-8><meta name=viewport content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"><link rel=dns-prefetch href=https://img.faballey.com><link rel=preconnect href=https://static.criteo.net><link rel=preconnect href=https://www.googletagmanager.com><link rel=preconnect href=https://www.googleadservices.com><link rel=dns-prefetch href=https://static.bytedance.com><link rel=preconnect href=https://s0.ipstatp.com><link rel=preconnect href=https://www.google-analytics.com><link rel=preconnect href=https://static.faballey.com><link rel=dns-prefetch href=https://gum.criteo.com><link rel=preconnect href=https://sslwidget.criteo.com><link rel=preconnect href=https://dis.as.criteo.com><link rel=preconnect href=https://connect.facebook.net><link rel="shortcut icon" href=data:image/x-icon;base64,AAABAAEAICAAAAEACACoCAAAFgAAACgAAAAgAAAAQAAAAAEACAAAAAAAAAQAAAAAAAAAAAAAAAEAAAABAAAAAAAAJC1tACgtwQAoKNQAKDCkAB4kQwAoMakAJyDtACcg7AAiKVgAIyxkABEUHwAoK8kAJC1rACcxigAoJ9cAJi95ACcwhAAZHTIADQ8YACgm2gAmMIUAFBclACgwowAnJtkAJS5yABUYKAAZHjMACw0VAIGBhACXl5sAJiYnAP///HCAcHCAkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAECAwQFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA><link href="/themes/default/css/fontawesomePro.css?v=8.1.1" rel=stylesheet><link href="https://static.faballey.com/themes/default/css/indya/mainstyle.min.css?v=6.7" rel=stylesheet><script src="https://static.faballey.com/themes/default/javascript/jquery-3.2.1.min.js?v=6.7"></script><script src="https://static.faballey.com/themes/default/javascript/mainjs.min.js?v=6.7"></script><meta name=viewport content="width=device-width"><link rel=canonical href=https://www.houseofindya.com/zyra/necklace-sets/cat><meta name=canonical content=https://www.houseofindya.com/zyra/necklace-sets/cat><link rel=amphtml href=https://www.houseofindya.com/amp/zyra/necklace-sets/cat><meta property=twitter:card content=""><meta name=twitter:site content=@houseofindya><meta property=twitter:title content="Necklace Sets - Buy Designer Necklace Sets for Women &amp; Girls Online in India | Indya"><meta property=twitter:description content="Necklace Sets For Women - Buy latest collection of designer Necklace Sets online for ladies and girls. Browse wide range of Short, Medium, Long &amp; Choker Necklace Sets from Indya"><meta property=twitter:image content=https://img.faballey.com/images/indya/logo.png><meta property=og:title content="Necklace Sets - Buy Designer Necklace Sets for Women &amp; Girls Online in India | Indya"><meta property=og:type content=website><meta property=og:url content=https://www.houseofindya.com/zyra/necklace-sets/cat><meta property=og:image content=https://img.faballey.com/images/indya/logo.png><meta property=og:description content="Necklace Sets For Women - Buy latest collection of designer Necklace Sets online for ladies and girls. Browse wide range of Short, Medium, Long &amp; Choker Necklace Sets from Indya"><meta property=og:site_name content=Houseofindya><meta name=robots content="INDEX, FOLLOW"><title>Necklace Sets - Buy Designer Necklace Sets for Women &amp; Girls Online in India | Indya</title><meta name=description content="Necklace Sets For Women - Buy latest collection of designer Necklace Sets online for ladies and girls. Browse wide range of Short, Medium, Long &amp; Choker Necklace Sets from Indya"><script>try{dataLayer=[{'userIDHit':'6de21f99-fe42-4a59-8b1e-0fe2d430badb'}];}
catch(e){}</script><script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-KH87V84');</script><script>!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');fbq('init','1961137310870679');fbq('track','PageView');(function removeFacebookAppendedHash(){if(!window.location.hash||window.location.hash!=='#_=_')
return;if(window.history&&window.history.replaceState)
```

Required attributes:
* description
* price
* image urls

Extraction:

response.css(".title::text").extract()

Here response.css(..) is a function that helps extract content based on css selector passed to it. 
The ‘.’ is used with the title because it’s a css . Also you need to use ::text to tell your scraper to extract only text content of the matching elements. 
This is done because scrapy directly returns the matching element along with the HTML code. 

When more than two selectors are required to identify an element, we use them both. Also since both are CSS classes we have to use “.” with their names. Let’s try it out first by extracting the first element that matches:

response.css(".score.unvoted").extract_first()

response.css(".score.unvoted::text").extract()

response.css("time::attr(title)").extract()

The .attr(attributename) is used to get the value of the specified attribute of the matching element.

response – An object that the scrapy crawler returns. This object contains all the information about the downloaded content.
response.css(..) – Matches the element with the given CSS selectors.
extract_first(..) – Extracts the “first” element that matches the given criteria.
extract(..) – Extracts “all” the elements that match the given criteria.

* description / title

> response.css("li::attr(data-name)").extract()

['White Diamond Aqua Drop Earring Necklace Set', 'Gold Kundan Aqua Stone Floral Pendant Necklace Set', 'Rose Gold Plated  Crystal Necklace Set', 'Silver Oxidized Green Stone Star Earring Necklace Set', 'Gold Green Kundan Floral Pendant Necklace Set', 'Gold Kundan Blue Bead Earring Necklace Set', 'Gold Kundan Multi Pearl String Earring Necklace Set', 'Gold Textured Contemporary Choker Necklace Set', 'Gold Kundan Red Drop Meena Earring Necklace Set', 'Gold Green Kundan Bead Drop Earring Necklace Set', 'Gold Maroon Kundan Floral Necklace Set', 'White Diamond Floral Bunch Earring Necklace Set', 'Gold Kundan Pear Dainty Drop Earrings  Necklace Set', 'Gold Kundan Tukdi Earring Necklace Set', 'Dual Gold Kundan Pearl Earring Necklace Set', 'Blue Bead Kundan Earring Necklace Set', 'Gold Kundan Green Bead String Earring Necklace Set', 'Gold Kundan Green Drop Double Orb Earring Necklace Set', 'Gold Kundan Mangtika Earring Necklace Set', 'White Blue Diamond Earring Pendant Necklace Set', 'Gold Round Kundan Pearl Earring Necklace Set', 'Gold Kundan Earring Pearl String Pendant Necklace Set', 'Gold Orb Kundan Double Pearl Earrings Necklace Set', 'Gold Red Kundan Bead Earring Necklace Set', 'Gold Kundan Blue Bead Pearl Earring Necklace Set', 'White Blue Diamond Drop String Earring Necklace Set', 'Gold Kundan Cascade Earring Necklace Set', 'Gold Kundan Dual Pearl Earring Necklace Set', 'Gold Kundan Green Drop Pearl Earring Necklace Set', 'Gold Kundan Pearl Earring Necklace Set', 'Gold Leaf Kundan Double Pearl Earrings Necklace Set', 'Dual Gold Kundan Green Bead Earring Necklace Set', 'Gold Kundan Multicolor Stone Earring Necklace Set']


* price

> response.css("li::attr(data-price)").extract()

['2450.00', '1475.00', '2450.00', '1750.00', '2100.00', '1750.00', '2000.00', '1100.00', '2250.00', '3750.00', '2250.00', '2750.00', '1750.00', '2500.00', '2000.00', '1750.00', '2000.00', '2250.00', '3500.00', '2625.00', '1750.00', '1500.00', '1750.00', '1600.00', '1750.00', '2875.00', '2250.00', '2000.00', '1750.00', '2375.00', '1750.00', '1750.00', '2000.00']

* image urls

DID NOT GIVE CORRECT OUTPUT:

> response.css("img::attr(src)").extract()
['https://static.faballey.com/images/fabblk.png?v=6.7', 'https://static.faballey.com/images/indwht.png?v=6.7', 'https://static.faballey.com/images/indya/logo.png?v=6.7', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', '/themes/default/images/indya/loader.jpg', 'https://img.faballey.com/images/membership-desktop.png', 'https://static.faballey.com/images/crncytrans.gif?v=6.7', 'https://static.faballey.com/images/crncytrans.gif?v=6.7', 'https://static.faballey.com/images/crncytrans.gif?v=6.7']


DID NOT GIVE CORRECT OUTPUT:

> response.css("img::attr(data-original)").extract()
['https://img.faballey.com/Images/Product/ZNS00013/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00062/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00064/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00021/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00063/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00041/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00048/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00070/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00054/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00018/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00058/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00032/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00046/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00007/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00056/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00050/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00049/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00038/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00002/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00011/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00035/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00008/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00051/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00003/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00042/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00031/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00039/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00052/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00047/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00044/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00045/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00055/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00053/1.jpg', 'https://static.faballey.com/images/glplay.png?v=6.7', 'https://static.faballey.com/images/appstore.png?v=6.7', 'https://static.faballey.com/images/patmentimg.png?v=6.7']


GAVE CORRECT OUTPUT:

> catgItem = response.css(".catgItem")

> itemImage = catgItem.css("img::attr(data-original)").getall()

> itemImage

['https://img.faballey.com/Images/Product/ZNS00013/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00062/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00064/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00021/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00063/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00041/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00048/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00070/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00054/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00018/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00058/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00032/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00046/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00007/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00056/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00050/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00049/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00038/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00002/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00011/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00035/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00008/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00051/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00003/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00042/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00031/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00039/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00052/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00047/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00044/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00045/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00055/1.jpg', 'https://img.faballey.com/Images/Product/ZNS00053/1.jpg']

## Reference links:

https://www.analyticsvidhya.com/blog/2017/07/web-scraping-in-python-using-scrapy/
https://docs.scrapy.org/en/latest/intro/tutorial.html
https://docs.scrapy.org/en/latest/topics/selectors.html
https://docs.scrapy.org/en/latest/topics/media-pipeline.html
http://scrapingauthority.com/scrapy-download-images/#:~:text=You%20have%20to%20enable%20ImagesPipeline,these%20fields%3A%20image_urls%20and%20images
https://stackoverflow.com/questions/23574636/scrapy-from-script-output-in-json

## Rough Work (Shall be removed later)

response.css(".catgItem.img").extract()

response.css("img::attr(data-original)").extract()

> catgItem = response.css(".catgItem").extract()
itemImage = catgItem.css("img::attr(data-original)").getall()

response.css("fal.fa-rupee-sign").extract()

> catgName = response.css(".catgName").extract()
itemActualCost = catgName.css("span").extract()

#JsonProductList > li:nth-child(24) > a > div:nth-child(3) > span:nth-child(1)

//*[@id="JsonProductList"]/li[24]/a/div[3]/span[1]


response.css("li::attr(data-price)").extract()

