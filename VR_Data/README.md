# VR Data

Our study consisted of four treatments: 
1. No wait for hostess, No wait for food: When the participant is teleported into the cafe area, they are presented with an empty queue and can approach the hostess NPC when they wish. They may go through a series of dialogue with the hostess NPC and make a selection on a menu item, ending the scene.
2. No wait for hostess, 3-minute wait for food: The participant is teleported into the scene and can approach the hostess NPC when they wish. They may go through a series of dialogue with the hostess NPC and make a selection on a menu item, prompting a 3-minute wait time, that is not disclosed to the participant. The scene ends after the wait time. 
3. 3-minute wait for hostess, No wait for food: The participant is teleported into the scene and can approach the hostess NPC when they wish. The hostess communicates that they will be with the participant shortly and looks down at her tablet, prompting a 3-minute wait time. After the wait time is complete, the hostess engages in a series of dialogue with the participant, in which they make a selection on a menu item, ending the scene.
4. 3-minute wait for hostess, 3-minute wait for food: The participant is teleported into the scene and can approach the hostess NPC when they wish. The hostess communicates that they will be with the participant shortly and looks down at her tablet, prompting a 3-minute wait time, that is not disclosed to the participant. After the wait time is complete, the hostess engages in a series of dialogue with the participant, in which they make a selection on a menu item. A 3-minute wait time, that is not disclosed to the participant, is prompted. The scene ends after the wait time.

Each of the 35 folders here represents a single participant. The folder is named with a unique 5-character ID assigned to each participant. Within each of these 35 folders there are four subfolders named ParticipantID_0_0, ParticipantID_0_3, ParticipantID_3_0, and ParticipantID_3_3. Here, ParticipantID is the 5-character ID assigned to each participant and 0_0, 0_3, 3_0, and 3_3 indicates whether the participant was in a no wait for hostess and no wait for food, a no wait for hostess and 3-minute wait for food, a 3-minute wait for hostess and no wait for food, or a 3-minute wait for hostess and 3-minute wait for food. Within the 0_0, 0_3, 3_0, and 3_3 sub-subfolders are at minimum 5 raw CSV files, for a total of 20 raw CSV files per participant. 

*An additional 6th raw CSV file is included only if the participant interacts with objects in the scene, with a max possible total of 24 raw CSV files per participant. 

The names and locations of each of these CSV files are as follows:

| Filename |	Location |
| -------- | -------- |
| ButtonLog.csv	| ParticipantID/ParticipantID_0_0 |
| EyeGaze.csv	| ParticipantID/ParticipantID_0_0 |
| *HandGrabLog.csv	| ParticipantID/ParticipantID_0_0 |
| Head.csv	| ParticipantID/ParticipantID_0_0 |
| LeftHand.csv	| ParticipantID/ParticipantID_0_0 | 
| RightHand.csv	| ParticipantID/ParticipantID_0_0 |
| ButtonLog.csv	| ParticipantID/ParticipantID_0_3 |
| EyeGaze.csv	| ParticipantID/ParticipantID_0_3 |
| *HandGrabLog.csv	| ParticipantID/ParticipantID_0_3 |
| Head.csv	| ParticipantID/ParticipantID_0_3 |
| LeftHand.csv	| ParticipantID/ParticipantID_0_3 | 
| RightHand.csv	| ParticipantID/ParticipantID_0_3 |
| ButtonLog.csv	| ParticipantID/ParticipantID_3_0 |
| EyeGaze.csv	| ParticipantID/ParticipantID_3_0 |
| *HandGrabLog.csv	| ParticipantID/ParticipantID_3_0 |
| Head.csv	| ParticipantID/ParticipantID_3_0 |
| LeftHand.csv	| ParticipantID/ParticipantID_3_0 | 
| RightHand.csv	| ParticipantID/ParticipantID_3_0 |
| ButtonLog.csv	| ParticipantID/ParticipantID_3_3 |
| EyeGaze.csv	| ParticipantID/ParticipantID_3_3 |
| *HandGrabLog.csv	| ParticipantID/ParticipantID_3_3 |
| Head.csv	| ParticipantID/ParticipantID_3_3 |
| LeftHand.csv	| ParticipantID/ParticipantID_3_3 | 
| RightHand.csv	| ParticipantID/ParticipantID_3_3 |

The content stored in each of these 24 CSV files per participant are as follows:

| Filename |	Content |
| -------- | -------- |
| ButtonLog.csv	| **timeStampNs:** Time stamp in nanoseconds for when the button interaction event was recorded.<br> **gameTime:** Game time stamp in seconds for when the button interaction event was recorded.<br>**buttonSelection:** Human readable name for the button interacted with in the scene.|
| EyeGaze.csv	| **timeStampNs:** Time stamp in nanoseconds for when the eye gaze event was recorded.<br> **gameTime:** Game time stamp in seconds for when the eye gaze event was recorded.<br>**objectName:** Human readable name for the scene object the eye gaze has recorded.<br> **posX:** X position of the eye gaze hit location. <br> **posY:** Y position of the eye gaze hit location. <br> **posZ:** Z position of the eye gaze hit location. |
| *HandGrabLog.csv	| **timeStampNs:** Time stamp in nanoseconds for when the head movement was recorded.<br> **gameTime:** Game time stamp in seconds for when the head movement was recorded.<br> **hand:** Specifies which hand the object was interacted with.<br> **objectName:** Human readable name for the object interacted with in the scene.|
| Head.csv	| **timeStampNs:** Time stamp in nanoseconds for when the head movement was recorded.<br> **gameTime:** Game time stamp in seconds for when the head movement was recorded.<br> **posX:** X position of the head location. <br> **posY:** Y position of the head location. <br> **posZ:** Z position of the head location. <br> **rotX:** X rotation of the head location. <br> **rotY:** Y rotation of the head location. <br> **rotZ:** Z rotation of the head location. |
| LeftHand.csv	| **timeStampNs:** Time stamp in nanoseconds for when the left hand movement was recorded.<br> **gameTime:** Game time stamp in seconds for when the left hand movement was recorded.<br> **posX:** X position of the left hand location. <br> **posY:** Y position of the left hand location. <br> **posZ:** Z position of the left hand location. <br> **rotX:** X rotation of the left hand location. <br> **rotY:** Y rotation of the left hand location. <br> **rotZ:** Z rotation of the left hand location. |
| RightHand.csv	| **timeStampNs:** Time stamp in nanoseconds for when the right hand movement was recorded.<br> **gameTime:** Game time stamp in seconds for when the right hand movement was recorded.<br> **posX:** X position of the right hand location. <br> **posY:** Y position of the right hand location. <br> **posZ:** Z position of the right hand location. <br> **rotX:** X rotation of the right hand location. <br> **rotY:** Y rotation of the right hand location. <br> **rotZ:** Z rotation of the right hand location. |
