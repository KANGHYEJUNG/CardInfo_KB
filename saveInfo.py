import requests
import pandas as pd
from bs4 import BeautifulSoup


# KB 국민은행 체크카드 전체 링크 목록
# 순서대로 // 청춘대로 싱글 레터링 체크카드(긁으면), Liiv M 체크카드, 청춘대로 싱글 레터링 체크카드(잘사는),
# ONE 체크카드, 노리 체크카드, LG U+ 체크카드, 청춘대로 싱글 체크카드, 민 체크카드, 나라사랑 체크카드)
urlList = ['https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01790&categoryCode=L0086&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01772&categoryCode=L0087&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01788&categoryCode=L0086&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01946&categoryCode=L0087&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01664&categoryCode=L0086&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01990&categoryCode=L0087&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01988&categoryCode=L0086&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=01560&categoryCode=L0087&sGroupCode=2',
           'https://card.kbcard.com/CXPRICAC0076.cms?mainCC=a&cooperationcode=04120&categoryCode=L0086&sGroupCode=2']


# 모든 카드의 이름과 혜택을 정리해 놓은 리스트
results = []

for link in urlList:
    req = requests.get(link)
    raw = req.text
    html = BeautifulSoup(raw, 'html.parser')

    # 카드명
    cardname = html.select('h1.tit')
    print('<카드 이름> ' + cardname[0].text)

    # 카드 혜택
    benefits = html.select('span.txt')
    print(benefits[0].text)

    # content = 해당 카드의 이름과 혜택을 담는 리스트
    # benefitList = 해당 카드의 혜택을 담는 리스트
    content = [cardname[0].text]
    benefitList = []

    # 카드 혜택  나열
    print('<카드 혜택>')
    for benefit in benefits:
        print(benefit.text)
        benefitList.append(benefit.text)

    # 카드 혜택 모두 리스트화해서 content에 저장
    content.append(benefitList)
    print(content)

    # 해당 카드의 이름과 모든 혜택이 정리된 리스트인 content를 results에 추가
    results.append(content)
    print('------------------------------------------------------')

data = pd.DataFrame(results)
data.to_csv('크롤링결과.csv')








