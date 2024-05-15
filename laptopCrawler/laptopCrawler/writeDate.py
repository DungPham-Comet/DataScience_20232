import os
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

# Định nghĩa hàm để chạy lệnh Scrapy và tạo file JSON mới
def run_scrapy():
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"test_{current_time}.json"
    print(f"Running Scrapy at {current_time}, output file: {output_file}")
    os.system(f'scrapy crawl laptopworld_gaming -o DataCrawl/{output_file}')

# Tạo một instance của BlockingScheduler
scheduler = BlockingScheduler()

# Lập lịch để chạy hàm run_scrapy mỗi 3 phút
scheduler.add_job(run_scrapy, 'interval', minutes=3)

# Bắt đầu lịch trình
try:
    print("Scheduler started...")
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    pass
# import os
# from apscheduler.schedulers.blocking import BlockingScheduler
#
# # Định nghĩa hàm để chạy lệnh Scrapy và tạo file JSON mới
# output_file = "test.json"
# def run_scrapy():
#     # Xóa file JSON hiện tại nếu tồn tại
#     if os.path.exists(output_file):
#         os.remove(output_file)
#     # Chạy lệnh Scrapy và ghi dữ liệu vào file JSON
#     os.system(f'scrapy crawl laptopworld_gaming -o {output_file}')
#
# # Tạo một instance của BlockingScheduler
# scheduler = BlockingScheduler()
#
# # Lập lịch để chạy hàm run_scrapy mỗi 4 phút
# scheduler.add_job(run_scrapy, 'interval', minutes=3)
#
# # Bắt đầu lịch trình
# try:
#     print("Scheduler started...")
#     scheduler.start()
# except (KeyboardInterrupt, SystemExit):
#     pass
