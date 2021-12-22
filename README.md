# dataCrawling

4학년 2학기 데이터크롤링 수업 자료

<br/>

## 📄Examples

<br/>

### 🔍nvCrawler_std.py

<br/>

네이버 검색 > 뉴스 api
https://developers.naver.com/docs/serviceapi/search/news/news.md#%EB%89%B4%EC%8A%A4

<br/>

### ✈openapi_tour_std.py

<br/>

공공데이터 > 한국문화관광연구원_출입국관광통계서비스 api
https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15000297

<br/>

### 🛬openapi_TourPointVisitor.py

<br/>

공공데이터 > 한국문화관광연구원_관광자원통계서비스 api
https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15000366

<br/>

### ☕ hollysCrawler.py

<br/>

할리스커피 매장 정보 크롤링

updated at 2021.9.30

<br/>

### 🍗Chicken_cheogajip.py

<br/>

처갓집양념치킨 매장 정보 크롤링

updated at 2021.10.07

<br/>

### 🍗Chicken_pericana.py

<br/>

페리카나 매장 정보 크롤링

updated at 2021.10.07

<br/>

## 🏍Midterm Project

<br/>

**프로젝트 : 배달 앱의 등장에 따른 도로교통 사고 추이 분석**

<br/>

### 🧐분석 배경

<br/>

배달앱의 등장과 배달시장의 성장으로 배달업에 대한 관심도가 높아졌다. 

그러나 심각한 배달오토바이 사고가 자주 보도될 뿐만 아니라 도로에서 오토바이의 신호위반은 흔치않게 볼 수 있다.

문제점과 그 원인은 무엇인지 데이터를 통해 분석해보고 해결방안을 찾아보자.

<br/>

### 🧭목표

<br/>

1. 공공데이터 open-api (https://www.data.go.kr/) 이용하기
2. 도로교통 사고 데이터를 통해 배달 앱의 등장 및 변화와 이륜차의 도로교통 사고 데이터의 추이를 함께 비교 분석하여 문제점을 찾기 
3. 분석을 통해 해결방안을 모색하기

<br/>

### 🛠이용 데이터

<br/>

[도로교통공단_사망교통사고정보서비스](https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15059126)

<br/>

**[발표자료 보기](./Midterm/midtermProjectPT.pdf)**

<br/>

## 📰Final Project



**프로젝트 : 키워드 분석을 통한 주요 언론사별 성향 파악**

<br/>

### 🧐분석 배경

<br/>

세간에서 얘기하는 보수 언론들은 진보진영에 대한 네거티브를, 진보언론들은 보수진영에 대한 네거티브들을 선거가 가까이 오면서 서로가 쏟아내고 있는 현실이다.

네거티브 속 가짜뉴스들은 지지자들에겐 마치 진실처럼 받아들여져 서로가 더욱 더 강성 지지층을 형성하게 되고 서로를 증오의 정치속으로 몰아넣게 된다.

키워드 분석을 통한 언론사별 성향을 파악해 언론사들마다의 성향에 대해 어렴풋이 추측하기보다 데이터로 증명해보고자 한다. 

그 대상으로 한국 10대 중앙 일간지 중 가장 대표적인 5곳을 선정했다.

- 조선일보
- 중앙일보
- 동아일보
- 한겨레
- 경향신문

<br/>

### 🧭목표

<br/>

1. 데이터 크롤링 하기
2. 텍스트 토큰화로 키워드 뽑아내기
3. 뉴스기사의 키워드 분석을 통해 언론사의 성향을 데이터로 증명하기

<br/>

### 📖사용 라이브러리

<br/>

- beautifulsoup 
- pandas
- matplotlib
- konlpy

<br/>

### 🛠이용 데이터

<br/>

[네이버 랭킹 뉴스](https://news.naver.com/main/ranking/popularDay.naver)

<br/>

**[발표자료 보기](./Final/finalProjectPT.pdf)**

<br/>