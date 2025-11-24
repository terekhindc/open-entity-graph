import json
import os
import sys

# Configuration: directory to scan
DATA_DIR = "./data"
REQUIRED_CONTEXT = "https://schema.org"

def validate_file(filepath):
    errors = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return [f"CRITICAL: Invalid JSON (syntax error): {str(e)}"]

    # Check if @graph is used
    if "@graph" in data:
        items = data["@graph"]
        # Context must be at the top level
        if data.get("@context") != REQUIRED_CONTEXT:
             errors.append("MISSING: Missing or invalid '@context' at top level (must be https://schema.org)")
    else:
        items = [data]

    for idx, item in enumerate(items):
        item_id = item.get("@id", "unknown_id")

        # 1. Check for @id (Critical for Linked Data)
        if "@id" not in item:
            errors.append(f"MISSING: Item #{idx} is missing '@id' field")
        
        # 2. Check for @type
        if "@type" not in item:
            errors.append(f"MISSING: Item #{idx} ({item_id}) is missing '@type' field")
            
        # 3. For single objects (no @graph), check context inside
        if "@graph" not in data and item.get("@context") != REQUIRED_CONTEXT:
            errors.append("MISSING: Missing or invalid '@context' (must be https://schema.org)")

        # 4. Check for 'subjectOf' (Verification Chain)
        # We check this only for main entities, not strictly for every nested offer
        main_types = ["Organization", "Person", "EventSeries", "ProfessionalService", "Product"]
        if item.get("@type") in main_types:
            if "subjectOf" not in item:
                 errors.append(f"WARNING: Entity '{item_id}' ({item.get('@type')}) is missing verification link 'subjectOf'")

    return errors

def main():
    has_errors = False
    print(f"🔍 Starting validation in folder: {DATA_DIR}...\n")

    for root, dirs, files in os.walk(DATA_DIR):
        for file in files:
            if file.endswith(".jsonld") or file.endswith(".json"):
                filepath = os.path.join(root, file)
                file_errors = validate_file(filepath)
                
                if file_errors:
                    has_errors = True
                    print(f"❌ ERROR in file {filepath}:")
                    for err in file_errors:
                        print(f"  - {err}")
                    print("-" * 40)
                else:
                    # Uncomment next line for verbose logging
                    # print(f"✅ OK: {filepath}")
                    pass

    if has_errors:
        print("\n⛔ VALIDATION FAILED. Fix the errors above.")
        sys.exit(1)
    else:
        print("\n✨ ALL FILES VALID. Great job!")
        sys.exit(0)

if __name__ == "__main__":
    main()