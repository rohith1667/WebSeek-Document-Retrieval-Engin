import subprocess
from nicegui import ui
import requests
from processor import app


base_url = "http://127.0.0.1:5000"
topSearchResults = {}
startProcress = True
if startProcress:
    subprocess.Popen(["python", "processor.py"])
    startProcress = False

def on_start():
    # Send a GET request to the init endpoint of the Flask server
    response = requests.get(f"{base_url}/init")

    # Check if the response status code is 200
    if response.status_code == 200:
        print("Flask server initialized successfully.")

        # Display a notification message to the user
        ui.notify(response.json()['message'], type='positive')
    else:
        print("Error:", response.status_code, response.text)

        # Display an error notification message to the user
        ui.notify(response.json()['error'], type='negative')


def on_search_click():
    search_text = result.value
    # Define the URL for the POST request
    url = f"{base_url}/process_query"

    # Define any additional data to send in the POST request
    data = {"query": search_text}

    # Send the POST request using requests library
    response = requests.post(url, json=data)

    # Handle the response based on status code
    if response.status_code == 200:
        global topSearchResults
        topSearchResults = response.json()['results']
        search_list.refresh()

        # Display a notification message to the user
        ui.notify(response.json()['message'], type='positive')
    else:
        print("Error:", response.status_code, response.text)

        # Display an error notification message to the user
        ui.notify(response.json()['error'], type='negative')


@ui.refreshable
def search_list():
    with ui.list().classes('self.center'):
        for i in topSearchResults:
            ui.item(i['article'], on_click=lambda x: ui.navigate().to(i['link']))


ui.button("Start", on_click=on_start)

with ui.row().classes('self-center'):
    result = ui.input(placeholder='start typing').props(
        'wide-input rounded outlined dense self-center').classes('w-96')
    ui.button("Search", on_click=on_search_click)

search_list()

# Run the UI
ui.run()
