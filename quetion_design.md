# Sequence Verification
## COIN
- Burger making (fUjz_eiIX8k 79.9)
  - General
    - Frame locating, extracting gist
      - What was the **first 10 seconds** [\TP] of the video about?
        - A: Introduction to the video clip. / The header of this instruction clip.
      - What is the video about?
        - A: Making a burger.

    - Sequence Extraction and Verification
      - How many steps were there in total **to make a burger** [\VP] as is shown in the clip?
        - A: Three.
      - How many steps do you reckon the YouTuber did **when she fried the meat** [\TP]?
        - A: Two.
    
    - Temporal Relation
      - Did the instructor **fry meat** [\VP] **before building her burger** [\TP]?
        - A: Yes.
      - What did the YouTuber do **after meat frying** [\TP]?
        - A: Combining meat and bread to make burger.
    
    - Action Segmentation
      - Could you tell me each of the step the YouTuber did in this video clip?
        - When did each step start and end?
      - A1: Just follow the label bank.
        - A2: Need further annotation. (Hardest)
    - Similar Video Query
      - Did the clip **YxajdZyFMIo** show the same sequence steps as is in this clip?
        - A: Yes. Same procedures, fry -> fry -> combine.

  - Scene Specific
    - How many **layers** [\NP] were there in total **in this homemade burger** [\SP]?
      - Detail understanding, key frame extraction
      - A: Five. Need information out of annotation.
  
    - What did **the YouTuber** [\NP] do right **before building up his burger** [\VP]?
      - Temporal relation
      - A: Meat frying. / Frying. / Frying meat.


- SIM card insertion (_2Sj5abMtqY 141.6)
  - General
    - Sequence Extraction and Verification
      - How many steps were there in total **to insert a SIM card** [\VP] as is shown in the clip?
        - A: Five.
      - How many times did the YouTuber **press the SIM card slot back** [\VP]?
        - A: Two.

    - Temporal Relation
      - Did the instructor **put the SIM card into the SIM card slot** [\VP] **before pressing the SIM card slot back** [\TP]?
        - A: Yes.
      - What did the YouTuber do **after using the needle to open the SIM card slot** [\TP]?
        - A: Putting the SIM card into the SIM card slot.

    - Action Segmentation
      - Could you tell me each of the step the YouTuber did in this video clip?
        - When did each step start and end?
      - A1: Just follow the label bank.
        - A2: Need further annotation. (Hardest)

    - Similar Video Query
      - Did the clip **x82uHFqRbkc**(141.4) show the same sequence steps as is in this clip?
        - A: No. One more putting the SIM card into the SIM card slot before final pressing the SIM 
    
    - Gist Extraction
      - What is the video about?
        - A: SIM card insertion. / Inserting SIM card.


## CSV
- Scene specific
  - Entity interaction, Temporal relation
    - What did **the experiment operator** [\E] put down **after he put down the glass rod** [\TP]?
      - A: The beaker.
    - Did **the experiment operator** [\E] take up *the glass rod* **before taking up the beaker** [\TP]?
      - A: The beaker.


## Diving
- Scene specific
  - Sequence verification, classification, temporal localization
    - What was the start pose of the athlete?
      - A: Back
    - Could tell me the pose code when the athlete was in the air?
      - A: "25som", "15Twis"
    - What was the ending pose of the athlete when she entered the water?
      - A: PIKE
    - How many postures did the athlete perform in the air?
      - A: Two.
  - Extracting key info, generalization
    - What was this video about? / How could you describe the video clip?
      - A: Diving.

## RepCount
- Classification, generalization
  - What sport was the athlete doing in this video clip?
    - A: Pull up.
- Frame locating
  - When did the athlete start doing the sport in the video? / How long was the introduction (header)?
    - A: Frame 77 / Second xxxx.
- Verification, counting
  - How many times did the athlete do this sport in total?
    - A: Six times.
- Discontinuity / Noise identification
  - Was there any discontinuity in this clip? If so, please locate the break.
    - A: There should be no discontinuity here.
  - Did the cameraman change the recording angle during this video?
    - A: Need further annotation.

