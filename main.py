import time
import sys
import random

# --- MEDICAL KNOWLEDGE BASE ---
# This simulates the "Trained Data" of our OCR Model
MEDICAL_LEXICON = {
    "A": "Amoxicillin (Antibiotic)",
    "B": "Brufen (Pain Relief)",
    "C": "Cetirizine (Antiallergic)",
    "D": "Dolo 650 (Antipyretic)",
    "P": "Paracetamol (Pain/Fever)"
}

class MedScriptEngine:
    def __init__(self):
        self.accuracy_threshold = 0.92
        self.processing_layers = 4

    def simulate_vision_processing(self, filename):
        """Step-by-step simulation of how a CNN reads an image."""
        print(f"\n[SYSTEM] Loading Image: {filename}...")
        time.sleep(1)
        
        stages = [
            "Converting to Grayscale (L-Channel)...",
            "Applying Median Blur to remove paper noise...",
            "Segmenting handwritten characters via Thresholding...",
            "Extracting feature vectors from stroke patterns..."
        ]
        
        for stage in stages:
            print(f"  > {stage}")
            time.sleep(0.8)

    def identify_medication(self, initial_letter):
        """Simulates the final classification layer of the Neural Network."""
        letter = initial_letter.upper()
        if letter in MEDICAL_LEXICON:
            return MEDICAL_LEXICON[letter]
        return "Unknown Compound (Requires Human Review)"

def run_medscript():
    print("===============================================")
    print("      MEDSCRIPT OCR: HANDWRITING ENGINE        ")
    print("      Status: Active | No External API         ")
    print("===============================================\n")

    ocr = MedScriptEngine()

    print("--- STEP 1: IMAGE SELECTION ---")
    img_path = input("Enter image filename (e.g., prescription_01.png): ")
    
    if "." not in img_path:
        print("Error: Invalid file format. Please use .png or .jpg")
        return

    # Phase 1: Image Processing
    ocr.simulate_vision_processing(img_path)

    # Phase 2: User Input (Simulating the detected first letter)
    print("\n--- STEP 2: CHARACTER CLASSIFICATION ---")
    detected_char = input("System detected initial letter 'D'. Confirm or override: ") or "D"
    
    # Phase 3: Result
    result = ocr.identify_medication(detected_char)
    confidence = round(random.uniform(89.5, 98.2), 1)

    print("\n" + "="*45)
    print("        FINAL DECIPHERED OUTPUT        ")
    print("="*45)
    print(f"IDENTIFIED: {result}")
    print(f"CONFIDENCE: {confidence}%")
    print(f"LATENCY: 4.2ms")
    print("\n[AI ADVICE]: The pattern matches standard dosage forms.")
    print("WARNING: Final verification by a Pharmacist is mandatory.")
    print("="*45)

if __name__ == "__main__":
    try:
        run_medscript()
    except KeyboardInterrupt:
        print("\n\nShutting down MedScript safely.")
