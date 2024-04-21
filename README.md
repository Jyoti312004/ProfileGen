# ProfileGen

ProfileGen is a web application that allows users to generate a professional profile based on their resume. It extracts relevant information from the resume, such as the candidate's name, contact information, education, work experience, and skills, and presents it in a user-friendly format.

## Features

- Resume Information Extraction: ProfileGen utilizes the PyPDF2 library to extract text from uploaded PDF resumes. It parses the text to extract key details, including the candidate's name, email, phone number, education, work experience, and skills.

- User Input Form: The application provides a user-friendly form for users to manually input their information, including name, email, phone number, education, work experience, and skills.

- Dashboard: Once the user submits their information, ProfileGen presents a dashboard that displays the extracted resume details or the user-submitted information in an organized manner.

## Installation

To run the ProfileGen application locally, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/keshav1sharma/ProfileGen.git
   ```

2. Navigate to the project directory:

   ```
   cd ProfileGen
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Run the application:

   ```
   python manage.py runserver
   ```

5. Access the application in your web browser at `http://localhost:8000`.

## Usage

1. Upload a Resume: On the homepage, you can upload your resume in PDF format. ProfileGen will extract the necessary details from the resume.

2. Fill in the Form: Alternatively, you can fill in the provided form fields with your personal information, including name, email, phone number, education, work experience, and skills.

3. View the Dashboard: After submitting your information, you will be redirected to the dashboard. It will display the extracted resume details or the information you provided in an organized manner.

## Technologies Used

- Python
- Django
- PyPDF2

## Contributions

Contributions to ProfileGen are welcome! If you have any ideas, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## License

ProfileGen is released under the [MIT License](LICENSE).

## Acknowledgments

- [PyPDF2](https://pythonhosted.org/PyPDF2/): A library for extracting text from PDF files.
- [Django](https://www.djangoproject.com/): A high-level Python web framework used to build the application.
- [Bootstrap](https://getbootstrap.com/): A popular CSS framework for creating responsive and visually appealing web pages.
