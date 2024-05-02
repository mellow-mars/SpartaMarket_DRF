# SpartaMarket_drf
---
## 목차
* ERD
* 주요기능/API 명세
* 개발기간
* 기술스택

---

## ERD
![Untitled (5)](https://github.com/mellow-mars/SpartaMarket_DRF/assets/142032967/ed6b1f91-9474-4dd2-8373-85b296a1b7ab)

---

## 주요기능/API 명세

### 상품관련 기능
* 상품등록
    * Endpoint:/api/products
    * Method:POST
![image](https://github.com/mellow-mars/spartamarket/assets/142032967/270df0c7-3e08-454e-bcff-bb2d86191c54)
* 상품목록 조회
    * Endpoint:/api/products
    * Method:GET
![image](https://github.com/mellow-mars/spartamarket/assets/142032967/ff3f0fae-fdf2-4491-8706-b33e6e99a3aa)
* 상품 수정
    * Endpoint:/api/products/<int:productId>
    * Method:PUT
![image](https://github.com/mellow-mars/spartamarket/assets/142032967/f1a70933-1668-40a1-af6a-48d7f53cc754)
* 상품 삭제
    * Endpoint:/api/products/<int:productId>
    * Method:DELETE
![image](https://github.com/mellow-mars/spartamarket/assets/142032967/6b22ed09-43f5-4f63-a729-b76a510dad0a)

## 회원가입 관련 기능

* 회원가입
    * Endpoint:/api/accounts 
    * Method:POST
![image](https://github.com/mellow-mars/spartamarket/assets/142032967/d639bf32-b2af-408a-9972-77d7ffafd7e9)
* 로그인
    * Endpoint:/api/accounts/login
    * Method:POST
![image](https://github.com/mellow-mars/spartamarket/assets/142032967/0519856c-cb8b-4a7a-842a-35f5226d29ca)
* 로그아웃
    * Endpoint:/api/accounts/logout/
    * Method:POST
![image](https://github.com/mellow-mars/SpartaMarket_DRF/assets/142032967/02ff3cc1-8a1f-4f92-af9a-23846ee70181)


* 프로필 페이지
    * Endpoint:/api/accounts/<str:username>/
    * Method:GET
![image](https://github.com/mellow-mars/spartamarket/assets/142032967/4a07fca9-e9f9-462d-a1a2-e2cefa366fc7)
* 회원 정보수정
    * Endpoint:/api/accounts/<str:username>/
    * Method:PUT
![image](https://github.com/mellow-mars/spartamarket/assets/142032967/ecb47be1-21be-4ab5-86e9-f665913a113b)

* 비밀번호 변경
    * Endpoint:/api/accounts/password/
    * Method:PUT
![image](https://github.com/mellow-mars/spartamarket/assets/142032967/7203aa1c-8278-43cc-a939-a9c45919b583)

* 회원 탈퇴 
    * Endpoint:/api/accounts/delete/
    * Method:DELETE
![image](https://github.com/mellow-mars/spartamarket/assets/142032967/5408ebe9-24ec-40c3-a3ed-251c2b275e1b)

## 개발기간
---
2024년04월26일 ~ 2024년05월02일

## 기술스택
---
<div align="center">
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/django-092E20.svg?&style=for-the-badge&logo=django&logoColor=white">
<img src="https://img.shields.io/badge/postman-FF6C37.svg?&style=for-the-badge&logo=postman&logoColor=white">
<br>
<img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">
<img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
<img src="https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=Slack&logoColor=white">
<br>
<img src="https://img.shields.io/badge/notion-000000?style=for-the-badge&logo=notion&logoColor=white">
<img src="https://img.shields.io/badge/google-sheets-34A853?style=for-the-badge&logo=google-sheets&logoColor=white">
