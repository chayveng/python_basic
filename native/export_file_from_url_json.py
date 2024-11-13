import requests
import pandas as pd

# Make a GET request to fetch data from the API
urls = [
    "https://jsonplaceholder.typicode.com/posts",
    "https://jsonplaceholder.typicode.com/comments",
    "https://jsonplaceholder.typicode.com/albums",
    "https://jsonplaceholder.typicode.com/photos",
    "https://jsonplaceholder.typicode.com/todos",
    "https://jsonplaceholder.typicode.com/users"
]

def export_excel_file():
    for url in urls:
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response into a list of dictionaries
            data = response.json()

            # Convert the data to a DataFrame using pandas
            df = pd.DataFrame(data)
            
            file_name = url.split("/")[-1]

            # Export the DataFrame to an Excel file
            df.to_excel(f'exports/files/{file_name}.xlsx', index=False)

            print(f"Data has been successfully exported to {file_name}.xlsx")
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")


def export_csv_file():
    for url in urls:
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response into a list of dictionaries
            data = response.json()

            # Convert the data to a DataFrame using pandas
            df = pd.DataFrame(data)
            
            file_name = url.split("/")[-1]

            # Export the DataFrame to an Excel file
            df.to_csv(f'exports/files/csv/{file_name}.csv', index=False)

            print(f"Data has been successfully exported to {file_name}.csv")
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")

# export_excel_file()
export_csv_file()