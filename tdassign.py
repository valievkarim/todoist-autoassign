
import todoist
import time
from config import token

api = todoist.api.TodoistAPI(token)


while True:
    api.sync()
    ll = [item for item in api.state['items'] if item['responsible_uid'] is None and item['project_id'] == 2213617986]
    for item in ll:
        print item['content']
        item.update(responsible_uid=23288590)
    if ll:
        api.commit()
    print 'sleep..'
    time.sleep(5)
