import requests
import csv


def fetch_user_data():
    try:
        print(" data from API")
        response = requests.get('https://jsonplaceholder.typicode.com/users', timeout=10)

        if response.status_code == 200:
            print("Data received successfully")
            return response.json()
        else:
            print(f"Error: Status code {response.status_code}")
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None


def process_and_save_data(users_data, output_path):
    if users_data is None:
        print("No data to process")
        return False

    print(f"Processing {len(users_data)} users")

    filtered_users = []


    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['name', 'email'])
            writer.writeheader()
            writer.writerows(filtered_users)

        print(f"Data saved to {output_path}")
        print(f"Filtered users: {len(filtered_users)}")
        return True

    except Exception as e:
        print(f"Save error: {e}")
        return False


def main():
    print("Starting data pipeline...")

    # Step 1: Get data from API
    users = fetch_user_data()

    # Step 2: Process and save
    if users is not None:
        success = process_and_save_data(users, 'processed_users.csv')
        if success:
            print("Pipeline completed successfully!")
        else:
            print("Error in data processing")
    else:
        print("Data fetch failed")


if __name__ == "__main__":
    main()