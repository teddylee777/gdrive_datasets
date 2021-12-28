from google_drive_downloader import GoogleDriveDownloader as gdd
import urllib.request
import zipfile
import os


def load_from_google_drive(file_id, folder='data/'):
    gdd.download_file_from_google_drive(file_id=file_id, dest_path='./dataset.zip')

    local_zip = 'dataset.zip'
    zip_ref = zipfile.ZipFile(local_zip, 'r')
    zip_ref.extractall(folder)
    zip_ref.close()

    for f in os.listdir(folder):
        print(os.path.join(folder, f))