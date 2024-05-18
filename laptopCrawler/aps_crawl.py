import os
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

def run_scrapy():
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    hacom_gm = f"hacom_gm_{current_time}.json"
    hacom_vp = f"hacom_vp_{current_time}.json"
    laptopworld_gaming = f"laptopworld_gaming_{current_time}.json"
    laptopworld_vp = f"laptopworld_vp_{current_time}.json"
    phucanh_vp = f"phucanh_vp_{current_time}.json"

    os.system(f'scrapy crawl laptopworld_gaming -o ../database/{laptopworld_gaming}')
    os.system(f'scrapy crawl laptopworld_vp -o ../database/{laptopworld_vp}')
    os.system(f'scrapy crawl hacom_gm -o ../database/{hacom_gm}')
    os.system(f'scrapy crawl hacom_vp -o ../database/{hacom_vp}')
    os.system(f'scrapy crawl phucanh_vp -o ../database/{phucanh_vp}')


scheduler = BlockingScheduler()

scheduler.add_job(run_scrapy, 'interval', minutes=3)

try:
    print("Scheduler started...")
    run_scrapy()
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    pass
