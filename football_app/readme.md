# Football Logo Guessing Game

This is a simple Django-based football logo guessing game.

## Setup

Follow these steps to set up and run the game on your local machine:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/MBoyadzhiev/guess_the_logo.git
   cd football_app
Create and Activate a Virtual Environment

If you don't have Python's venv installed, you can install it using:

bash
Copy code
python -m venv football_env
Activate the virtual environment:

On Windows:

bash
Copy code
.\football_env\Scripts\activate
On macOS and Linux:

bash
Copy code
source football_env/bin/activate
Install Dependencies

Install the required packages from the requirements.txt file:

bash
Copy code
pip install -r requirements.txt
Run Migrations

Apply the database migrations:

bash
Copy code
python manage.py migrate
Start the Development Server

Start the Django development server:

bash
Copy code
python manage.py runserver
The site will be available at http://localhost:8000/.

Play the Game

Open your web browser and visit http://localhost:8000 to play the game.

Credits
This project uses the Football Data API for team information.

License
This project is licensed under the MIT License.

Author
Martin Boyadzhiev

Feedback and Issues
If you have feedback or encounter any issues while using this application, please create an issue on the GitHub repository.