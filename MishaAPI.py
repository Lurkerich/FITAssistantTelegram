import os
import time
from datetime import time, datetime, timezone

from dateutil.relativedelta import relativedelta
from dotenv import load_dotenv

load_dotenv()


# https://rasp.omgtu.ru/api/schedule/group/375?start=2021.05.10&finish=2021.05.16
class URLhandler:
    def __init__(self):
        self.token = os.getenv("FIRASS")
        self.url = 'https://public-fit-assistant.gnkdev.space/Assistant/{0}/{1}'

    def subjects(self):
        return self.url.format('Subjects', self.token)

    def teachers(self):
        return self.url.format('Teachers', self.token)

    def schedule(self):
        return self.url.format('Schedule', 'Today')

    def queues(self):
        return self.url.format('Queues', self.token)


class URLSchedule:

    def __init__(self):
        self.d1 = datetime.now(timezone.utc).strftime("%Y.%m.%d")
        self.urls = 'https://rasp.omgtu.ru/api/schedule/group/375?start={0}&finish={1}'

    def schedule(self):
        d1 = datetime.now(timezone.utc).strftime("%Y.%m.%d")
        d2 = (datetime.now(timezone.utc)) + relativedelta(days=+6)
        d2 = d2.strftime("%Y.%m.%d")
        return self.urls.format(d1, d2)

    def date(self):
        return self.d1

