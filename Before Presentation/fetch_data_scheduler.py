def fetch_data():
    # remove the current file
    print("fetch start")
    import os
    import shutil
    '''if os.path.exists(".\ISCXURL2016.zip"):
        os.remove(".\ISCXURL2016.zip")
    if os.path.exists(".\ISCXURL2016"):
        shutil.rmtree(".\ISCXURL2016")
    #  download a file from the web using requests
    '''
    import requests
    url = 'http://205.174.165.80/CICDataset/ISCX-URL-2016/Dataset/ISCXURL2016.zip'
    r = requests.get( url , allow_redirects=True ) 
    open('ISCXURL2016.zip','wb').write(r.content)
    from zipfile import ZipFile
    with ZipFile('ISCXURL2016.zip', 'r') as zipObj:
        # Extract all the contents of zip file in different directory
        zipObj.extractall('ISCXURL2016')
        # print('File is unzipped in dataset folder')
    print("Data_fetched")

from apscheduler.schedulers.blocking import BlockingScheduler
scheduler = BlockingScheduler()
# scheduler.add_job(fetch_data, 'interval', days=1)
scheduler.add_job(fetch_data, 'interval', seconds=10)
scheduler.start()


'''
def test_fun():
    print("hi") 

test = BlockingScheduler()
test.add_job(test_fun, 'interval', seconds=2)
test.start()
'''