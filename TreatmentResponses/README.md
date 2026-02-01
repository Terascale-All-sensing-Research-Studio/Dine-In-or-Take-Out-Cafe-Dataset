# Treatment Responses

Our study consisted of four treatments: 
1.	No wait for maître d' with No wait for food (00): The participant is spawned into the cafe area and may approach the maître d' podium at any time to engage in dialogue with the maître d' NPC. The participant may then make a selection on a menu item, and the scene ends.
2.  No wait for maître d' with 3-minute wait for food (03): The participant is spawned into the cafe area and may approach the maître d' podium at any time to engage in dialogue with the maître d' NPC. The participant may then make a selection on a menu item, starting a 3-minute wait for food. The scene ends after the wait time.
3.  3-minutes wait for maître d' with No wait for food (30): The participant is spawned into the cafe area and may approach the maître d' podium at any time. The interacting maître d' NPC tells the participant she will be with them shortly, starting a 3-minute wait time. After 3-minutes, the maître d' engages in dialogue with the participant.The participant may then make a selection on a menu item, and the scene ends.
4.  3-minutes wait for maître d' with 3-minute wait for food (33): The participant is spawned into the cafe area and may approach the maître d' podium at any time. The interacting maître d' NPC tells the participant she will be with them shortly, starting a 3-minute wait time. After 3-minutes, the maître d' engages in dialogue with the participant.The participant may then make a selection on a menu item, starting a 3-minute wait for food. The scene ends after the wait time.

All participants complete all four treatments, however, treatments are assigned in random order to each participant as provided in the treatment_order.csv file:

| Dataset Column | Data | Value | 
| ------------- | ------------- | ------------- |
| 1 | Participant ID | Unique 5-character ID assigned to each participant. |
| 2 | Treatment1 | 00, 03, 30, or 33 to indicate which treatment the participant completed first. |
| 3 | Treatment2 | 00, 03, 30, or 33 to indicate which treatment the participant completed second. |
| 4 | Treatment3 | 00, 03, 30, or 33 to indicate which treatment the participant completed third. |
| 5 | Treatment4 | 00, 03, 30, or 33 to indicate which treatment the participant completed fourth. |

Treatment responses are provided in two CSV file formats: Numerical and String

| Dataset Column | Data | Response Value | 
| ------------- | ------------- | ------------- |
| 1 | Participant ID | Unique 5-character ID assigned to each participant. |
| 2 | TreatmentPeopleProximity | Integer Likert scale value with 1 being Very close, 2 being Somewhat close, 3 being Neither, 4 being Somewhat far, and 5 being Very far, indicating the participant's perception of proximity of the NPC's in the scene|
| 3 | TreatmentNoiseLevel | Integer Likert scale value with 1 being Very quiet, 2 being Somewhat quiet, 3 being Neither, 4 being Somewhat loud, and 5 being Very loud, indicating the participant's perception of noise level of the scene. |
| 4 | TreatmentDelay | Integer Likert scale value with 1 being Very low, 2 being Somewhat low, 3 being Neither, 4 being Somewhat high, and 5 being Very high, indicating the participant's frustration level with delay times. |
| 5 | TreatmentIsolation | Integer Likert scale value with 1 being Very low, 2 being Somewhat low, 3 being Neither, 4 being Somewhat high, and 5 being Very high, indicating the participant's frustration level from feeling isolated. |
| 6 | TreatmentAnxiety | Integer Likert scale value with 1 being Very low, 2 being Somewhat low, 3 being Neither, 4 being Somewhat high, and 5 being Very high, indicating the participant's frustratin level from feeling anxious. |
| 7 | TreatmentRealLifeLikelihood | Integer Likert scale value with 1 being Very likely, 2 being Somewhat likely, 3 being Neither, 4 being Somewhat unlikely, and 5 being Very unlikely, indicating the participant's likeliness to make the same choices in a similar real life scenario. |
