from bs4 import BeautifulSoup
import requests
# s=requests.get('https://sinoptik.com.ru/погода-москва')
# b=bs4.BeautifulSoup(s.text, "html.parser")
# p3=b.select('.temperature .p3')
# pogoda1=p3[0].getText()
# p4=b.select('.temperature .p4')
# pogoda2=p4[0].getText()
# p5=b.select('.temperature .p5')
# pogoda3=p5[0].getText()
# p6=b.select('.temperature .p6')
# pogoda4=p6[0].getText()
# print('Утром :' + pogoda1 + ' ' + pogoda2)
# print('Днём :' + pogoda3 + ' ' + pogoda4)
# p=b.select('.rSide .description')
# pogoda=p[0].getText()
# print(pogoda.strip())

surls = ['https://librasimferopol.ru/index.php?offset='+str(i)+'&s_cat=65' for i in range(2,13)]
site = 'https://librasimferopol.ru'


def make_goal_urls(arr_urls):
    url_arr = [urlreturner(i) for i in arr_urls]
    goal_urls = []
    for i in url_arr:
        for j in i:
            goal_urls.append(j)
    return goal_urls


def urlreturner(surl):
    urls=[]
    page = requests.get(surl)
    soup = BeautifulSoup(page.text, 'html.parser')
    urls_tag = soup.findAll('dt')
    atgs = [i.find('a') for i in urls_tag]
    for i in atgs:
        urls.append(site + i.get('href'))
    return urls


target = 'https://librasimferopol.ru/?84689'
def get_email(target_url):
    page = requests.get(target_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    url1 = soup.find('span','maillink')
    url2 = soup.findAll('span','let')
    email = ''
    for i in url2:
        email += i.string
    return email

url_pool = make_goal_urls(surls)
email_pool = []
 
for i in url_pool:
    email_pool.append(get_email(i))

f = open( 'emails.txt', 'w' )
for item in email_pool:
    #Если длинна больше трех (убираем пустые строки с сайтов, где не было найдено e-mail)
    if len(item) > 3:
        print(item)
        f.write("%s\n" % item)
f.close()