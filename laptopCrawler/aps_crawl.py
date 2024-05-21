import os
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

def run_scrapy():
    start_time = datetime.now()
    current_time = start_time.strftime("%Y-%m-%d_%H-%M-%S")
    spiders = {
        "laptopworld_gaming": f"laptopworld_gaming_{current_time}.json",
        "laptopworld_vp": f"laptopworld_vp_{current_time}.json",
        "hacom_gm": f"hacom_gm_{current_time}.json",
        "hacom_vp": f"hacom_vp_{current_time}.json",
        "phucanh_vp": f"phucanh_vp_{current_time}.json",
    }
    
    for spider, output_file in spiders.items():
        os.system(f'scrapy crawl {spider} -o ../database/{output_file}')
        # Also store the status
        status_file = f'../database/crawl_status_{spider}.txt'
        if os.path.exists(status_file):
            with open(status_file, 'r') as f:
                status = f.read()
            with open(f'../database/crawl_status_log.txt', 'a') as log:
                log.write(status)
    
    end_time = datetime.now()
    duration = end_time - start_time
    with open(f'../database/crawl_status_log.txt', 'a') as log:
        log.write(f"Crawl started at: {start_time}\n")
        log.write(f"Crawl ended at: {end_time}\n")
        log.write(f"Total duration: {duration}\n")
        log.write(f"Crawl success")

scheduler = BlockingScheduler()
scheduler.add_job(run_scrapy, 'interval', months=1)

try:
    print("Scheduler started...")
    run_scrapy()
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    pass
