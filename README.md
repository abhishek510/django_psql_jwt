# django_psql_jwt

Database used Postgresql
Api to search in that data for specific authenticated users 
All API calls authenticated by JWT Tokens

for localhost:
get access and refresh token:
curl -X POST -H "Content-Type: application/json" -d '{"username": "a@b.com", "password": "1234"}' http://localhost:8000/api/token/

get new access token after expiration:
curl -X POST -H "Content-Type: application/json" -d '{"refresh":"<REFRESH-TOKEN-HERE>",}' http://localhost:8000/api/token/refresh/

search by ifsc:
curl -H "Authorization: Bearer "<ACCESS-TOKEN-HERE>" " http://localhost:8000/ifscresult?ifsc=ABHY0065121

search by name and city:
curl -H "Authorization: Bearer "<ACCESS-TOKEN-HERE>" " http://127.0.0.1:8000/namecity?name=ABHYUDAYA COOPERATIVE BANK LIMITED&city=MUMBAI&limit=9&offset=1



deployed on heroku:
get access and refresh token:
curl -X POST -H "Content-Type: application/json" -d '{"username": "a@b.com", "password": "1234"}' http://appassignment.herokuapp.com/api/token/

get new access token after expiration:
curl -X POST -H "Content-Type: application/json" -d '{"refresh":"<REFRESH-TOKEN-HERE>",}' http://appassignment.herokuapp.com/api/token/refresh/

search by ifsc:
curl -H "Authorization: Bearer "<ACCESS-TOKEN-HERE>" " http://appassignment.herokuapp.com/ifscresult?ifsc=ABHY0065121

search by name and city:
curl -H "Authorization: Bearer "<ACCESS-TOKEN-HERE>" " http://appassignment.herokuapp.com/namecity?name=ABHYUDAYA COOPERATIVE BANK LIMITED&city=MUMBAI&limit=9&offset=1

