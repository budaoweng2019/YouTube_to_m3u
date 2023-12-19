#! /usr/bin/python3

banner = r'''
#EXTINF:-1 ,CCTV-1
http://[2409:8087:2001:20:2800:0:df6e:eb07]/wh7f454c46tw3252572940_-481357165/ott.mobaibox.com/PLTV/3/224/3221227467/index.m3u8?icpid=3&RTS=1668593752&from=40&ocs=2_2409:8087:2001:20:2800:0:df6e:eb0a_80&popid=40&hms_devid=2036&prioritypopid=40&vqe=3

#EXTINF:-1 ,CCTV-2
http://[2409:8087:2001:20:2800:0:df6e:eb12]/wh7f454c46tw3589111099_-1793408755/ott.mobaibox.com/PLTV/3/224/3221227543/index.m3u8?icpid=3&RTS=1668594088&from=40&popid=40&hms_devid=2112&prioritypopid=40&vqe=3

#EXTINF:-1 ,CCTV-3
http://[2409:8087:2001:20:2800:0:df6e:eb18]/wh7f454c46tw3746132328_-1754088424/ott.mobaibox.com/PLTV/3/224/3221228126/index.m3u8?icpid=3&RTS=1668594245&from=40&popid=40&hms_devid=2113&prioritypopid=40&vqe=3

#EXTINF:-1 ,CCTV-4
http://[2409:8087:2001:20:2800:0:df6e:eb12]/wh7f454c46tw3772680253_-1555628407/ott.mobaibox.com/PLTV/3/224/3221227549/index.m3u8?icpid=3&RTS=1668594272&from=40&popid=40&hms_devid=2112&prioritypopid=40&vqe=3

#EXTINF:-1 ,CCTV-5
http://[2409:8087:2001:20:2800:0:df6e:eb15]/wh7f454c46tw3847208563_882248521/ott.mobaibox.com/PLTV/3/224/3221228179/index.m3u8?icpid=3&RTS=1668594346&from=40&popid=40&hms_devid=2115&prioritypopid=40&vqe=3

#EXTINF:-1 ,CCTV-6
http://[2409:8087:2001:20:2800:0:df6e:eb13]/wh7f454c46tw3940641123_459833286/ott.mobaibox.com/PLTV/3/224/3221227505/index.m3u8?icpid=3&RTS=1668594440&from=40&popid=40&hms_devid=2112&prioritypopid=40&vqe=3

#EXTINF:-1 ,CCTV-7
http://[2409:8087:2001:20:2800:0:df6e:eb26]/wh7f454c46tw3984282630_1427246842/ott.mobaibox.com/PLTV/3/224/3221228283/index.m3u8?icpid=3&RTS=1668594483&from=40&popid=40&hms_devid=2293&prioritypopid=40&vqe=3

#EXTINF:-1 ,CCTV-8
http://[2409:8087:2001:20:2800:0:df6e:eb12]/wh7f454c46tw4086984004_1136880123/ott.mobaibox.com/PLTV/3/224/3221227473/index.m3u8?icpid=3&RTS=1668594586&from=40&popid=40&hms_devid=2112&prioritypopid=40&vqe=3

#EXTINF:-1 ,CCTV-9
http://[2409:8087:2001:20:2800:0:df6e:eb21]/wh7f454c46tw4254168827_1850088835/ott.mobaibox.com/PLTV/3/224/3221228303/index.m3u8?icpid=3&RTS=1668594753&from=40&popid=40&hms_devid=2290&prioritypopid=40&vqe=3

#EXTINF:-1 ,CCTV-10
http://[2409:8087:2001:20:2800:0:df6e:eb21]/wh7f454c46tw30319478_-185824076/ott.mobaibox.com/PLTV/3/224/3221228286/index.m3u8?icpid=3&RTS=1668594824&from=40&popid=40&hms_devid=2290&prioritypopid=40&vqe=3

#EXTINF:-1 ,CCTV-11
http://[2409:8087:2001:20:2800:0:df6e:eb23]/wh7f454c46tw105619488_1866436632/ott.mobaibox.com/PLTV/3/224/3221228289/index.m3u8?icpid=3&RTS=1668594900&from=40&popid=40&hms_devid=2291&prioritypopid=40&vqe=3

#EXTINF:-1 ,CCTV-12
http://[2409:8087:2001:20:2800:0:df6e:eb23]/wh7f454c46tw185877003_-533945400/ott.mobaibox.com/PLTV/3/224/3221228401/index.m3u8?icpid=3&RTS=1668594980&from=40&popid=40&hms_devid=2291&prioritypopid=40&vqe=3

#EXTINF:-1 ,CCTV-13
http://[2409:8087:2001:20:2800:0:df6e:eb16]/wh7f454c46tw259647455_-1559913959/ott.mobaibox.com/PLTV/3/224/3221228224/index.m3u8?icpid=3&RTS=1668595054&from=40&popid=40&hms_devid=2114&prioritypopid=40&vqe=3

#EXTINF:-1 ,CCTV-14
http://[2409:8087:2001:20:2800:0:df6e:eb22]/wh7f454c46tw340147088_1594094424/ott.mobaibox.com/PLTV/3/224/3221228292/index.m3u8?icpid=3&RTS=1668595134&from=40&popid=40&hms_devid=2291&prioritypopid=40&vqe=3

#EXTINF:-1 ,CCTV-15
http://[2409:8087:2001:20:2800:0:df6e:eb22]/wh7f454c46tw434828587_188325560/ott.mobaibox.com/PLTV/3/224/3221228404/index.m3u8?icpid=3&RTS=1668595229&from=40&popid=40&hms_devid=2291&prioritypopid=40&vqe=3

#EXTINF:-1 ,CCTV-16
http://[2409:8087:2001:20:2800:0:df6e:eb0b]/wh7f454c46tw456909575_2098882473/ott.mobaibox.com/PLTV/3/224/3221228144/index.m3u8?icpid=3&RTS=1668595251&from=40&popid=40&hms_devid=2038&prioritypopid=40&vqe=3

#EXTINF:-1 ,CCTV-17
http://[2409:8087:2001:20:2800:0:df6e:eb23]/wh7f454c46tw483903016_-67353299/ott.mobaibox.com/PLTV/3/224/3221228407/index.m3u8?icpid=3&RTS=1668595278&from=40&popid=40&hms_devid=2291&prioritypopid=40&vqe=3
'''

import requests
import os
import sys

windows = False
if 'win' in sys.platform:
    windows = True

def grab(url):
    response = requests.get(url, timeout=15).text
    if '.m3u8' not in response:
        #response = requests.get(url).text
        if '.m3u8' not in response:
            if windows:
                print('https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u')
                return
            #os.system(f'wget {url} -O temp.txt')
            os.system(f'curl "{url}" > temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
                print('https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u')
                return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    print(f"{link[start : end]}")

print('#EXTM3U')
print('#EXT-X-VERSION:3')
print('#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000')
print(banner)
#s = requests.Session()
with open('../youtube_channel_info.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
            print(f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}')
        else:
            grab(line)
            
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
