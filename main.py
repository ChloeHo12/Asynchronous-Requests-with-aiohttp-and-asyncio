import asyncio
import aiohttp

from aiohttp import ClientSession

async def get_schedule(id):
  url = f'https://api.schedule.nylas.com/schedule/{id}/timeslots?allow_stale=true&locale=en'
  async with ClientSession() as session:
    async with session.get(url) as response:
      response = await response.read()

async def main():
  mentor_schedule = {}
  mentor_json = []
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

  for url in schedule_list:
    mentor_general_id = url.split('/')[-1]
    mentor_schedule[url] = mentor_general_id

    # Remove empty keys
  mentor_schedule = {k: v for k, v in mentor_schedule.items() if v}

  # Loop through mentor_schedule, make API calls and aggregate all times into a dataframe
  #for schedule, id in mentor_schedule.items():
  mentor_json.append(url.split('/')[-1])
  await asyncio.gather(get_schedule(mentor_schedule))

asyncio.run(main())
