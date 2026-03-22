## Dine In or Take Out Café Dataset: 

## Contents
[Description](#description)

[Contributors](#contributors)

[Overview of Dataset](#overview-of-dataset)

## Description
Our Dine In or Take Out Café Dataset can be accessed by visiting our GitHub repository [1]. The dataset consists of 35 participants, of whom 33 fall into the Gen Z and 1 in the cusper Zillennials category, interacting in a digital twin of a café to order food for dine in or take out. Our virtual café, called Flavor and Vine, was designed using Unity 6000.0.53f1. Each participant interacts with a maître d' non-playable character (NPC) to order food off a digital menu. Each participant completes the following 4 treatments, with treatments assigned at random: No wait for maître d' with No wait for food (coded as 00), No wait for maître d' with 3-minute wait for food (coded as 03), 3-minutes wait for maître d' with No wait for food (coded as 30), and 3-minutes wait for maître d' with 3-minute wait for food (coded as 33).  In our dataset all participants provided data using the same Meta Quest Pro headset. Prior to interacting in the virtual café, we collected participant demographics for age, self-identified gender, ethnicity, race, education level, whether they wear glasses, if they wear contacts, how frequently they play video games, what type of video games they play, how frequently they use VR, if they own a VR device, what type of VR devices they use, how frequently they use take-out services, how frequently they use dine-in services, and which of these services they prefer. All participants completed the Frustration Distraction Scale (FDS), Revised UCLA-20 Loneliness Scale (R-UCLA), Social Phobia Inventory (SPIN), State Trait Anxiety Inventory (STAI) to measure frustration and discomfort intolerance, loneliness, social phobia, and anxiety respectively prior to immersion. After each treatment, participants completed the STAI to record changes in anxiety and completed a survey asking them how close they felt the other people were in the café, how they perceived the noise level, how likely they were to make the same table selection in real-life, and their frustration with the delay, sense of isolation, and feeling of anxiousness. After completing all four treatments, participants completed a second FDS to record changes in frustration as well as the NASA Task Load Index (NASA TLX) to measure perceived workload, System Usability Scale (SUS) to measure overall usability, and the Virtual Reality Sickness Questionnaire (VRSQ) to measure any feelings of simulator discomfort. Each participant provided data in a single session lasting approximately 1 hour. For each participant we recorded: a button log showing their dialogue and menu choices, eye gaze hit locations showing objects viewed per timestamp based on the gaze ray intersections with scene objects, hand grab log showing the objects interacted with using their hands, headset position and orientation, and left and right-hand position and orientation. All folders in our repository contain README.md files that describe the contents of each folder and file within the directory. In our dataset the Participant ID is consistent across all folders.

## Contributors
Elza Ibragimov, Natasha Kholgade Banerjee, Sean Banerjee, Ashutosh Shivakumar

[Terascale All-sensing Research Studio](https://tars-home.github.io)

## Overview of Dataset
The dataset is organized into the following folders:

| FolderName |	SubFolders |	DataType |	Contents |
| ------------- | ------------- | ------------- | ------------- |
| [Assets](https://github.com/Terascale-All-sensing-Research-Studio/VR-Social-Isolation-Cafe/blob/main/Assets/) |	Yes |	MP3	| Contains two subfolders, namely [00_03_Audio_Files](https://github.com/Terascale-All-sensing-Research-Studio/VR-Social-Isolation-Cafe/blob/main/Assets/00_03_Audio_Files) and [30_33_Audio_Files](https://github.com/Terascale-All-sensing-Research-Studio/VR-Social-Isolation-Cafe/blob/main/Assets/30_33_Audio_Files). The folder [00_03_Audio_Files](https://github.com/Terascale-All-sensing-Research-Studio/VR-Social-Isolation-Cafe/blob/main/Assets/00_03_Audio_Files) contains all the audio assets in MP3 format for the No wait for maître d' with No wait for food and No wait for maître d' with 3-minute wait for food treatments. [30_33_Audio_Files](https://github.com/Terascale-All-sensing-Research-Studio/VR-Social-Isolation-Cafe/blob/main/Assets/30_33_Audio_Files) contains all the audio assets in MP3 format for the 3-minute wait for maître d' with No wait for food and 3-minute wait for maître d' with 3-minute wait for food treatments.  The audio files are generated using [ElevenLabs](https://elevenlabs.io/).  |
| [Cybersickness](https://github.com/Terascale-All-sensing-Research-Studio/VR-Social-Isolation-Cafe/blob/main/Cybersickness/) |	None |	CSV	| Participant responses to the standard Virtual Reality Cyber Sickness Questionnaire (VRSQ). Each participant is assigned a unique 5-character ID. |
| [Demographics](https://github.com/Terascale-All-sensing-Research-Studio/VR-Social-Isolation-Cafe/blob/main/Demographics/) |	None |	CSV	| Participant demographics consisting of: age, self-identified gender, ethnicity, race, education level, whether they wear glasses, if they wear contacts, how frequently they play video games, what type of video games they play, how frequently they use VR, if they own a VR device, what type of VR devices they use, how frequently they use take-out services, how frequently they use dine-in services,and which of these services the most often choose. Each participant is assigned a unique 5-character ID. |
| [FDS](https://github.com/Terascale-All-sensing-Research-Studio/VR-Social-Isolation-Cafe/blob/main/FDS/)	| None |	CSV |	Participant responses to the standard Frustration Discomfort Scale (FDS). The CSV files are annotated as pre_ and post_ to indicate that they were administered prior to and after the immersion. The CSV files are annotated as numerical_ and string_ to indicate the format of the scale values. Each participant is assigned a unique 5-character ID. |
| [NASA_TLX](https://github.com/Terascale-All-sensing-Research-Studio/VR-Social-Isolation-Cafe/blob/main/NASA_TLX/) |	None |	CSV	| Participant responses to the standard 21-tick NASA Task Load Index (TLX). Each participant is assigned a unique 5-character ID. |
| [ObjectNames](https://github.com/Terascale-All-sensing-Research-Studio/VR-Social-Isolation-Cafe/blob/main/ObjectNames/) |	None |	None | The EyeGaze.csv found in the [VRData](https://github.com/Terascale-All-sensing-Research-Studio/VR-Social-Isolation-Cafe/blob/main/VRData/) folder for each participant contains a column titled objectName that stores the name of the object being observed. A top down view of the scene is provided along with a list of labeled ObjectNames. |
| [R_UCLA](https://github.com/Terascale-All-sensing-Research-Studio/VR-Social-Isolation-Cafe/blob/main/R_UCLA/) | None | CSV | Participant responses to the Revised UCLA Loneliness Scale (R-UCLA). Each participant is assigned a unique 5-character ID. |
| [SPIN](https://github.com/Terascale-All-sensing-Research-Studio/VR-Social-Isolation-Cafe/blob/main/SPIN/) | None | CSV | Participant responses to the Social Phobia Inventory (SPIN). Each participant is assigned a unique 5-character ID. |
| [STAI](https://github.com/Terascale-All-sensing-Research-Studio/VR-Social-Isolation-Cafe/blob/main/STAI/) | None | CSV | Participant responses to the State Trait Anxiety Inventory (STAI). Each participant is assigned a unique 5-character ID. |
| [SUS](https://github.com/Terascale-All-sensing-Research-Studio/VR-Social-Isolation-Cafe/blob/main/SUS/)	| None |	CSV	| Participant responses to the standard System Usability Scale (SUS). Each participant is assigned a unique 5-character ID. |
| [TreatmentResponses](https://github.com/Terascale-All-sensing-Research-Studio/VR-Social-Isolation-Cafe/blob/main/TreatmentResponses/) |	None |	CSV	| Participant responses to each treatment, i.e., not being forced to wait for a social interaction (00 or 03) or being forced to wait for a social interaction (33 or 30). Participant responses include their frustration level on a 5-point Likert scale caused by people proximity, noise level, time delay, feeling isolated, anxiousness, and finally their likelihood of doing making the same choices in real life. Each participant is assigned a unique 5-character ID.
| [VRData](https://github.com/Terascale-All-sensing-Research-Studio/VR-Social-Isolation-Cafe/blob/main/VRData/)	| Yes	| CSV | Contains 35 subfolders that represents each participant. Each subfolder is named with the unique 5-character ID. Within each participant subfolder there are four additional subfolders named ParticipantID_0_0, ParticipantID_0_3, ParticipantID_3_0, and ParticipantID_3_3. Here Participant_ID is the unique 5-character ID and _0_0, _0_3, _3_0, and _3_3  are the wait conditions. Within the ParticipantID_0_0, ParticipantID_0_3, ParticipantID_3_0, and ParticipantID_3_3 subfolders are *six CSV files for Button Log (ButtonLog), Eye Gaze (EyeGazeLog), *Hand Grab Log (HandGrabLog), Head Position and Orientation (Head), Left Hand (LeftHand), and Right Hand (RightHand). Thus, each participant has *24 CSV files. |

*HandGrabLog is only created if a participant interacts with an object in the environment using their hands.

## Directory Tree
We provide the directory tree below for the repository and the tree for one example participant (0P9C0) in the VRData folder:

```
├── Assets
│   ├── 00_03_Audio_Files
│   │   ├── FemaleBackgroundConvo.mp3
│   │   ├── OkRightThisWay.mp3
│   │   ├── Sorry.mp3
│   │   ├── TrimmedCafeAmbientNoise.mp3
│   │   ├── Welcome.mp3
│   │   ├── WelcomeLoop.mp3
│   │   ├── WillStandingTableWork.mp3
│   │   └── WillTakeoutWork.mp3
│   ├── 30_33_Audio_Files
│   │   ├── FemaleBackgroundConvo.mp3
│   │   ├── OkRightThisWay.mp3
│   │   ├── Sorry.mp3
│   │   ├── TrimmedCafeAmbientNoise.mp3
│   │   ├── Welcome.mp3
│   │   ├── WelcomeLoop.mp3
│   │   ├── WillStandingTableWork.mp3
│   │   ├── WillTakeoutWork.mp3
│   │   └── WithYouShortly.mp3
│   └── README.md
├── Cybersickness
│   ├── numerical_vrsq.csv
│   ├── README.md
│   └── string_vrsq.csv
├── Demographics
│   ├── demographics.csv
│   └── README.md
├── FDS
│   ├── numerical_post_fds.csv
│   ├── numerical_pre_fds.csv
│   ├── README.md
│   ├── string_post_fds.csv
│   └── string_pre_fds.csv
├── NASA_TLX
│   ├── nasatlx.csv
│   └── README.md
├── ObjectNames
│   ├── README.md
│   └── top_down_view.png
├── R_UCLA
│   ├── numerical_ucla.csv
│   ├── README.md
│   └── string_ucla.csv
├── SPIN
│   ├── numerical_spin.csv
│   ├── README.md
│   └── string_spin.csv
├── STAI
│   ├── numerical_00_stai.csv
│   ├── numerical_03_stai.csv
│   ├── numerical_30_stai.csv
│   ├── numerical_33_stai.csv
│   ├── numerical_pre_stai.csv
│   ├── README.md
│   ├── string_00_stai.csv
│   ├── string_03_stai.csv
│   ├── string_30_stai.csv
│   ├── string_33_stai.csv
│   └── string_pre_stai.csv
├── SUS
│   ├── numerical_sus.csv
│   ├── README.md
│   └── string_sus.csv
├── TreatmentResponses
│   ├── numerical_00_responses.csv
│   ├── numerical_03_responses.csv
│   ├── numerical_30_responses.csv
│   ├── numerical_33_responses.csv
│   ├── README.md
│   ├── string_00_responses.csv
│   ├── string_03_responses.csv
│   ├── string_30_responses.csv
│   ├── string_33_responses.csv
│   └── treatment_order.csv
├── VRData
│   ├── 0P9C0
│   │   ├── 0P9C0_0_0
│   │   │   ├── ButtonLog.csv
│   │   │   ├── EyeGaze.csv
│   │   │   ├── Head.csv
│   │   │   ├── LeftHand.csv
│   │   │   └── RightHand.csv
│   │   ├── 0P9C0_0_3
│   │   │   ├── ButtonLog.csv
│   │   │   ├── EyeGaze.csv
│   │   │   ├── Head.csv
│   │   │   ├── LeftHand.csv
│   │   │   └── RightHand.csv
│   │   ├── 0P9C0_3_0
│   │   │   ├── ButtonLog.csv
│   │   │   ├── EyeGaze.csv
│   │   │   ├── Head.csv
│   │   │   ├── LeftHand.csv
│   │   │   └── RightHand.csv
│   │   └── 0P9C0_3_3
│   │       ├── ButtonLog.csv
│   │       ├── EyeGaze.csv
│   │       ├── Head.csv
│   │       ├── LeftHand.csv
│   │       └── RightHand.csv│   
│   └── README.md
├── dictionary.csv
├── LICENSE
├── README.md
└── vrdata_frame_summary.py
```

### Dataset Frame Rate Summary
The minimum (Min), maximum (Max), average (Mean), and standard deviation (SD) frame rate for the eye gaze, head, left hand, and right hand for our dataset are provided below. The table below is generated by running the Python script [vrdata_frame_summary.py](https://github.com/Terascale-All-sensing-Research-Studio/VR-Social-Isolation-Cafe/blob/main/waitSummary.py) over the [VRData](https://github.com/Terascale-All-sensing-Research-Studio/VR-Social-Isolation-Cafe/blob/main/VRData) folder.

| Treatment | Type of Data | Min | Max | Mean | SD |
| ----- | ----- | ----- | ----- | ----- | ----- |
| 00 | EyeGaze | 46.69 | 70.72 | 66.39 | 4.89 |
|| Head | 46.83 | 70.45 | 66.85 | 4.70 |
|| LeftHand | 46.83 | 70.45 | 66.85 | 4.70 |
|| RightHand | 46.83 | 70.45 | 66.85 | 4.70 |
| 03 | EyeGaze | 50.75 | 71.67 | 68.78 | 3.80 |
|| Head | 52.42 | 71.71 | 70.00 | 3.29 |
|| LeftHand | 52.42 | 71.71 | 70.00 | 3.29 |
|| RightHand | 52.42 | 71.71 | 70.00 | 3.29 |
| 30 | EyeGaze | 42.72 | 71.40 | 68.13 | 5.75 |
|| Head | 43.79 | 71.43 | 69.41 | 5.32 |
|| LeftHand | 43.79 | 71.43 | 69.41 | 5.32 |
|| RightHand | 43.79 | 71.43 | 69.41 | 5.32 |
| 33 | EyeGaze | 51.64 | 71.46 | 69.09 | 3.51 |
|| Head | 52.60 | 72.45 | 70.31 | 3.32 |
|| LeftHand | 52.60 | 72.45 | 70.31 | 3.32 |
|| RightHand | 52.60 | 72.45 | 70.31 | 3.32 |

