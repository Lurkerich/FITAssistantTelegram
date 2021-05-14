import os
from datetime import datetime, timezone

from dateutil.relativedelta import relativedelta
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("FIRASS")
URL = 'https://public-fit-assistant.gnkdev.space/Assistant/{0}/{1}'

class URLhandler:
    @staticmethod
    def subjects():
        return URL.format('Subjects', TOKEN)

    @staticmethod
    def teachers():
        return URL.format('Teachers', TOKEN)


class URLSchedule:
    @staticmethod
    def schedule():
        url = 'https://rasp.omgtu.ru/api/schedule/group/375?start={0}&finish={1}'
        d1 = datetime.now(timezone.utc) + relativedelta(hours=+6)
        d1 = d1.strftime("%Y.%m.%d")
        return url.format(d1, d1)
