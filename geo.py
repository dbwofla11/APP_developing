import numpy as np 
import pandas as pd     
from urllib.request import urlopen , Request
from urllib import parse
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import json
import folium as g 

# 판다스로 엑셀 파일 열기 (주소목록 서울시 쓰레기통 주소)
data = pd.read_excel('test.xlsx', usecols=[2,3] , header=None ) # x가 경도 y가 위도 

g_map = g.Map(location=[37.333333,127.111111],zoom_start=8)

g_map.save('new.html')
