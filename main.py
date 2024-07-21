import requests
from datetime import datetime

date = datetime.now()
formated_date = date.strftime("%d/%m/%Y")

time = date.time()
formated_time = time.strftime("            %H:%M:%S")

nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
app_id = "7fc42193"
api_key = "46b53266661703dcab7da7e51f2c56a1"

nutri_header = {
    "x-app-id": app_id,
    "x-app-key": api_key,
}

ask_details = {
    "query": input("Enter what exercise you did today: "),
}
nutri_response = requests.post(url=nutri_endpoint, json=ask_details, headers=nutri_header)
data = nutri_response.json()['exercises']

exercise_name = data[0]['user_input'].title()
exercise_time = data[0]['duration_min']
exercise_calories = data[0]['nf_calories']

# shetty programs
sheety_header = {
    "Authorization": "Bearer dfaefafec"

}
sheety = "https://api.sheety.co/9329baf914dbbb5e8af0a1222ac22115/copyOfMyWorkouts/workouts"

body = {
    "workout": {
        "date": formated_date,
        "time": formated_time,
        "exercise": exercise_name,
        "duration": exercise_time,
        "calories": exercise_calories,
    }
}

sheet_response = requests.post(url=sheety, json=body,headers=sheety_header)
print(sheet_response.text)
