from app.main import app

# Check if the run.py file has executed directly and not imported
# Statement starts the Flask server on your local machine
if __name__ == "__main__":
    app.run(debug=True)

#http://127.0.0.1:5000/api/synthetictable