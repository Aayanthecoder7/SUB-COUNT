from tkinter import *
import requests

# Initialize the main application window
root = Tk()
root.title("Social Media Automation Tool")
root.config(background="Black")
root.geometry("300x300")


def sub_count():
    # Your RapidAPI key
    api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  #API FROM RAPIDAPI (YOUTUBE v4)

    # The URL for the YouTube API endpoint (from RapidAPI)
    url = "https://youtube-v31.p.rapidapi.com/channels"

    # Set up the query parameters (Channel ID for MrBeast)
    params = {
        "id": "UCX6OQ3DkcsbYNE6H8uQQuVA",  # MrBeast's Channel ID
        "part": "statistics"  # We're interested in the 'statistics' part for subscriber count
    }

    # Set up the headers with the API key
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "youtube-v31.p.rapidapi.com"
    }

    try:
        # Send a GET request to the API
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an error for unsuccessful requests

        # Parse the JSON response
        data = response.json()

        # Check if the response contains the necessary data
        if "items" in data and len(data["items"]) > 0:
            # Extract the subscriber count
            subscriber_count = data["items"][0]["statistics"]["subscriberCount"]
            mrbast.config(text=f"Subscribers: {subscriber_count}")
        else:
            mrbast.config(text="No data found.")
    except requests.exceptions.RequestException as e:
        mrbast.config(text="Error: API request failed.")
        print(e)

# UI Elements
titel_label = Label(root, text="SUB COUNT:", bg="Black", fg="Red", font=("Arial", 22))
titel_label.pack()

get_sub = Button(root, text="CLICK TO SEE SUBS COUNTS", command=sub_count)
get_sub.pack()

mrbast = Label(root, text="", bg="Black", fg="Cyan")
mrbast.pack()

# Start the main event loop
root.mainloop()
