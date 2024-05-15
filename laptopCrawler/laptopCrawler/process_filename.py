import os
import re
import shutil
from datetime import datetime

# Định nghĩa đường dẫn đến thư mục DataCrawl
data_crawl_dir = os.path.join(os.path.dirname(__file__), 'DataCrawl')

# Kiểm tra xem thư mục có tồn tại hay không
if not os.path.exists(data_crawl_dir):
    print(f"Thư mục {data_crawl_dir} không tồn tại")
    exit()

# Lấy danh sách các file trong thư mục DataCrawl
files = os.listdir(data_crawl_dir)

# Định nghĩa regex để khớp với các file có định dạng tên mong muốn
pattern = r'test_(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}).json'

# Khởi tạo biến để lưu trữ file mới nhất
latest_file = None
latest_time = None

# Duyệt qua các file để tìm file mới nhất
for file in files:
    match = re.match(pattern, file)
    if match:
        # Trích xuất chuỗi thời gian từ tên file
        file_time_str = match.group(1)
        # Chuyển đổi chuỗi thời gian thành đối tượng datetime
        file_time = datetime.strptime(file_time_str, '%Y-%m-%d_%H-%M-%S')
        # Kiểm tra và cập nhật file mới nhất
        if latest_time is None or file_time > latest_time:
            latest_time = file_time
            latest_file = file

if latest_file:
    # Định nghĩa đường dẫn đến file mới nhất
    latest_file_path = os.path.join(data_crawl_dir, latest_file)
    # Định nghĩa đường dẫn đến file test.json
    new_file_path = os.path.join(data_crawl_dir, 'test.json')
    # Sao chép và đổi tên file mới nhất thành test.json
    shutil.copy(latest_file_path, new_file_path)
    print(f"Đã sao chép {latest_file} thành test.json")
else:
    print("Không tìm thấy file JSON nào có định dạng thời gian phù hợp")
