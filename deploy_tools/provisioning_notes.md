신규 사이트 프로비저닝
======================

## 필요 패키지

* nginx
* Python3
* Git
* pip
* virtualenv

Ubuntu에서 실행 방법 예:

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## Nginx 가상 호스트 설정

* nginx.template.conf 참고
* SITENAME 부분을 다음과 같이 수정 sunsuking.kro.kr

## 서비스 등록

* sunsuking.service 참고
* /etc/systemd/system에 서비스 넣, chmod 755 후등록
* SITENAME 부분을 다음과 같이 수정 sunsuking.kro.kr

## 폴더 구조:
사용자 계정의 홈 폴더가 /home/username이라고 가정