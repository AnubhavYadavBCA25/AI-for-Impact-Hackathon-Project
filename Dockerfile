# Step 1: Use an official Python runtime as the base image
FROM python:3.12

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the requirements.txt file to the container
COPY requirements.txt /app/

# Step 4: Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the application code to the container
COPY . /app/

# Step 6: Expose the port on which Streamlit runs (default: 8501)
EXPOSE 8501

# Step 7: Command to run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

