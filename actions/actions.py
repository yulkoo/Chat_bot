# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
# REQUIRED_SKILLS = ["python", "sql", "алгоритмы", "git"]
#
#
# class ActionCompareSkills(Action):
#     def name(self) -> Text:
#         return "action_compare_skills"
#
#     def run(
#             self,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]
#     ) -> List[Dict[Text, Any]]:
#
#         user_skills = [s.lower() for s in tracker.get_slot("skills") or []]
#         missing_skills = [s for s in REQUIRED_SKILLS if s not in user_skills]
#
#         if missing_skills:
#             dispatcher.utter_message(
#                 response="utter_missing_skills",
#                 missing_skills=", ".join(missing_skills))
#         else:
#             dispatcher.utter_message(response="utter_good_skills")
#
#         return []
