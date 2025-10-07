import csv
import json
from symbol import return_stmt
from urllib import response
import requests

api_url = 'https://jsonplaceholder.typicode.com/todos/'


def fetch_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        # print(data)
        return data

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        data = None

        return data



def process_and_save(data, csv_file, filtered_users=None):
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)  #

    process_and_save(data, "F:\\user.csv")
    return True

#get_user

#filter
def filter_users_by_zipcode(users_data):
    filtered_users = []
    for user in users_data:
        #postal code(zip code)
        address = user.get('address', {})
        zipcode = address.get('zipcode', '')
        if str(zipcode).startswith('0'):
            filtered_users.append({'name': user.get('name', ''), 'email': user.get('email', '')})
    return filtered_users


def main_question3() -> None:
    users_data = fetch_users_data()

    if users_data:
        filtered_users = filter_users_by_zipcode(users_data)

        #  CSV
        with open('F:\\users.csv', 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['name', 'email'])
            writer.writeheader()
            writer.writerows(filtered_users)

        print(f"Saved {len(filtered_users)} users to F:\\users.csv")

if __name__ == "__main__":
    main_question3()

for i in range(10, 20):
    data = fetch_data(api_url + str(i))
    process_and_save(data,"F:\\user.csv")
    print(fetch_data(api_url + str(i)))