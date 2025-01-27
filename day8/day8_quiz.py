from day8.MongoDBQuizDay8 import client
from datetime import datetime

db = client['day8_quiz_db']
books = db["books"]
movies = db["movies"]
user_actions = db["user_actions"]


books_col = books.find()


def show_books():
    for book in books.find():
        print(book)


# 문제 1번
def quiz_1(genre):
    doc = {"genre":genre}
    for data in books.find(doc):
        print(data)


# 문제 2번 // 감독별 평균 영화 평점 계산
def quiz_2():
    doc = [
        {
            '$group':{
                '_id': '$director',
                'avg_rating':{'$avg':'$rating'}
            }
        },
        {
            '$sort':{'avg_rating': -1}
        }
    ]

    for data in movies.aggregate(doc):
        print(data)

# 문제 3번 // 특정 사용자의 최근 행동 조회
# 특정 저자의 최근 년도 순으로 조회 해봤습니다.
def quiz_3():
    doc = {
        'author': {"$regex": "한강", "$options": "i"}
    }
    datas = books.find(doc).sort({'year': -1}).limit(5)
    for data in datas:
        print(data)


# 문제 4번
# 출한 연도별 책의 수 계산
def quiz_4():
    doc = [
        {
            '$group':{
                '_id':'$year',
                'count': {'$sum': 1}
            }
        },
        {
            '$sort': {'count': -1}
        }
    ]

    datas = books.aggregate(doc)
    for data in datas:
        print(data)

# 문제 5
# 특정 사용자의 행동 유형 업데이트
def quiz_5():
    # 이런식으로 한번에 넣을수가 없구만..
    # doc = [
    #     {
    #         'user_id':1,
    #         'action': 'view',
    #         'timestamp': {'$lt': datetime(2023, 4, 13)}
    #     },
    #     {
    #         '$set': {
    #             'action': 'seen'
    #         }
    #     }
    # ]

    filter_doc = {
        'user_id': 1,
        'action': 'view',
        'timestamp': {'$lt': datetime(2023, 4, 13)}
    }
    update = {
        '$set': {
            'action': 'seen'
        }
    }
    print("변경전")
    for data in user_actions.find():
        print(data)
    # user_actions.update_many(doc)
    user_actions.update_many(filter_doc, update)
    print("변경후")
    for data in user_actions.find():
        print(data)


# print('*'*10,"1번",'*'*10)
# quiz_1('소설')
# print('*'*10,"2번",'*'*10)
# quiz_1('fantasy')
# quiz_2()
# quiz_3()
# quiz_4()
# quiz_5()
