from js import document  

# Hi maam bawi ako sa FA...
# below is the dictionary which contains all club information
Clubz = {
    "Math Club": {
        "description": "Enhance your mathematical skills with math club!",
        "meeting_time": "Mondays 2:30 - 4:30 PM",
        "location": "Room 404",
        "moderator": "Sir. Gabuya",
        "members": "15"
    },
    "Science Club": {
        "description": "Innovate your inner Einstein... OBMC-FV Science club!",
        "meeting_time": "Tuesdays 3:00 - 4:00 PM, Fridays 2:00 - 3:00 PM",
        "location": "Room 404",
        "moderator": "Ms. Maramag",
        "members": "22"
    },
    "Dance Club": {
        "description": "Dance your heart away with dance club!",
        "meeting_time": "Tuesday 3:00 - 5:00 PM",
        "location": "Teatro Preciosa",
        "moderator": "Sir. Cases",
        "members": "50+"
    },
    "Communications Arts Club": {
        "description": "For the artists, journalists, and public speaking, ComArts!",
        "meeting_time": "Wednesday 3:00 - 4:00 PM, Friday 3:00 - 4:00 PM",
        "location": "Room 406",
        "moderator": "Ms. Yannis",
        "members": "20"
    },
    "Basketball Varsity": {
        "description": "Lock in and play with the OBMC-FV Basketball varsity team!",
        "meeting_time": "Monday 3:00 - 5:00 PM",
        "location": "Quadrangle",
        "moderator": "Sir. Ruiz",
        "members": "23"
    },
    "Marching Band Club": {
        "description": "OBMC-FV Marching band! Performs in events, programs, etc.",
        "meeting_time": "Mon, Tue, Wed 3:00 - 4:30 PM",
        "location": "Marching Band Room",
        "moderator": "Sir. Alumno",
        "members": "45"
    },
    "Volleyball Varsity": {
        "description": "Set, Spike, Boom! Check out the OBMC-FV Volleyball varsity team!",
        "meeting_time": "Wednesday 3:00 - 4:00 PM",
        "location": "Quadrangle",
        "moderator": "Sir. Ruiz",
        "members": "25"
    },
    "COCC Club": {
        "description": "Enhance your discipline, be a leader. COCC Club!",
        "meeting_time": "Wednesdays 2:30 - 4:30 PM",
        "location": "Fourth Floor, Quadrangle",
        "moderator": "SSgt Jemima David, PA (Res)",
        "members": "16"
    },
    "Glee Club": {
        "description": "Sings from the chambers of your hear -- Glee Club!",
        "meeting_time": "Mondays and Fridays 3:00 - 4:30 PM",
        "location": "Music Room",
        "moderator": "Sir Martin",
        "members": "28"
    },
    "Social Science Club": {
        "description": "Be social, and join SocSci Club!!",
        "meeting_time": "Tuesdays and Thursdays 3:00 - 4:00 PM",
        "location": "Room 409",
        "moderator": "Sir. Lim",
        "members": "18"
    },
}


# show info function gets the selected info from "clubz" and updates the output

def show_info(event=None):
    # this will get the selected club from the dropdown
    selected = document.querySelector("#clubSelect").value
    # this is connected to the div where the club information will be displayed
    output_div = document.querySelector("#output")
    
    # If no such club is selecte it will display a warning message
    if not selected:
        output_div.innerHTML = "<b>Please select a club first!</b>"
        return
    
    # this will take back the selected clubs information from the dictionary
    club = Clubz[selected]
    
    # this essentially like formats the content for displaying the club info in an aesthtically pleasing format 
    # the code below (card) is taken from W3SCHOOLS and the styling is formatted using chatgpt, because when i formatted the color, padding, font size, etc. it was very messy.
    profile = f"""
    <div class="card" style="background-color: rgba(255,255,255,0.0); border-width: 0px; padding:20px; border-radius: 0px; font-size:18px; text-align:left;">
        <h3 style="font-weight:bold; margin-bottom:0px;">{selected}</h3>
        <p><strong>Description:</strong> {club['description']}</p>
        <p><strong>Meeting Time:</strong> {club['meeting_time']}</p>
        <p><strong>Location:</strong> {club['location']}</p>
        <p><strong>Moderator:</strong> {club['moderator']}</p>
        <p><strong>Members:</strong> {club['members']}</p>
    </div>
    """
    
    # this will put the generated HTML into the div
    output_div.innerHTML = profile
