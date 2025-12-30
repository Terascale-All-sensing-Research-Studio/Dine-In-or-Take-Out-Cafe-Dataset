## Waiting in Line in Virtual Reality Dataset (WAIT)

## Contents
[Description](#description)

[Contributors](#contributors)

[Overview of Dataset](#overview-of-dataset)

## Description
The Social Isolation Cafe dataset consists of 35 human participants interacting with a hostess NPC in a virtual cafe environment, designed using a Unity 6000.0.53f1, to order food off a menu. Each participant is randomly assigned to 4 treatment: No wait for hostess and No wait for food (00), No wait for hostess and 3-minute wait for food (03), 3-minutes wait for hostess and No wait for food (30), and 3-minutes wait for hostess and 3-minute wait for food (33). Each participant completed all 4 treatments using a Meta Quest Pro headset. For each participant, we collect demographic data, frustration intolerance using the Frustration Discomfort Scale (FDS), subjective feelings of loneliness using the Revised UCLA Loneliness Scale (R-UCLA), severity of social phobia using Social Phobia Inventory (SPIN), and current state of anxiety using State Trait Anxiety Inventory (STAI) prior to immersion. After each treatment, participants provided their perceived level of anxiety using the STAI and custom frustration scales using a 5-point Likert scale. After completing all treatments, participants retook the FDS and completed the NASA Task Load Index (TLX), System Usability Scale (SUS), and Cybersickness in VR Questionnaire (VRCS). Our dataset also consists of head, left hand, and right hand position and orientation data as well as object names and hit positions of all objects the participant visually engaged with. 

## Contributors
TBA

[Terascale All-sensing Research Studio](https://tars-home.github.io)

## Overview of Dataset
The dataset is organized into the following folders:

| FolderName |	SubFolders |	DataType |	Contents |
| ------------- | ------------- | ------------- | ------------- |
| Cybersickness |	None |	CSV	| Participant responses to the standard Virtual Reality Cyber Sickness Questionnaire (VRCSQ). Each participant is assigned a unique 5-character ID. |
| Demographics |	None |	CSV	| Participant demographics consisting of: age, self-identified gender, ethnicity, race, education level, whether they wear glasses, if they wear contacts, how frequently they play video games, what type of video games they play, how frequently they use VR, if they own a VR device, what type of VR devices they use, how frequently they use take-out services, how frequently they use dine-in services,and which of these services the most often choose. Each participant is assigned a unique 5-character ID. |
| FDS	| None |	CSV |	Participant responses to the standard Frustration Discomfort Scale (FDS). The CSV files are annotated as pre_ and post_ to indicate that they were administered prior to and after the immersion. The CSV files are annotated as numerical_ and string_ to indicate the format of the scale values. Each participant is assigned a unique 5-character ID. |
| NASA_TLX |	None |	CSV	| Participant responses to the standard 21-tick NASA Task Load Index (TLX). Each participant is assigned a unique 5-character ID. |
| R_UCLA | None | CSV | Participant responses to the Revised UCLA Loneliness Scale (R-UCLA). Each participant is assigned a unique 5-character ID. |
| SPIN | None | CSV | Participant responses to the Social Phobia Inventory (SPIN). Each participant is assigned a unique 5-character ID. |
| STAI | None | CSV | Participant responses to the State Trait Anxiety Inventory (STAI). Each participant is assigned a unique 5-character ID. |
| SUS	| None |	CSV	| Participant responses to the standard System Usability Scale (SUS). Each participant is assigned a unique 5-character ID. |
| TreatmentResponses |	None |	CSV	| Participant responses to each treatment, i.e., being notified about the reason for the wait (With_Notification) or not being notified about the reason (Without_Notification). Participant responses include their time estimate for the wait in minutes, their frustration level on a 5-point Likert scale (1 being lowest and 5 highest), and their likelihood to exit on a 5-point Likert scale. Each participant is assigned a unique 5-character ID.
| VRData	| Yes	| CSV | Contains 36 subfolders that represents each participant. Each subfolder is named with the unique 5-character ID. Within each participant subfolder there are three additional subfolders named ParticipantID_NO_WAIT, ParticipantID_3_MINUTE_WAIT and ParticipantID_6_MINUTE_WAIT. Here Participant_ID is the unique 5-character ID and NO_WAIT, 3_MINUTE_WAIT and 6_MINUTE_WAIT are the wait conditions. Within the ParticipantID_NO_WAIT, ParticipantID_3_MINUTE_WAIT, and ParticipantID_6_MINUTE_WAIT subfolders are four CSV files for Eye Gaze (EyeGazeLog), Head Position and Orientation (HeadPosition), Left Hand (LeftHandLog), and Right Hand (RightHandLog). Thus, each participant has 12 CSV files. |

### Dataset Frame Rate Summary
The minimum (Min), maximum (Max), and average (Mean) frame rate for the head, eye gaze, right hand, and left hand for our dataset are provided below.  

| Treatment | Type of Data | Min | Max | Mean | SD |
| ----- | ----- | ----- | ----- | ----- | ----- |
| NO_WAIT | Head | 49.52 | 71.55 | 67.81 | 3.42 |
| | Eye gaze | 49.36 | 70.83 | 67.65 | 3.46 |
| | Right hand | 49.52 | 71.55 | 67.81 | 3.42 |
| | Left hand | 49.52 | 71.55 | 67.81 | 3.42 |
| 3_MINUTE_WAIT | Head | 55.42 | 103.84 | 65.11 | 7.23 |
| | Eye gaze | 54.09 | 103.84 | 64.85 | 7.20 |
| | Right hand | 55.42 | 103.84 | 65.11 | 7.23 |
| | Left hand | 55.42 | 103.84 | 65.11 | 7.23 |
| 6_MINUTE_WAIT | Head | 55.18 | 71.69 | 60.91 | 3.32 |
| | Eye gaze | 55.18 | 71.67 | 60.70 | 3.94 |
| | Right hand | 55.18 | 71.69 | 60.92 | 3.32 |
| | Left hand | 55.18 | 71.69 | 60.92 | 3.32 |
