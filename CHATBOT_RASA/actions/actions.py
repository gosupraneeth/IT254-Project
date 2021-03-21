# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from rasa_sdk.forms import FormAction
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet, Form
import logging
import datetime

LANGUAGES = {
    "telugu":
        {
            "name": "telugu",
            "resource": "tl"
        },
    "english":
        {
            "name": "english",
            "resource": "en"
        },
    "hindi":
        {
            "name": "hindi",
            "resource": "hn"
        },
    "bengali":
        {
            "name": "bengali",
            "resource": "bn"
        },
    "kannada":
        {
            "name": "kannada",
            "resource": "kn"
        },
    "marathi":
        {
            "name": "marathi",
            "resource": "mr"
        },
    "malayalam":
        {
            "name": "malayalam",
            "resource": "ml"
        },
    "punjabi":
        {
            "name": "punjabi",
            "resource": "pa"
        },
    "tamil":
        {
            "name": "tamil",
            "resource": "ta"
        }
}

MOOD= ["happy","sad","upset","worry","excited","silly","frustrated","scared","angry"]

GENRE = ["action","comedies","crime","documentaries","drama","fantasy","horror","romance","sci-fi","thriller","under 18","18+"]

def _resolve_name(languages, resource) ->Text:
    for key, value in languages.items():
        if value.get("resource") == resource:
            return value.get("name")
    return ""

class FindLanguageTypes(Action):
    """This action class allows to display buttons for languages to choose."""

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "find_language_types"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:
        
        buttons = []
        for t in LANGUAGES:
            language = LANGUAGES[t]
            payload =  language.get("name")

            buttons.append(
                {"title": "{}".format(language.get("name").title()),
                 "payload": payload})

        # TODO: update rasa core version for configurable `button_type`
        dispatcher.utter_message(template="utter_greet",buttons=buttons)
        return []

class FindMood(Action):
    """This action class allows to display buttons for languages to choose."""

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "find_mood"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:
        
        buttons = []
        for m in MOOD:
            payload =  m

            buttons.append(
                {"title": "{}".format(m.title()),
                 "payload": payload})

        # TODO: update rasa core version for configurable `button_type`
        dispatcher.utter_message(template="utter_select_mood",buttons=buttons)
        return []

class FindGenre(Action):
    """This action class allows to display buttons for languages to choose."""

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "find_genre"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:
        
        buttons = []
        for g in GENRE:
            payload =  g

            buttons.append(
                {"title": "{}".format(g.title()),
                 "payload": payload})

        # TODO: update rasa core version for configurable `button_type`
        dispatcher.utter_message(template="utter_select_genre",buttons=buttons)
        return []