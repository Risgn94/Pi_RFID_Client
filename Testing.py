import requests
r = requests.post('http://localhost:4433/users/signup/1', data={
    'EMAIL': 'andreas@adnudging.com',
    'NAME': "Andreas Randloec",
    'BUDGET': "2000",
    "DESC": "Something interesting"
})

print r.text