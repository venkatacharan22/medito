<img width="1440" alt="image" src="https://github.com/user-attachments/assets/acc37e19-a14c-48d5-86f6-35cef4d40bc4" />
<img width="1440" alt="image" src="https://github.com/user-attachments/assets/9528030e-b5d7-4fcc-a7bf-a5554fee28e1" />
<img width="1423" alt="image" src="https://github.com/user-attachments/assets/ee5be622-eefc-4d1e-a042-015af8462551" />
# Medito - Meditation and Wellness Platform

A comprehensive web application that combines meditation resources, interactive features, and AI-powered chat assistance for mental wellness.

## Features

- **Animated Navigation Bar**: Modern and responsive navigation interface
- **Meditation Space**: Dedicated area for meditation with audio resources
- **Interactive Games**: Mental wellness games and activities
- **AI Chatbot**: Powered by Google's Gemini AI for wellness-related conversations
- **About Section**: Information about the platform and its purposes

## Prerequisites

- Python 3.7+
- Flask
- Google Generative AI library
- Modern web browser

## Installation

1. Clone the repository:
```bash
git clone https://github.com/venkatacharan22/medito.git
cd medito
```

2. Install required Python packages:
```bash
pip install flask google-generativeai python-dotenv
```

3. Set up environment variables:
Create a `.env` file in the project root and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```
Note: A default API key is provided in the code, but it's recommended to use your own.

## Running the Application

1. Start the Flask server:
```bash
python gemini_backend.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Project Structure

- `animated-navbar.html`: Main navigation interface
- `medspace.html`: Meditation space with audio resources
- `games.html`: Interactive wellness games
- `chatbot.html`: AI-powered chat interface
- `about.html`: Platform information
- `gemini_backend.py`: Flask backend with Gemini AI integration
- `med1.mp3`, `med2.mp3`: Meditation audio resources

## Usage

1. **Navigation**: Use the animated navbar to move between different sections
2. **Meditation**: Access meditation resources in the Meditation Space
3. **Games**: Engage with interactive wellness games
4. **Chat**: Interact with the AI chatbot for wellness-related queries
5. **About**: Learn more about the platform

## Contributing

Feel free to fork the repository and submit pull requests for any improvements.

## License

This project is open source and available under the MIT License.
