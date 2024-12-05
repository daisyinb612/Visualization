import requests
import re
import file
import json

url = f'https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid=26475105367&date=2024-10-27'

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'Cookie':"PVID=1; buvid_fp=d05271b27a3d06c398f34ec22183e087; buvid4=8C815EC0-56CA-8C3B-A251-A6A2A45848FF82694-022030410-vgAjGt65oDNS0XWeAJsraA%3D%3D; buvid3=AF50FA55-DE8F-B320-CEE8-9D2B1C8F540683952infoc; b_nut=1729153283; _uuid=FEC96CF9-EC9F-61064-5C32-E2CEA16441FD85062infoc; CURRENT_FNVAL=4048; rpdid=|(J~k))m~J||0J'u~kmulJk)Y; header_theme_version=CLOSE; enable_web_push=DISABLE; home_feed_column=5; browser_resolution=1408-198; is-2022-channel=1; CURRENT_BLACKGAP=0; SESSDATA=42a08722%2C1745411950%2C75ad2%2Aa1CjDffS7_tFOKph4yFf2B6RZn7KJWMZ3vko28UYzmyqpqFRYpviJttY_2eaegm5jv-f0SVjA2MW16WGppVXQ1U3g5djZHNzVfVThIZXZibS04c0cyNlFXWVd4RGIwZUhNWk0tTHpmWHpzcUF3OXlKbllaQWN1WkFNVWcxRmxtNXNrNUVFVXZ0NHZBIIEC; bili_jct=525b098733cc6a2d8984be6912ecab12; DedeUserID=33047317; DedeUserID__ckMd5=85797e9cc47b1ae3; b_lsid=1910752F10_192C3AFFFB5; sid=dsycox8m; bp_t_offset_33047317=992230062050770944"
}

response = requests.get(url=url,headers=headers)
response.encoding = 'utf-8'  #进行转码防止乱码
danmu_list = re.findall('[\u4e00-\u9fa5]+',response.text)   #正则表达式只匹配中文
danmu_str = json.dumps(danmu_list, ensure_ascii=False, indent=4)
danmu_dict = json.loads(danmu_str)

file.func_write_to_json(
   json_file_name='./danmu.json',
   json_dict=danmu_dict,
)
