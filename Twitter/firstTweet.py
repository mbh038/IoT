from twython import Twython

C_KEY="Xh0uiwG5ao1r141p2uALJvTcU"
C_SECRET="fWEGJfCQDnW77m25IX6HJx5cfwoYkueyOk7lBx5WqvUvUMmzG5"
A_TOKEN="846305455332900864-zy9DsYB9NNOIJgIciUVwIJzixbiCX4K"
A_SECRET="TqqLZfTRGo38SBeXYAS3UyqPxFjkcOrr9K7qNYP1urFC5"

api=Twython(C_KEY,C_SECRET,A_TOKEN,A_SECRET)

api.update_status(status='Hunt_IoT')
