import aiohttp
import asyncio
import pandas as pd

schedule_list = ['https://schedule.nylas.com/tuan-anh-nguyen-30min', 'https://schedule.nylas.com/hien-dt-30min-1',
                   'https://schedule.nylas.com/hoang-le-30min',
                   'https://schedule.nylas.com/tim-nguyen-45min', 'https://schedule.nylas.com/khang-hoang-30min',
                   'https://schedule.nylas.com/anthony-vo-45min',
                   'https://schedule.nylas.com/khoa-le-30min', 'https://schedule.nylas.com/dat-nguyen-30min',
                   'https://schedule.nylas.com/nam-ho-30min',
                   'https://schedule.nylas.com/dat-b-do-60min', 'https://schedule.nylas.com/quangta93',
                   'https://schedule.nylas.com/lukas-tuong-30min',
                   'https://schedule.nylas.com/bao-chau-45min', 'https://schedule.nylas.com/hai-ho-60min',
                   'https://schedule.nylas.com/hieu-pham-30min',
                   'https://schedule.nylas.com/nga-than-45min', 'https://schedule.nylas.com/quyen-le',
                   'https://schedule.nylas.com/thang-dao-mentor-session',
                   'https://schedule.nylas.com/scarlet-nguyen-45min', 'https://schedule.nylas.com/mark-morawski-30min',
                   'https://schedule.nylas.com/thao-nguyen',
                   'https://schedule.nylas.com/bao', 'https://schedule.nylas.com/nhung-le-30min',
                   'https://schedule.nylas.com/tuan-doan-30min',
                   'https://schedule.nylas.com/hien-le-30min-2', 'https://schedule.nylas.com/khang-nguyen-30min',
                   'https://schedule.nylas.com/khang-pham-15min-1',
                   'https://schedule.nylas.com/namnomnom', 'https://schedule.nylas.com/ryan-dao-30min',
                   'https://schedule.nylas.com/nghi-truong-30min',
                   'https://schedule.nylas.com/khoa', 'https://schedule.nylas.com/loc-bui-30min-1',
                   'https://schedule.nylas.com/phuong-belman-30min',
                   'https://schedule.nylas.com/tu-tran-30min-1', 'https://schedule.nylas.com/viet-do-15min',
                   'https://schedule.nylas.com/nga-le-30min',
                   'https://schedule.nylas.com/khanh-nguyen', 'https://schedule.nylas.com/chau-vu-30min',
                   'https://schedule.nylas.com/si-dang-60min-2',
                   'https://schedule.nylas.com/david-vu-60min', 'https://schedule.nylas.com/anh-trinh-30min']
mentor_schedule = {}
mentor_json = []

for url in schedule_list:
    mentor_general_id = url.split('/')[-1]
    mentor_schedule[url] = mentor_general_id

mentor_schedule = {k: v for k, v in mentor_schedule.items() if v}

def get_tasks(session):
    tasks = []
    for schedule,id in mentor_schedule.items():
        url = f'https://api.schedule.nylas.com/schedule/{id}/timeslots?allow_stale=true&locale=en'
        tasks.append(asyncio.create_task(session.get(url)))
    return tasks

async def get_url():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        apis = await asyncio.gather(*tasks)
        for api in apis:
            mentor_json.append(await api.json())
        #api_dataframe = pd.DataFrame(mentor_json)
        print(mentor_json[0])
        #print(api_dataframe.dtypes)

asyncio.run(get_url())
