from google_drive_downloader import GoogleDriveDownloader as gdd
import urllib.request
import zipfile
import os

# reference @ https://gldmg.tistory.com/141
# treating Hangul encoding problem
def unzip(source_file, dest_path):
    with zipfile.ZipFile(source_file, 'r') as zf:
        zipInfo = zf.infolist()
        for member in zipInfo:
            try:
                member.filename = member.filename.encode('cp437').decode('euc-kr', 'ignore')
                zf.extract(member, dest_path)
            except:
                print(source_file)
                raise Exception('unzipping error')


def load_from_google_drive(file_id, folder='data/'):
    gdd.download_file_from_google_drive(file_id=file_id, dest_path='./dataset.zip')

    local_zip = 'dataset.zip'
    unzip(local_zip, folder)

    print('========== files ============', end='\n\n')
    for f in os.listdir(folder):
        print(os.path.join(folder, f))
    print('\n=============================')

