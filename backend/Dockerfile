# Use the official Python image as the base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt


# wait-for-it.sh スクリプトをコピーして実行権限を付与
# COPY wait-for-it.sh /app/wait-for-it.sh
# RUN chmod +x /app/wait-for-it.sh

# Netcat をインストール
RUN apt-get update && apt-get install -y netcat-openbsd

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Start the application
# CMD ["./wait-for-it.sh", "db:3306", "--", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["/app/wait-for-it.sh", "db", "3306", "--", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]