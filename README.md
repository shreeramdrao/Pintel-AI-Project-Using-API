
# Data Extraction and Risk Analysis using OpenAI API

## Project Overview:
This project crawls and extracts data from an SEC report using Python. The extracted sections are cleaned and stored in a structured format (list of dictionaries). Additionally, it uses the OpenAI API to analyze a specific section (e.g., "risk") to identify 3-5 potential risks the company might face and extracts important phrases.

## Project Structure:
- **pintel_ai_task.py**: The main Python script containing the code for data extraction and risk analysis using OpenAI API.
- **requirements.txt**: Contains all the dependencies required for the project.
- **README.md**: Instructions for running the project.

## Installation Instructions:
1. Clone the repository or download the zip folder:
    ```bash
    git clone <repo_link> OR download the zip file
    ```

2. Navigate to the project directory:
    ```bash
    cd <project_directory>
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Get your OpenAI API Key:
    - Visit the [OpenAI API website](https://beta.openai.com/signup/) to get your API key.
    - Replace `'your-openai-api-key'` in the code with your actual API key.

## Running the Script:
1. Run the script:
    ```bash
    python pintel_ai_task.py
    ```

2. Expected Output:
    - The extracted sections and their cleaned content will be printed.
    - The potential risks for the selected section will be printed (using OpenAI API).
    - Important phrases will be extracted from the selected section.

## Notes:
- Ensure that you have a valid OpenAI API key before running the code.
- The extracted sections and their content can be further processed as per your specific needs.
