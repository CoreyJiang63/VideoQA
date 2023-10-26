# Task: Video Sequence Verification

## Dataset Format: CSV

- Objective: Generate a set of detailed question-answer pairs based on provided images, image captions, or video summaries. Your output will aid in training our model. All necessary information for crafting the answers is available in the label files.

### Instructions:

#### 1. Crafting Questions based on Images:
    - Question Type: Define the type, such as judgment, essay, etc.
    - Context: Create a backstory for the image scene, including setting, time, and atmosphere.
    - Motivation: Introduce the scenario and reason for the question. Describe what you aim to clarify or achieve through the answer.
    - Activity Description: Describe the activities in the image without directly stating the actions.
        - Variety: Ensure diverse background stories and avoid repetition.
        - Format Diversity: Produce questions and answers in varied formats to cater to multiple image interpretations.

#### 2. Crafting Answers:
    - Base Answer: Generate the foundational answer using the video's annotations.
    - Detailed Answer: Examine the provided image or caption, then describe the scene, focusing on primary actions. Further, provide context or backstory explaining the event's circumstances.

#### 3. Consistency and Clarity:
    - Variety: Ensure diverse yet continuous question-answer pairs.
    - Clarity: Every pair should be lucid, concise, and relevant.

#### 4. Output Formatting:
    - Provide the output in JSON format.
    - Produce 10 sequential question-answer pairs without interjected notes or extraneous details.

    - Output JSON Structure:  

        ```json
        {
            "1": {
                "Original question": "...",
                "Original answer": "...",
                "Detailed question": "...",
                "Detailed answer": "..."
            },
            ...
            "10": {}
        }
        ```

### Example:

Input:
    - Original question: What actions occurred in the sequence video?
    - Original answer:
        ```json
        "1.2":[
            "take up the test tube",
            ...
            "put down the conical flask"
        ]
        ```

Output:
    ```json
    {
        "1": {
            "Original question": "...",
            "Original answer": "...",
            "Detailed question": "...",
            "Detailed answer": "..."
        },
        ...
        "10": {}
    }
    ```

Once you understand these requirements, let me know, and I'll provide the initial dataset for annotation generation.
