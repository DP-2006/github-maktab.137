import requests
import csv

def fetch_user_data():
    try:
        print("Fetching data from API")
        response = requests.get('https://jsonplaceholder.typicode.com/users',)

        if response.status_code == 200:
            print("Data received successfully")
            return response
        else:
            print(f"Error: Status code {response.status_code}")
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None


def process_and_save_data(users_data, output_path):
    if users_data is None:
        print("no data to process")
        return False
    filtered_users = []
    filtered_users.append({
        'name': user.get('name', 'Unknown'),
        'email': user.get('email', 'Unknown')
    })


    try:
        with open(output_path, 'w+', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['name', 'email'])
            writer.writeheader()


        print(f"Data saved to {output_path}")
        return True

    except Exception as e:
        print(f"Save error: {e}")
        return False


def main():
    print("Starting data pipeline...")

    users = fetch_user_data()

    if users is not None:
        success = process_and_save_data(users, 'processed_users.csv')
        if success:
            print("Pipeline completed successfully!")
        else:
            print("Error in data processing")
    else:
        print("Data fetch failed")

