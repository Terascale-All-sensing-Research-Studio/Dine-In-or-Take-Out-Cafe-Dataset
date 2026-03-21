## User Behavior in an Interactive Virtual Reality Cafe (Social Isolation Dataset)

## Contents
[Description](#description)

[Contributors](#contributors)

[Overview of Dataset](#overview-of-dataset)

## Description
The Social Isolation Cafe dataset consists of 35 human participants interacting with a maître d' NPC in a virtual cafe environment, designed using a Unity 6000.0.53f1, to order food from a menu. Each participant is randomly assigned to 4 treatments: No wait for maître d' with No wait for food (00), No wait for maître d' with 3-minute wait for food (03), 3-minutes wait for maître d' with No wait for food (30), and 3-minutes wait for maître d' with 3-minute wait for food (33). Each participant completed all 4 treatments using a Meta Quest Pro headset. For each participant, we collect demographic data, frustration intolerance using the Frustration Discomfort Scale (FDS), subjective feelings of loneliness using the Revised UCLA Loneliness Scale (R-UCLA), severity of social phobia using Social Phobia Inventory (SPIN), and current state of anxiety using State Trait Anxiety Inventory (STAI) prior to immersion. After each treatment, participants provided their perceived level of anxiety using the STAI and custom frustration scales using a 5-point Likert scale. After completing all treatments, participants retook the FDS and completed the NASA Task Load Index (TLX), System Usability Scale (SUS), and Cybersickness in VR Questionnaire (VRSQ). Our dataset also consists of head, left hand, and right hand position and orientation data as well as object names and hit positions of all objects the participant visually and physically engaged with. 

## Contributors
Elza Ibragimov, Ava Megyeri, Natasha Kholgade Banerjee, Sean Banerjee, Ashutosh Shivakumar

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
└── README.md
```

### Dataset Frame Rate Summary
The minimum (Min), maximum (Max), average (Mean), and standard deviation (SD) frame rate for the eye gaze, hand grab log, head, left hand, and right hand for our dataset are provided below.  

| Treatment | Type of Data | Min | Max | Mean | SD |
| ----- | ----- | ----- | ----- | ----- | ----- |
| 00 | EyeGaze | 44.67 | 71.88 | 69.47 | 5.52 |
|| HandGrabLog | 47.67 | 50.58 | 49.13 | 2.05 |
|| Head | 44.86 | 71.88 | 70.16 | 5.38 |
|| LeftHand | 44.86 | 71.88 | 70.16 | 5.38 |
|| RightHand | 44.86 | 71.88 | 70.16 | 5.38 |
| 03 | EyeGaze | 50.82 | 72.4 | 69.5 | 3.93 |
|| HandGrabLog | 8.36 | 77.9 | 37.16 | 16.84 |
|| Head | 52.66 | 72.44 | 70.79 | 3.24 |
|| LeftHand | 52.66 | 72.44 | 70.79 | 3.24 |
|| RightHand | 52.66 | 72.44 | 70.79 | 3.24 |
| 30 | EyeGaze | 42.73 | 71.79 | 68.87 | 5.85 |
|| HandGrabLog | 8.68 | 72.09 | 28.8 | 18.92 |
|| Head | 43.7 | 71.81 | 70.22 | 5.37 |
|| LeftHand | 43.7 | 71.81 | 70.22 | 5.37 |
|| RightHand | 43.7 | 71.81 | 70.22 | 5.37 |
| 33 | EyeGaze | 51.84 | 71.77 | 69.46 | 3.53 |
|| HandGrabLog | 6.23 | 72.13 | 34.32 | 21.42 |
|| Head | 52.84 | 72.69 | 70.73 | 3.33 |
|| LeftHand | 52.84 | 72.69 | 70.73 | 3.33 |
|| RightHand | 52.84 | 72.69 | 70.73 | 3.33 |

