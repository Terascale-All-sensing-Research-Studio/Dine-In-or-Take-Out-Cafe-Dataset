# Assets

Our study consisted of four treatments: 
1.  No wait for maître d' with No wait for food (coded as 00): In this treatment, the participant engages in dialogue with a virtual maître d'. The folder [00_03_Audio_Files](https://github.com/Terascale-All-sensing-Research-Studio/VR-Social-Isolation-Cafe/blob/main/Assets/00_03_Audio_Files) contains all the audio assets in MP3 format for the 00 treatment.
2.	No wait for maître d' with 3-minute wait for food (coded as 03): In this treatment, the participant engages in dialogue with a virtual maître d'. The folder [00_03_Audio_Files](https://github.com/Terascale-All-sensing-Research-Studio/VR-Social-Isolation-Cafe/blob/main/Assets/00_03_Audio_Files) contains all the audio assets in MP3 format for the 03 treatment.
3.  3-minute wait for maître d' with No wait for food (coded as 30): In this treatment, the participant engages in dialogue with a virtual maître d', after they are informed to wait. The folder [30_33_Audio_Files](https://github.com/Terascale-All-sensing-Research-Studio/VR-Social-Isolation-Cafe/blob/main/Assets/30_33_Audio_Files) contains all the audio assets in MP3 format for the 30 treatment.
4.  3-minute wait for maître d' with 3-minute wait for food (coded as 33): In this treatment, the participant engages in dialogue with a virtual maître d', after they are informed to wait. The folder [30_33_Audio_Files](https://github.com/Terascale-All-sensing-Research-Studio/VR-Social-Isolation-Cafe/blob/main/Assets/30_33_Audio_Files) contains all the audio assets in MP3 format for the 33 treatment.

We provide the differences in the audio assets used in each treatment below. **Present** indicates that the audio asset is used in the treatment and **Absent** indicates that the audio asset is not used in the treatment. 

| Audio Asset Name | 00 | 03 | 30 | 33 |
| ----------------------------| ----------------- | --------------------- |--------------------- |--------------------- |
| WithYouShortly.mp3 | Absent | Absent | Present | Present |
| Welcome.mp3 | Present | Present | Present | Present |
| WelcomeLoop.mp3 | Present | Present | Present | Present |
| OkRightThisWay.mp3 | Present | Present | Present | Present |
| WillStandingTableWork.mp3 | Present | Present | Present | Present |
| WillTakeoutWork.mp3 | Present | Present | Present | Present |
| Sorry.mp3 | Present | Present | Present | Present |
| FemaleBackgroundConvo.mp3 | Present | Present | Present | Present |
| TrimmedCafeAmbientNoise.mp3 | Present | Present | Present | Present |

We provide the timing of when each audio asset is used in each treatment. We provide the time as Minute:Second format. **Absent** indicates that the audio asset is not used in the treatment. **(variable)** indicates that the event can occur at different time instances depending on when the participant approaches the maître d' NPC, what dialogue options they choose, or if they choose to approach a female customer NPC. **N/A** indicates that an audio asset is not used as it represents a specific event such as the start of the simulation or end of the simulation. 
 
| Time (Minute:Second) | Event | Audio Asset Name 00 and 03 | Audio Asset Name 30 and 33 |
| -------------------- | ----- | ---------------------------------- | ------------------------------------- |
| 0:00 | Participant spawned into simulation | TrimmedCafeAmbientNoise.mp3 | TrimmedCafeAmbientNoise.mp3 |
| (variable) When participant reaches NPC maître d' | NPC maître d' says: "I will be with you shortly." | Absent | WithYouShortly.mp3 |
| (variable) When participant reaches NPC maître d' | NPC maître d' says: "Hello, welcome to Flavor and Vine. Would you like to dine in or take out?" | Welcome.mp3 | Welcome.mp3 | 
| (variable) Upon selecting "Dine In" | NPC maître d' says: "Unfortunately, we only have standing tables available right now. Will that work for you?" | WillStandingTableWork.mp3 | WillStandingTableWork.mp3 | 
| (variable) Upon selecting "Take Out"	| NPC maître d' says: "Ok, right this way." | OkRightThisWay.mp3 | OkRightThisWay.mp3 | 
| (variable) Upon selecting "Yes Standing Table" | NPC maître d' says: "Ok, right this way." | OkRightThisWay.mp3 | OkRightThisWay.mp3 | 
| (variable) Upon selecting "No Standing Table"	| NPC maître d' says: "Ok, will take out be ok for you?" | WillTakeoutWork.mp3 | WillTakeoutWork.mp3 | 
| (variable) Upon selecting "Yes Take Out" | NPC maître d' says: "Ok, right this way." | OkRightThisWay.mp3 | OkRightThisWay.mp3 |
| (variable) Upon selecting "No Take Out" | NPC maître d' says: "Sorry about that." | Sorry.mp3 | Sorry.mp3 |
| (variable) If participant reaches within vicinity of NPC Female40s | NPC Female40s says: "I hope we see Emily before the holidays, we had such a great time at the beach last time. By the way, how is your deal at the office going, hopefully you can close by next month. I am so hungry I can't wait for the wait staff." in a loop | FemaleBackgroundConvo.mp3 | FemaleBackgroundConvo.mp3 | 
| (variable) Upon selecting a menu option | End Simulation | N/A | N/A |