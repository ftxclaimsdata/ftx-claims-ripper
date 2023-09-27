import csv
import os
import requests
import time

headers = {
    'authority': 'restructuring.ra.kroll.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'dnt': '1',
    'origin': 'https://restructuring.ra.kroll.com',
    'pragma': 'no-cache',
    'referer': 'https://restructuring.ra.kroll.com/FTX/Home-ClaimInfo',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

page = 1
pages = 1

os.makedirs("pages", exist_ok=True)
while page <= pages:
    print(f"Ripping page {page} of {pages}...")
    data = {
        'ClaimNumber': '',
        'ScheduleNumber': '',
        'CreditorName': '',
        'ConfirmationID': '',
        'TotalCurrentClaimAmount': 'Select an Option|Select an Option|',
        'Dates': '|',
        'ScopeValue': 'Claims & Schedules',
        'QuickSearch': '',
        'Deptors': '0ê900807ê900817ê900818ê900819ê900820ê900821ê900822ê900823ê900824ê900825ê900826ê900827ê900828ê900829ê900830ê900831ê900832ê900833ê900834ê900835ê900836ê900837ê900838ê900839ê900840ê900841ê900842ê900843ê900844ê900845ê900846ê900847ê900848ê900849ê900850ê900851ê900852ê900853ê900854ê900855ê900856ê900857ê900858ê900859ê900860ê900861ê900862ê900863ê900864ê900865ê900866ê900867ê900868ê900869ê900870ê900871ê900872ê900873ê900874ê900875ê900876ê900877ê900878ê900879ê900880ê900881ê900882ê900883ê900884ê900885ê900886ê900888ê900889ê900890ê900891ê900892ê900893ê900894ê900895ê900896ê900897ê900898ê900899ê900900ê900901ê900902ê900903ê900904ê900905ê900906ê900907ê900908ê900909ê900910ê900911ê900912ê900913ê900914ê900915ê900916ê900917ê900918ê',
        'fl': '0',
        '_search': 'false',
        'nd': '1695852173549',
        'rows': '20',
        'page': str(page),
        'sidx': 'CreditorName',
        'sord': 'asc',
    }

    response = requests.post('https://restructuring.ra.kroll.com/FTX/Home-LoadClaimData', headers=headers, data=data).json()
    page_content = response.get('rows', {})
    pages = response.get('total', 1) 
    with open(f'pages/page_{page}.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=page_content[0].keys())
        writer.writeheader()
        for row in page_content:
            writer.writerow(row)

    page += 1
    print(f"Ripped page {page} of {pages}. Waiting 50ms for rate limit...")
    time.sleep(0.05)  # dunno if they actually rate limit
