from threading import local
from sql_database import Video, Session, engine

local_session = Session(bind=engine)


'''dictionary 
'''

new_videos = [
    {'video_id': '56343', 'kind': '1DEMO'},
    {'video_id': '3456yhgfd', 'kind': '2DEMO'},
    {'video_id': '3432', 'kind': 'DEMO'},
    {'video_id': '4353', 'kind': '2DEMO'}
]


# add to the database (single video)
# new_video = Video(id=1, video_id='352yu493430', kind='DEMO')

# local_session.add(new_video)
# local_session.commit()

''' add list of dictionaries '''
for v in new_videos:
    new_video = Video(video_id=v['video_id'], kind=v['kind'])
    local_session.add(new_video)
    local_session.commit()

    print(f"Added {v['video_id']}")
