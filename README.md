MedScript-OCR 🩺📝
Deciphering Medical Prescriptions with Lightweight AI

MedScript-OCR is a lightweight handwriting recognition system designed to address a major challenge in healthcare: illegible medical prescriptions. It simulates a Convolutional Neural Network (CNN) pipeline to interpret messy cursive handwriting and map it to a verified medical lexicon—enhancing patient safety and clinical efficiency.

📌 The Problem

Handwritten prescriptions in fast-paced clinical environments often lead to:

Medication Errors: Misreading drug names or dosages
Time Delays: Manual verification by pharmacists and staff
OCR Limitations: Traditional OCR systems fail on cursive and medical shorthand
💡 The Solution

MedScript-OCR delivers a low-latency, high-accuracy solution that runs locally without relying on heavy cloud infrastructure. It is optimized for:

Clinics with limited internet access
Environments requiring high data privacy
Edge deployment in healthcare settings

🚀 Key Features
CNN-Inspired Processing Pipeline: Simulates vision-based AI using layered image processing
Medical Lexicon Matching: Maps detected patterns to validated drug names
Human-in-the-Loop Verification: Ensures accuracy through manual confirmation
Pure Python Implementation: Zero external dependencies for maximum compatibility

🛠 System Architecture
The system operates through a structured 4-stage pipeline:
Pre-processing
Converts input images into high-contrast grayscale to highlight ink patterns
Noise Reduction
Applies filters to remove background noise and distortions
Segmentation
Detects and separates connected handwritten characters
Classification
Matches extracted features with entries in the MEDICAL_LEXICON

💻 Installation & Usage
Requirements
Python 3.6 or above
No additional libraries required
Steps to Run
git clone https://github.com/your-username/MedScript-OCR.git
cd MedScript-OCR
python main.py
How It Works
Input a prescription image (e.g., sample_note.png)
Follow terminal prompts
Review and verify suggested outputs

🔮 Future Enhancements
OpenCV integration for real-time image processing
Integration with global drug databases (e.g., WHO)
Mobile interface for bedside usage

⚖️ Ethics & Data Privacy
Fully Local Processing: No data is transmitted externally
Assistive Tool Only: Designed to support—not replace—medical professionals

👩‍💻 Author
Palak Priya
B.Tech – Computer Science (Health Informatics)
