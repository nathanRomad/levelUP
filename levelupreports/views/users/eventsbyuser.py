"""Module for generating games by user report"""
import sqlite3
from django.shortcuts import render
from levelupapi.models import Event
from levelupreports.views import Connection


def userevent_list(request):
    """Function to build an HTML report of games by user"""
    if request.method == 'GET':
        # Connect to project database
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            # Query for all games, with related user info.
            db_cursor.execute("""
                SELECT
                    event_id,
                    datetime,
                    game_name,
                    host_id,
                    full_name
                FROM
                    EVENTS_BY_GAMER
            """)

            dataset = db_cursor.fetchall()

            # Take the flat data from the database, and build the
            # following data structure for each event.
            #             {
            #     1: {
            #         "gamer_id": 1,  = host_id
            #         "full_name": "Molly Ringwald", = full_name
            #         "events": [
            #             {
            #                 "id": 5,  = event_id
            #                 "datetime": "2020-12-23 00:00:00", = datetime
            #                 "game_name": "Fortress America"  = game_name
            #             }
            #         ]
            #     }
            # }

            events_by_user = {}

            for row in dataset:
                # Crete a Event instance and set its properties
                event = Event()
                event.id = row["event_id"]
                event.datetime = row["datetime"]
                event.game_name = row["game_name"]

                # Store the user's id
                uid = row["host_id"]

                # If the user's id is already a key in the dictionary...
                if uid in events_by_user:

                    # Add the current event to the `users` list for it
                    events_by_user[uid]['events'].append(event)

                else:
                    # Otherwise, create the key and dictionary value
                    events_by_user[uid] = {}
                    events_by_user[uid]["host_id"] = uid
                    events_by_user[uid]["full_name"] = row["full_name"]
                    events_by_user[uid]["events"] = [event]

        # Get only the values from the dictionary and create a list from them
        list_of_events_hosted_by_gamers = events_by_user.values()

        # Specify the Django template and provide data context
        template = 'users/events_by_gamers.html'
        context = {
            'events_gamer_list': list_of_events_hosted_by_gamers
        }

        return render(request, template, context)


# Note: You are strongly encouraged to take the time to understand the data structure above that is created from the results of the query.
# This is a common strategy for converting flat data from a SQL data set into a data structure to be used in your application.
