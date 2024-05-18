import os
import re
import shutil
from datetime import datetime

# Định nghĩa đường dẫn đến thư mục DataCrawl

current_file_path = os.path.abspath(__file__)
data_crawl_dir = os.path.dirname(current_file_path)

files = os.listdir(data_crawl_dir)

def get_lastest_file(files, pattern):
    latest_file = None
    latest_time = None

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

    return latest_file


hacom_gm_pattern = r"hacom_gm_(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}).json"
hacom_vp_pattern = r"hacom_vp_(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}).json"
laptopworld_gaming_pattern = r"laptopworld_gaming_(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}).json"
laptopworld_vp_pattern = r"laptopworld_vp_(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}).json"
phucanh_vp_pattern = r"phucanh_vp_(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}).json"

hacom_gm_file = get_lastest_file(files, hacom_gm_pattern)
hacom_vp_file = get_lastest_file(files, hacom_vp_pattern)
laptopworld_gaming_file = get_lastest_file(files, laptopworld_gaming_pattern)
laptopworld_vp_file = get_lastest_file(files, laptopworld_vp_pattern)
phucanh_vp_file = get_lastest_file(files, phucanh_vp_pattern)

latest_files = {
    'hacom_gm': hacom_gm_file,
    'hacom_vp': hacom_vp_file,
    'laptopworld_gaming': laptopworld_gaming_file,
    'laptopworld_vp': laptopworld_vp_file,
    'phucanh_vp': phucanh_vp_file
}

for key in latest_files:
    # move lastest files to latest_files folder
    latest_file_path = os.path.join(data_crawl_dir, latest_files[key])
    latest_files_dir = os.path.join(data_crawl_dir, 'latest_files')
    if not os.path.exists(latest_files_dir):
        os.makedirs(latest_files_dir)
    new_file_path = os.path.join(latest_files_dir, f'{key}.json')
    if os.path.exists(new_file_path):
        os.remove(new_file_path)
    shutil.copy(latest_file_path, new_file_path)
    print(f"Đã sao chép {latest_files[key]} thành {key}.json")


