# Fashion MNIST Classifier Web App
This is a Streamlit web application for classifying Fashion MNIST images using a pre-trained CNN model.

## Model Training (Jupyter Notebook):
- Located in the model_training_Jupyter folder.
- Trains a Convolutional Neural Network (CNN) on the Fashion MNIST dataset to recognize clothing categories.
- The trained model is saved as trained_model.keras.

## Web App (Streamlit):
- Located in the app folder.
- Provides a user-friendly web interface to upload 28x28 grayscale images (PNG or JPG).
- Displays the uploaded image and predicts its fashion category using the pre-trained model.
- Shows the confidence score and handles errors for invalid images.
- Can be run locally or via Docker.

## Usage:
Set up a Python virtual environment and install dependencies.
Run the app with streamlit run app.py.
The app will be available at http://localhost:8501.

## Local Setup and Run
### Prerequisites
- Python 3.9 installed.
- Virtual environment tool (built-in with Python).

### Setup Virtual Environment
You can set up the virtual environment either in the root project folder for universal access and unified dependencies (sharing with the notebook) or app folder for isolation.

### Option 1: In the `root` project folder (Shared with notebook)
This option sets up the virtual environment in the root `.venv` folder.
This makes the environment accessible from both the root directory (e.g., for running the notebook) and the `app` subfolder.
1. Navigate to the root project folder:
   ```
   cd Image-Classification-Fashion-MNIST
   ```

2. Create a virtual environment in the `.venv` folder:
   ```
   python -m venv .venv
   ```
   - Note: If the process is interrupted or fails, delete the broken folder before retrying:
   ```
   Remove-Item -Recurse -Force .venv
   ```

3. Activate the virtual environment:
   - On Windows: Terminal Type: Command Prompt (CMD): `.venv\Scripts\activate`
   - On Windows: Terminal Type: PowerShell (PS): `.\.venv\Scripts\Activate.ps1`
   - On Git Bash / macOS / Linux: `source .venv/bin/activate`

4. Install dependencies:
   ```
   pip install -r app/requirements.txt
   ```

### Option 2: In the `app` folder (isolation)
This option sets up the virtual environment in the root `app` folder.
Use this setup to isolate the application from the training environment.
1. Navigate to the `app` folder:
   ```
   cd app
   ```

2. Create a virtual environment in the `.venv` folder:
   ```
   python -m venv .venv
   ```
   - Note: If the process is interrupted or fails, delete the broken folder before retrying:
   ```
   Remove-Item -Recurse -Force .venv
   ``` 

3. Activate the virtual environment:
   - On Windows: Terminal Type: Command Prompt (CMD): `.venv\Scripts\activate`
   - On Windows: Terminal Type: PowerShell (PS): `.\.venv\Scripts\Activate.ps1`
   - On Git Bash / macOS / Linux: `source .venv/bin/activate`

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Run Locally
Ensure you are at the appropriate location. (root project folder / app folder)
Ensure the virtual environment is activated.

#### Option 1: Virtual Environment in `root` project folder
1. Navigate to the root folder if not already there:
```
cd Image-Classification-Fashion-MNIST
```

2. Ensure the virtual environment is activated.
   - On Windows: Terminal Type: Command Prompt (CMD): `.venv\Scripts\activate`
   - On Windows: Terminal Type: PowerShell (PS): `.\.venv\Scripts\Activate.ps1`
   - On Git Bash / macOS / Linux: `source .venv/bin/activate`
   
3. Navigate to the `app` folder:
   ```
   cd app
   ```

4. Run the app:
   ```
   streamlit run main.py
   ```
   
5. Wait for browser or open your browser to `http://localhost:8501`.

#### Option 2: Virtual Environment in the `app` folder
1. Navigate to the app folder if not already there:
```
cd app
```

2. Ensure the virtual environment is activated.
   - On Windows: Terminal Type: Command Prompt (CMD): `.venv\Scripts\activate`
   - On Windows: Terminal Type: PowerShell (PS): `.\.venv\Scripts\Activate.ps1`
   - On Git Bash / macOS / Linux: `source .venv/bin/activate`

3. Run the app:
   ```
   streamlit run main.py
   ```

4. Wait for browser or Open your browser to `http://localhost:8501`.

## Docker Setup and Run
### Prerequisites
- Docker installed.

### Build and Run
1. Navigate to the `app` folder.
    ```
   cd Image-Classification-Fashion-MNIST\app
   ```

2. Ensure the virtual environment is activated.

   - On Windows: `.venv\Scripts\activate`
   - On macOS/Linux: `source .venv/bin/activate`

3. Ensure the Docker Desktop is activated.

4. Build the Docker image: (Skip this if Docker image have already been built once on your computer)
   ```
   docker build -t fashion-mnist-app .
   ```
5. Run the container:
   ```
   docker run -p 8501:8501 fashion-mnist-app
   ```
6. Open your browser to `http://localhost:8501`.
