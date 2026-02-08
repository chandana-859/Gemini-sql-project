# SQL Query Generator with Google Gemini AI

This project is a simple web-based application that converts natural language questions into SQL queries using Google's Generative AI (Gemini). The app is built using **Streamlit** for the frontend and **SQLite** for the backend database. Users can input a question in plain English, and the AI model will generate the corresponding SQL query to fetch data from a student database.

## Project Overview

This project leverages Google Gemini AI to generate SQL queries dynamically from natural language inputs. The queries are executed on an SQLite database that contains student records such as names, classes, sections, marks, and ages.

![txt to sql](https://github.com/user-attachments/assets/1756442a-5400-4a64-8e2d-564d049aba42)



### Features:
- Converts natural language questions into SQL queries.
- Executes SQL queries on an SQLite database.
- Displays query results directly on the webpage.
- Simple UI built with Streamlit for ease of use.

### Technologies Used:
- **Python**: Main programming language for the project.
- **Streamlit**: For building the web interface.
- **Google Generative AI (Gemini)**: To convert natural language into SQL queries.
- **SQLite**: Local database for storing student records.
- **dotenv**: For loading environment variables securely.

## How to Run the Project

### Prerequisites:
- Python 3.x
- An API key for Google Gemini (Google's Generative AI)
- Streamlit installed (`pip install streamlit`)
- SQLite installed

### Installation:
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

3. Create a .env file in the root directory and add your Google API key:
    ```makefile
    GOOGLE_API_KEY=your-google-api-key-here

4. Set up the SQLite database by running the sql.py script:
    ```bash
    python sql.py

5. Run the Streamlit app:
    ```bash
    streamlit run app.py

6. Open your browser and navigate to the provided local address (e.g., `http://localhost:8501/`).

## Project Files


### `app.py`

This file contains the core logic of the project:
* It loads environment variables using dotenv to securely manage API keys.
* Uses Streamlit to build the web interface.
* Interacts with Google Gemini AI to convert English questions into SQL queries.
* Executes the generated SQL queries against the SQLite database to retrieve student data.
* Displays the generated SQL query and the results directly in the web application.


### `sql.py`

This script sets up the SQLite database (student.db) with a table called STUDENT. The table contains the following columns:
* `NAME`: The name of the student.
* `CLASS`: The class the student is enrolled in.
* `SECTION`: The section of the student.
* `MARKS`: The marks obtained by the student.
* `AGE`: The student's age.

It inserts sample records of students with Nepali names, simulating a real-world student database. It also prints the inserted records to the console for verification.

### Example Student Records:
Some of the student records that are pre-inserted into the database:
* `Puja` (Computer Science, Section A, 88 Marks, 21 years old)
* `Amit` (Computer Science, Section B, 74 Marks, 23 years old)
* `Sunita` (Business Management, Section A, 79 Marks, 22 years old)
* `Rajesh` (Economics, Section A, 68 Marks, 25 years old)
* And more...

### Example Usage

Once the app is running, you can input questions like:
* "Who scored the highest marks in Computer Science?"
* "Show me all students in section A."
* "How many students are there in the database?"

The app will generate the appropriate SQL queries for you and display the results fetched from the student.db database.

### Project Structure

```bash
.
├── app.py          # Main application file (Streamlit and AI interaction)
├── sql.py          # SQLite database setup script
├── requirements.txt # List of Python dependencies
├── .env             # Environment file for API keys (not included in repo)
└── README.md        # Documentation (this file)
```
### Future Improvements

Add more detailed error handling for invalid queries.
Enhance the UI for better user interaction and experience.
Expand the database with more student records or additional fields.

### Acknowledgments

Special thanks to Krishnayak YouTube Channel for providing valuable tutorials and inspiration that helped in building this project. You can check out the channel for more awesome content on Python, machine learning, and AI.
