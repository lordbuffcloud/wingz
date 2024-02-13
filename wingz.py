import requests
import tkinter as tk
from tkinter import PhotoImage
from threading import Thread, Event
import schedule
import time

def search_and_recommend(output, api_key, zip_code):
    output.insert(tk.END, f"Searching for traditional wings near the {zip_code}...\n")
    query = f"traditional wings in {zip_code}"
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&key={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors
        results = response.json().get('results', [])

        if results:
            recommended_place = compare_places(api_key, results)
            if recommended_place:
                output.insert(tk.END, f"Recommended Place: {recommended_place['name']}, Address: {recommended_place.get('formatted_address', 'No address provided')}, Price Level: {recommended_place.get('price_level', 'N/A')}, Rating: {recommended_place.get('rating', 'N/A')}\n")
            else:
                output.insert(tk.END, "Unable to determine a recommendation based on current criteria.\n")
        else:
            output.insert(tk.END, "No results found.\n")
    except requests.exceptions.RequestException as e:
        output.insert(tk.END, f"Error during search: {e}\n")

def fetch_place_details(api_key, place_id):
    url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name,rating,price_level,formatted_address&key={api_key}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json().get('result', {})

def calculate_place_score(place):
    
    price_score = 4 - place.get('price_level', 2)  # Assume a default price level of 2 if not available.
    rating_score = (place.get('rating', 0) - 1) * (4 / 4) # Normalize the rating to a 0-4 scale.

    # Calculate the weighted score: 70% rating, 30% price.
    weighted_score = (rating_score * 0.7) + (price_score * 0.3)
    
    return weighted_score

def compare_places(api_key, places):
    detailed_places = [fetch_place_details(api_key, place['place_id']) for place in places]
    
    # Add a 'score' key to each place based on our comparison logic.
    for place in detailed_places:
        place['score'] = calculate_place_score(place)
    
    # Recommend the place with the highest score.
    recommended_place = max(detailed_places, key=lambda x: x['score'])
    
    return recommended_place


def search_wings(output, api_key, zip_code):
    output.insert(tk.END, f"Searching for traditional wings near the {zip_code}...\n")
    
    # The query includes the type of food and the zip code for the location.
    query = f"traditional wings in {zip_code}"
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&key={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors
        results = response.json().get('results', [])

        if results:
            for result in results:
                name = result['name']
                address = result.get('formatted_address', 'No address provided')
                output.insert(tk.END, f"Found a place: {name} at {address}\n")
        else:
            output.insert(tk.END, "No results found.\n")
    except requests.exceptions.RequestException as e:
        output.insert(tk.END, f"Error during search: {e}\n")


def start_search(output, window, api_key, zip_code, stop_event):
    search_wings(output, api_key, zip_code)
    schedule.every(12).hours.do(lambda: search_wings(output, api_key, zip_code))
    while not stop_event.is_set():
        schedule.run_pending()
        time.sleep(1)

def stop_search(thread, stop_event):
    stop_event.set()
    thread.join()
    schedule.clear()

window = tk.Tk()
window.title("Wing Search")
window.configure(bg='black')

# Set the window size and position
window.geometry("400x500")
window.resizable(False, False)
window.eval('tk::PlaceWindow . center')

# Set the background image
background_image = PhotoImage(file="wingz.gif")
background_label = tk.Label(window, image=background_image, bg='black')
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame for the input elements
input_frame = tk.Frame(window, bg='black', bd=0)
input_frame.pack(pady=20)

zip_code_label = tk.Label(input_frame, text="Enter Zip Code:", fg='lime green', bg='black')
zip_code_label.pack(side=tk.LEFT, padx=10)

zip_code_entry = tk.Entry(input_frame, fg='black', bg='lime green')
zip_code_entry.pack(side=tk.LEFT)
zip_code_entry.insert(0, "45431")

# Create a frame for the output text
output_frame = tk.Frame(window, bg='black', bd=0)
output_frame.pack(pady=20)

output = tk.Text(output_frame, fg='lime green', bg='black', width=40, height=10)
output.pack()

# Create a frame for the buttons
button_frame = tk.Frame(window, bg='black', bd=0)
button_frame.pack(pady=20)

api_key = 'Google API Key'  # Replace this with your actual Google Places API key https://developers.google.com/
stop_event = Event()

def start_search_wrapper():
    stop_event.clear()  # Clear the stop event in case it was previously set
    # Adjust to call search_and_recommend instead of search_wings
    thread = Thread(target=search_and_recommend, args=(output, api_key, zip_code_entry.get()))
    thread.start()

start_button = tk.Button(button_frame, text="Start Search", command=start_search_wrapper, fg='lime green', bg='black')
start_button.pack(side=tk.LEFT, padx=10)

def stop_search_wrapper():
    stop_search(thread, stop_event)
    output.insert(tk.END, "Search stopped.\n")

stop_button = tk.Button(button_frame, text="Stop Search", command=stop_search_wrapper, fg='lime green', bg='black')
stop_button.pack(side=tk.LEFT)

window.mainloop()
