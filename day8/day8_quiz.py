from day8.MongoDBQuizDay8 import client

db = client['day8_quiz_db']
books = db["books"]
movies = db["movies"]
user_actions = db["suer_actions"]


books_col = books.find()

# 문제 1
for book in books.find():
    print(books_col.collection)


# 쉬는날 전부다 풀어서 다시 올리겠습니다!!!!!!
# 챌린지에는 아직 제출 안했음!!! github 에만 올렸습니다.
