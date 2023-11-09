# Task: Sequence video verification
## Dataset: CSV
**Prompt**  

I want you to act as a professional annotator. You need to generate the question-and-answer pair data to train the model based on the provided data. I will give you the image sampled from the video or the image caption or video summary of this video and the original labels. All the information that the answer needs is contained in the label files. Please remember you are a professional annotator and finish your work as required. Do not consider to briefly generate your output.

There are some rules you need to obey:  

### 1）For generating questions based on the provided image:

- Basic setting: The generated question should showcase this information: you are provided a video about something and need try to understand what happened this video. 
- Basic setting: When generating questions and answers, ensure that the framing implies that the person responding to the question has actual, direct access to the video. The questions should be phrased in a way that assumes the respondent is analyzing real footage, not imagining or guessing. The answers should reflect a clear and detailed understanding of the video's content, as if the respondent is describing what they are directly observing in the video.
    - For example:
        - Incorrect Approach: "Imagine you are watching a video, what happened in it?"
        - Correct Approach: "Watched the provided video, can you describe the sequence of actions that occurred?"
    - ensures that the generated Q&A pairs are based on the premise that the person being questioned is responding based on direct observation of the video, not on imagination or hypothetical scenarios.

- Question Type: It could be a judgment question, essay question, or any other specified format.
  - If you want to create judgement question. Please ensure the response is No or Yes with the same probability.  Note that the probability of each response, i.e. Yes's and No's, should be equal and balanced, so ensure a balance in question devising.
- Contextual Background: Craft a background story that provides a context to the scene depicted in the image. This might involve describing the setting, the time, the atmosphere, or any relevant details that set the stage.

- Motivation: Explain the motivation or reason behind the question. For instance, begin with an introduction explaining the scenario or situation, then delve into why this particular question is being asked. Further, indicate what one hopes to achieve or understand by getting the answer.

- Activity Description: Describe the activities or events taking place in the video, but avoid direct mentions of the exact action being performed.

- Variety in Storytelling: Ensure a diverse range of background stories. Repeating the same story or context should be avoided.

- Diversity in Format: The generated questions and answers should come in a variety of formats and narratives to cater to different interpretations of the video.

- The scene information in the video: 
    - Depicts a collection of laboratory equipment meticulously arranged for scientific experiments. Numerous small cylindrical containers with white caps suggest storage for samples. A ceramic mortar and pestle are evident, designed for grinding or mixing. Various clear glass apparatuses, including flasks, beakers, and test tubes, are spread across the scene, some filled with distinct colored solutions. An eye-catching yellow test tube rack holds several test tubes with varied solutions. Dropper bottles of different shapes, some with colored contents, are interspersed throughout the setting. The display also features syringes, stoppers,  glass rods, transparent tubes and straws of varying lengths. Other notable items include a plastic funnel alongside a folded material, flexible hoses, and an iron stand equipped with clamps. There's an assortment of other small items that might be integral to specific experiments. 

    - This detailed inventory may not capture every single item present in the video; thus, attention should also be given to elements not explicitly mentioned in this description.

### 2） For generating answer:
Based on the annotation, video and original answer:
- First of all, you need to generate the standard original answer based on the annotations of this video for the original question.
- Following the generated question by you, you need to write many details. Examine the provided image carefully based on the supplied photograph or image caption. Describe the scene in great detail, focusing on the primary action. 
- Additionally, elaborate on the potential context or background story that could explain the circumstances leading up to this moment.
     
### 3） the generated results:
- Ensure Variety: While maintaining continuity, make sure each pair is unique and captures different aspects of the source materials.
- Maintain Clarity: Despite the number of pairs, each question and answer should be clear, concise, and relevant to the source materials.
- Reliability： Do not ask any question that cannot be answered confidently.
- Accuracy: Do not omit the key information when generating the answer.

### 4） the output format:

- First of all， please use JSON format to reply to me.
- Please follow this format to give the final result. Generate 10 continuous question-answer pairs based on the video annotations,  video scene information ,images, and associated captions or video summaries. Do not include any interjected notes, disclaimers, or extraneous information. Simply produce the pairs consecutively. Do not pause, add notes, disclaimers, or any other commentary. Just provide 10 uninterrupted Q&A pairs.

    ```json
    {
        "1":{
            "Original question": "This is the question provided by me or generated by you",
            "Original answer": "This is the answer you created based on the annotation and the original question",
            "The question with details": "Your generated question, elaborated in depth, which should adhere to the requirements and incorporate more narrative or motivation elements",
            "The answer with details": "Your answer, expanded and detailed, elaborated in depth, which should offer a comprehensive understanding by explaining the context, reasons, scene knowledge, action motivations, or other pertinent information.",
        },
        "2":{},
        ...
        "10":{},
    }

    ```
Keep note that 5 Q&A pairs are needed.
Now I am providing you with specific details about the Q&A pairs you need to generate.


If you understand my requirements, please tell me, and then I will send you a set of data which are the first question, an image or only image caption, the original question, and the original simple answer. When you finish the annotation generation, I will give your new data with new question to do this task again.


---  
- Question 1.1: 
    - Objective: Generate questions and answers from the provided action sequence annotations, images, image captions, or video summaries. Ensure that questions accurately capture the actions or events depicted.
        -  Based on the video's annotations, generate a detailed question-and-answer pair. The question should delve into the specifics of the actions happening in the video, probing for a deeper understanding of each action and their sequence. The answer should provide a comprehensive description of every action, elucidating the order in which they occur.
        -  Refrain from using identifiers like "1.2" or "1.3" in your answers. Instead, refer to them as "the first video" or "the second video".
        - Subject Selection:
            - The subject of the question can be any reasonable role that fits the context of the video. Examples include but are not limited to: "instructor", "student", "boy".
            - Feel free to change or vary the subject across different question-and-answer pairs.
        - The output format：
            - Note using the given JSON template to return the generation result.
        - The generated question: you could change the framework of question without changing the benchmark's meaning.
    - Output(provided by you):
        ```json
        {
            "1":{
            "Original question": "This is the question provided by me or generated by you",
            "Original answer": "This is the answer you created based on the annotation and the original question",
            "The question with details": "Your generated question, elaborated in depth, which should adhere to the requirements and incorporate more narrative or motivation elements",
            "The answer with details": "Your answer, expanded and detailed, elaborated in depth, which should offer a comprehensive understanding by explaining the context, reasons, scene knowledge, action motivations, or other pertinent information.",
            },
            "2":{},
            ...
            "8":{},
        },

        ```    
    
    - Original question: What are the actions depicted in the video sequence, and in what specific order do they occur?
    - Original simple answer: The actions, as described in the video annotations, occur in a particular sequence. Below is the JSON format representation of these actions:
    ```json
    "1.2":[
        "take up the test paper",
        "tear the test paper",
        "put down the test paper",
        "put down the test paper",
        "take up the glass rod",
        "point the glass rod to evaporating dish",
        "point the glass rod to test paper",
        "put down the glass rod",
        "take up the tweezer",
        "clamp the tweezer",
        "put down the test paper",
        "put down the tweezer"
    ],
    ```

- Question 1.2: 
    - Objective: Generate questions and answers from the provided action sequence annotations, images, image captions, or video summaries. Ensure that questions accurately capture the actions or events depicted.
        -  Your task is to generate insightful questions and answers based on the provided action sequence annotations, images, image captions, or video summaries. The goal is to accurately capture and elaborate on the actions or events depicted in the video.
        - Base your question on the video's annotations. It should delve into the specifics of the actions occurring in the video, aiming for a deeper understanding of each action and their sequence.
        -  Refrain from using identifiers like "1.2" or "1.3" in your answers. Instead, refer to them as "the first video" or "the second video".
        - Subject Selection:
            - The subject of the question can be any reasonable role that fits the context of the video. Examples include but are not limited to: "instructor", "student", "boy".
            - Feel free to change or vary the subject across different question-and-answer pairs.
        - The output format：
            - Note using the given JSON template to return the generation result.
        - The generated question: you could change the framework of question without changing the benchmark's meaning.
  
    - Output(provided by you):
    ```json
    {
        "1":{
        "Original question": "This is the question provided by me or generated by you",
        "Original answer": "This is the answer you created based on the annotation and the original question",
        "The question with details": "Your generated question, elaborated in depth, which should adhere to the requirements and incorporate more narrative or motivation elements",
        "The answer with details": "Your answer, expanded and detailed, elaborated in depth, which should offer a comprehensive understanding by explaining the context, reasons, scene knowledge, action motivations, or other pertinent information.",
        },
        "2":{},
        ...
        "5":{},
    },

    ```    
    - Original question: your designed question.
    - Original simple answer: As shown in JSON, it is the annotations of this video, that describe the action occurring sequence.
        ```json
        "1.2":[
            "take up the test paper",
            "tear the test paper",
            "put down the test paper",
            "put down the test paper",
            "take up the glass rod",
            "point the glass rod to evaporating dish",
            "point the glass rod to test paper",
            "put down the glass rod",
            "take up the tweezer",
            "clamp the tweezer",
            "put down the test paper",
            "put down the tweezer"
        ],
        ```
- Question 1.3: 
    - Objective: Generate questions and answers from the provided action sequence annotations, images, image captions, or video summaries. Ensure that questions accurately capture the actions or events depicted.
        - sample question: How do the actions in the first video sequence differ from those in the second?
        - Sample Answer: 
            - First Video: [Description of events/actions in the first video],Second Video: [Description of events/actions in the second video]. Comparison: The two videos have several similarities and differences. [Specific differences and similarities between the two videos are highlighted here.]
    - Output(provided by you):
        ```json
        {
            "1":{
            "Original question": "This is the question provided by me or generated by you",
            "Original answer": "This is the answer you created based on the annotation and the original question",
            "The question with details": "Your generated question, elaborated in depth, which should adhere to the requirements and incorporate more narrative or motivation elements",
            "The answer with details": "Your answer, expanded and detailed, elaborated in depth, which should offer a comprehensive understanding by explaining the context, reasons, scene knowledge, action motivations, or other pertinent information.",
            },
            "2":{},
            ...
            "5":{},
        },

        ```    
        
    - Original question: your designed question.
    - Original simple answer: As shown in JSON, they are the annotations of these two video, that describe the action occurring sequence.
    ```json
    "1.2":[
        "take up the test paper",
        "tear the test paper",
        "put down the test paper",
        "put down the test paper",
        "take up the glass rod",
        "point the glass rod to evaporating dish",
        "point the glass rod to test paper",
        "put down the glass rod",
        "take up the tweezer",
        "clamp the tweezer",
        "put down the test paper",
        "put down the tweezer"
    ],
    ```json
    "1.3":[
        "take up the test paper",
        "tear the test paper",
        "put down the test paper",
        "put down the test paper",
        "take up the glass rod",
        "clamp the tweezer",
        "put down the test paper",
        "put down the tweezer"
    ],
    ```
- Question 1.4: 
    - Objective: Generate questions and answers from the provided action sequence annotations, images, image captions, or video summaries. Questions should accurately reflect the depicted actions or described events. 
        - new rules：
            - Refrain from using identifiers like "1.2" or "1.3" in your answers. Instead, refer to them as "the first video" or "the second video".
            - Elaborate on every action in each video in as much detail as possible.
        ample Question: How do the actions in the first video sequence differ from those in the second?↳
        - Sample Question: How do the actions in the first video sequence differ from those in the second?
        - Sample Answer:
            - First Video: The subject begins by picking up the test paper, then proceeds to tear it. After tearing, the paper is set down twice consecutively. Following this, a glass rod is picked up, and it's pointed towards an evaporating dish and then at the test paper. Later, the rod is set aside. The subject subsequently picks up a tweezer, clamps it, and finally sets down the test paper and tweezer in succession.
            - Second Video: The subject in this video also starts by picking up and tearing the test paper, setting it down twice afterward. They then pick up a glass rod, but instead of pointing it, they directly move on to clamp a tweezer. The sequence concludes with the test paper and tweezer being set down.
    - Output(provided by you):
        ```json
        {
            "1":{
            "Original question": "This is the question provided by me or generated by you",
            "Original answer": "This is the answer you created based on the annotation and the original question",
            "The question with details": "Your generated question, elaborated in depth, which should adhere to the requirements and incorporate more narrative or motivation elements",
            "The answer with details": "Your answer, expanded and detailed, elaborated in depth, which should offer a comprehensive understanding by explaining the context, reasons, scene knowledge, action motivations, or other pertinent information.",
            },
            "2":{},
            ...
            "5":{},
        },

        ```    
    - Original question: your designed question.
    - Original simple answer: As shown in JSON, they are the annotations of these two video, that describe the action occurring sequence.
    ```json
    "1.2":[
        "take up the test paper",
        "tear the test paper",
        "put down the test paper",
        "put down the test paper",
        "take up the glass rod",
        "point the glass rod to evaporating dish",
        "point the glass rod to test paper",
        "put down the glass rod",
        "take up the tweezer",
        "clamp the tweezer",
        "put down the test paper",
        "put down the tweezer"
    ],
    ```json
    "1.3":[
        "take up the test paper",
        "tear the test paper",
        "put down the test paper",
        "put down the test paper",
        "take up the glass rod",
        "clamp the tweezer",
        "put down the test paper",
        "put down the tweezer"
    ],
    ```



- Question 2.1 : 
     - Objective: Create questions and answers based on you've provided the action sequences annotations, images, image's captions, or video summaries extracted from the original video. Questions should accurately reflect the depicted actions or described events. Answers should be limited to "Yes" or "No".
        - Refrain from using identifiers like "1.2" or "1.3" in your answers. Instead, refer to them as "the first video" or "the second video
        - Subject Selection: 
            - The subject of the question can be any reasonable role that fits the context of the video. Examples include but are not limited to: "instructor", "lab assistant", "student", "chemist", "researcher".
            - Feel free to change or vary the subject across different question-and-answer pairs.
        - Action Selection: 
            - Choose two or more actions from the provided action sequence list. When choosing repetitive actions, make sure to provide clarity by adding slight variations or contexts.
        - Temporal Relationship: 
            - Integrate temporal relationships among the chosen actions in the question, such as "before", "after", "while", "until", "and then", etc.
            - Ensure clarity in the sequence, especially when the number of actions exceeds two
        - Flexibility: Frame the question in any manner that best captures the essence of the chosen actions and their sequence. Examples:
            - "After doing [action A], did the [chosen subject] proceed to [action B]?"
            - "In the video, was [action A] followed by [action B] and then [action C] by the [chosen subject]?"
            - "Did the sequence involve the [chosen subject] first doing [action A], and later [action B]?"
        - Answer: The answer should be either "Yes" or "No". Please ensure the response is No or Yes with the same probability. Note that the probability of each response, i.e. Yes's and No's, should be equal and balanced, so ensure a balance in question devising.
    - Output(provided by you):
        ```json
        {
            "1":{
            "Original question": "This is the question provided by me or generated by you",
            "Original answer": "This is the answer you created based on the annotation and the original question",
            "The question with details": "Your generated question, elaborated in depth, which should adhere to the requirements and incorporate more narrative or motivation elements",
            "The answer with details": "Your answer, expanded and detailed, elaborated in depth, which should offer a comprehensive understanding by explaining the context, reasons, scene knowledge, action motivations, or other pertinent information.",
            },
            "2":{},
            ...
            "5":{},
        },

        ```    
    - Original question and answer:
        - Original question: your designed judgment question.
        - Original simple answer: As shown in JSON, it is the annotations of this video, that describe the action occurring sequence.
            ```json
            "1.2":[
                "take up the test tube",
                "take up the iron clamp",
                "screw the iron clamp",
                "screw the iron clamp",
                "take up the conical flask",
                "pour the conical flask",
                "put down the conical flask"
            ],
            ```


- Question 2.2 : 
    - Objective: Create questions and answers based on you've provided the action sequences annotations, images, image's captions, or video summaries extracted from the original video. Questions should accurately reflect the depicted actions or described events. 
        - Refrain from using identifiers like "1.2" or "1.3" in your answers. Instead, refer to them as "the first video" or "the second video
        - Subject Selection: 
            - The subject of the question can be any reasonable role that fits the context of the video. Examples include but are not limited to: "instructor", "lab assistant", "student", "chemist", "researcher".
            - Feel free to change or vary the subject across different question-and-answer pairs.
        - Action Selection: 
            - You could choose two or more actions from the provided action sequence list. When choosing repetitive actions, make sure to provide clarity by adding slight variations or contexts.
            - You also could choose or create related action based on your knowledge, scene information, or others. But you need to ensure the generated action phrase is reasonable.
        - Temporal Relationship: 
            - Integrate temporal relationships among the chosen actions in the question, such as "before", "after", "while", "until", "and then", etc.
            - Ensure clarity in the sequence, especially when the number of actions exceeds two
        - Flexibility: Frame the question in any manner that best captures the essence of the chosen actions and their sequence. Examples:
            - "After doing [action A], did the [chosen subject] proceed to [action B]?"
            - "In the video, was [action A] followed by [action B] and then [action C] by the [chosen subject]?"
            - "Did the sequence involve the [chosen subject] first doing [action A], and later [action B]?"
        - Answer: 
            - Answer: The answer should be either "Yes" or "No". Please ensure the response is No or Yes with the same probability. Note that the probability of each response, i.e. Yes's and No's, should be equal and balanced, so ensure a balance in question devising.

    - Output(provided by you):
        ```json
        {
            "1":{
            "Original question": "This is the question provided by me or generated by you",
            "Original answer": "This is the answer you created based on the annotation and the original question",
            "The question with details": "Your generated question, elaborated in depth, which should adhere to the requirements and incorporate more narrative or motivation elements",
            "The answer with details": "Your answer, expanded and detailed, elaborated in depth, which should offer a comprehensive understanding by explaining the context, reasons, scene knowledge, action motivations, or other pertinent information.",
            },
            "2":{},
            ...
            "5":{},
        },

        ```    
    - Original question and answer:
        - Original question: your designed question.
        - Original simple answer: As shown in JSON, it is the annotations of this video, that describe the action occurring sequence.
            ```json
            "1.2":[
                "take up the test tube",
                "take up the iron clamp",
                "screw the iron clamp",
                "screw the iron clamp",
                "take up the conical flask",
                "pour the conical flask",
                "put down the conical flask"
            ],
            ```

- Question 3: 
    - Objective: Create questions and answers based on you've provided the action sequences annotations, images, image's captions, or video summaries extracted from the original video. Questions should accurately reflect the depicted actions or described events. 
        - Action Selection:
            Opt for actions from the given annotations or devise ones based on your understanding, but ensure they align with the scene's context.

    - Output(provided by you):
        ```json
        {
            "1":{
            "Original question": "This is the question provided by me or generated by you",
            "Original answer": "This is the answer you created based on the annotation and the original question",
            "The question with details": "Your generated question, elaborated in depth, which should adhere to the requirements and incorporate more narrative or motivation elements",
            "The answer with details": "Your answer, expanded and detailed, elaborated in depth, which should offer a comprehensive understanding by explaining the context, reasons, scene knowledge, action motivations, or other pertinent information.",
            },
            "2":{},
            ...
            "5":{},
        },

        ```    
    - Original question: Frame a question about the sequence of actions, such as [action], [action], ... , and [action].
    - Original simple answer: As shown in json, it is the annotations of this video, which describes  the action occurring sequence.
        ```json
        "1.2":[
            "take up the test tube",
            "take up the iron clamp",
            "screw the iron clamp",
            "screw the iron clamp",
            "take up the conical flask",
            "pour the conical flask",
            "put down the conical flask"
        ],
        ```

- Question 4:
    - Objective: This question aims to facilitate a benchmark test. Using the provided two videos, benchmark data, and evaluation metrics, create questions and answers. Your inquiries should precisely capture the benchmark's essence, displayed actions, and described events.
        - Refrain from using identifiers like "1.2" or "1.3" in your answers. Instead, refer to them as "the first video" or "the second video".
        - Benchmark: The benchmark consists of numerous video pairs. Each pair encompasses two videos, either showcasing similar actions or identical action sequences. The central challenge is distinguishing between two analogous videos.
        - Evaluation metric:  
            ```latex
            During inference, we apply the method that distinguishes positive pairs from negative pairs to evaluate the quality of learned video representations. Specifically in this paper, we calculate the normalized Euclidean distance between two video representations $v_1$ and $v_2$ in the same video pair:
                \begin{equation}
                    d = dis(v_1,v_2)  \\
                \end{equation}
                \vspace{-10pt}
                \begin{equation}
                    y=\begin{cases}
                    1, d \leq \tau \\
                    0, otherwise \\
                    \end{cases}
                \label{eq:logist}
                \end{equation}
                where $dis(.,.)$ means the $\ell2$-normalization Euclidean distance function. $\tau$ is a threshold to decide whether the sequences are consistent. $y = 1$ means the two sequences of videos are consistent, otherwise inconsistent.
            ```
        - Subject Selection:
            - The subject of the question can be any reasonable role that fits the context of the video. Examples include but are not limited to: "instructor", "student", "boy".
            - Feel free to change or vary the subject across different question-and-answer pairs.
        - The output format：
            - Note using the given JSON template to return the generation result.
        - The generated question: you could change the framework of question without changing the benchmark's meaning.
        - The generated answer: Provide a confidence score ranging from 0.0 to 1.0 based on a "Yes" or "No" answer. If the two videos share the exact same action sequence, assign a confidence score of 1.0. However, if there is any difference in action between the two videos, the confidence score should be 0.0, indicating no similarity in the action sequences. This score quantifies your certainty about the similarity or dissimilarity of the actions in both videos.
    - Output(provided by you):
        ```json
        {
            "1":{
            "Original question": "Do these two videos showcase the same action sequence?",
            "Original answer": "Provide a confidence score without any additional commentary",
            "The question with details": "Your generated question, elaborated in depth, which should adhere to the requirements and incorporate more narrative or motivation elements",
            "The answer with details": "Your answer, expanded and detailed, elaborated in depth, which should offer a comprehensive understanding by explaining the context, reasons, scene knowledge, action motivations, or other pertinent information.",
            },
            "2":{},
            ...
            "5":{},
        },

        ```    
    - Original question: Do these two videos showcase the same action sequence?
    - Original simple answer:  Provide a confidence score without any additional commentary. As shown in JSON, they are the annotations of these two videos, that describe the action occurring sequence. 
        - video 1
            ```json
            "1.2":[
                "take up the test tube",
                "take up the iron clamp",
                "screw the iron clamp",
                "screw the iron clamp",
                "take up the conical flask",
                "pour the conical flask",
                "put down the conical flask"
            ],
            ```
        - video 2
            ```json
            "1.2":[
                "take up the test tube",
                "take up the iron clamp",
                "screw the iron clamp",
                "screw the iron clamp",
                "take up the conical flask",
                "pour the conical flask",
                "put down the conical flask"
            ],
            ```
