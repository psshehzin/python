import requests
parameters={
    "amount": 10,
    "type": "boolean"

}
questions=requests.get(url="https://opentdb.com/api.php",params=parameters)
questions.raise_for_status()
questindict=questions.json()
question_data=questindict["results"]

