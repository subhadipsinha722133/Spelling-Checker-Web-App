# Spelling Checker Web App 📝
A simple and intuitive web application built with Streamlit and pyspellchecker to help you find and correct spelling mistakes in your text.

🚀 Features
Real-time Spell Check: Instantly identifies misspelled words in the input text.

Correction Suggestions: Provides a list of potential corrections for each misspelled word.

Simple Interface: Easy-to-use interface powered by Streamlit for a smooth user experience.

Word Highlighting: Highlights incorrect words to make them easy to spot.

## 🚀 Try the App Live

🖥️ **Streamlit Dashboard**  
🔗 [Live Demo](https://spelling-checker-web-app-zn4e2jvtejpacmpvynuwar.streamlit.app/)  

# 🛠️ Technologies Used
- Streamlit: The core framework for building the interactive web application.

- pyspellchecker: The library used for the spelling correction logic.

- Python 3: The programming language used for the project.


![Accuracy](https://github.com/subhadipsinha722133/Spelling-Checker-Web-App/blob/main/webpage_img)
![Accuracy](https://github.com/subhadipsinha722133/Spelling-Checker-Web-App/blob/main/wevpage_img2.png)



# ⚙️ Setup and Installation
To run this project locally, follow these steps:

- 1. Clone the repository:

git clone https://github.com/subhadipsinha722133/Spelling-Checker-Web-App.git
cd Spelling-Checker-Web-App

- 2. Create and activate a virtual environment (recommended):

# For Windows
    python -m venv venv
    .\venv\Scripts\activate
    
 # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

- 3. Install the required dependencies:
Make sure you have a requirements.txt file with the following content:

streamlit
pyspellchecker

Then, run the installation command:

pip install -r requirements.txt

- 4. Run the Streamlit application:

streamlit run app.py

(Assuming your main Python script is named app.py)

The application should now be open and running in your web browser!

# 📖 How to Use
Enter Text: Type or paste the text you want to check into the text area on the web app.

Check Spelling: Click the "Check Spelling" button to process the text.

View Results: The application will display the original text with any misspelled words highlighted.

Get Suggestions: A list of misspelled words and their suggested corrections will be shown below the text.
