Machine Predictive Maintenance App

📋 Overview

This is a Machine Learning–based web application built using Streamlit that predicts the likelihood of machine failure based on input parameters such as air temperature, process temperature, rotational speed, torque, and tool wear.

It helps identify potential breakdowns early and improve maintenance planning to reduce downtime and costs.

⸻

⚙ Features

✅ User-friendly web interface using Streamlit
✅ Predicts machine failure probability instantly
✅ Clean design with customized colors
✅ Trained using real-world machine data (ai42020.csv)
✅ Simple and lightweight model deployment

⸻

🧩 Tech Stack
	•	Python 3.11+
	•	Streamlit for web interface
	•	pandas, NumPy, scikit-learn for ML model
	•	joblib for model serialization

  Input Parameters
  
  Parameter                Description
  Air Temperature          Ambient temperature around the machine
  Process Temperature      Internal process temperature
  Rotational Speed         Machine spindle speed in RPM
  Torque                   Load torque in Nm
  Tool Wear                Tool usage time in minutes

  How to run the project
  git clone https://github.com/mufeedhakallan-creator/machine-predictive-maintenance.git

  Navigate to the project folder
  cd machine-predictive-maintenance

  install required packages
  pip install -r requirements.txt

  run the streamlit app
  streamlit run app.py


  PROJECT STRUCTURE
  machine-predictive-maintenance/
│
├── ai42020.csv                # Dataset
├── app.py                     # Streamlit web app
├── trained_model.pkl          # Saved ML model
├── requirements.txt           # Required libraries
└── README.md                  # Project documentation

Interface Preview

A minimal, elegant Streamlit interface with custom background, button, and input field colors for a clean user experience.

⸻

💡 Future Improvements
	•	Add more machine parameters for better accuracy
	•	Integrate with Power BI or dashboards
	•	Deploy on cloud (Streamlit Cloud / AWS / Azure)

⸻

👩‍💻 Author

Mufeedha Kallan
Data Science Enthusiast | Machine Learning & Python Developer
