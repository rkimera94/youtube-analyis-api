from sql_database import Video, Session, engine

local_session = Session(bind=engine)

'''
 query all videos
 
 '''

videos = local_session.query(Video).all()

# query with limit

videos_limit = local_session.query(Video).all()[:2]

# query one object
video_by_kind = local_session.query(Video).filter(Video.kind == "DEMO")

print('by kind', video_by_kind)


for v in videos:
    print(videos)

print('Fetch')
for v in videos_limit:
    print(videos_limit)


for v in video_by_kind:
    print(video_by_kind)
