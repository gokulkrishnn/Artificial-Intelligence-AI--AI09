from dotenv import load_dotenv
import os
import sys
import time
import requests
import json

def main():
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        # Get the business card
        image_file = 'biz-card-1.png'
        if len(sys.argv) > 1:
            image_file = sys.argv[1]

        # Get config settings
        load_dotenv()
        ai_svc_endpoint = os.getenv('ENDPOINT')
        ai_svc_key = os.getenv('KEY')
        analyzer = os.getenv('ANALYZER_NAME')

        # Analyze the business card
        analyze_card(image_file, analyzer, ai_svc_endpoint, ai_svc_key)

        print("\n")

    except Exception as ex:
        print(ex)

def analyze_card(image_file, analyzer, endpoint, key):
    # Use Content Understanding to analyze the image
    print(f"Analyzing {image_file}")

    # Set the API version
    CU_VERSION = "2025-05-01-preview"

    # Read the image data
    with open(image_file, "rb") as file:
        image_data = file.read()

    # Use a POST request to submit the image data to the analyzer
    print("Submitting request...")
    headers = {
        "Ocp-Apim-Subscription-Key": key,
        "Content-Type": "application/octet-stream"
    }
    url = f'{endpoint}/contentunderstanding/analyzers/{analyzer}:analyze?api-version={CU_VERSION}'
    response = requests.post(url, headers=headers, data=image_data)

    # Get the response and extract the ID assigned to the analysis operation
    print(response.status_code)
    response_json = response.json()
    id_value = response_json.get("id")

    if not id_value:
        print("No ID returned for analysis.")
        return

    # Use a GET request to check the status of the analysis operation
    print('Getting results...')
    time.sleep(1)
    result_url = f'{endpoint}/contentunderstanding/analyzerResults/{id_value}?api-version={CU_VERSION}'
    result_response = requests.get(result_url, headers=headers)
    print(result_response.status_code)

    # Keep polling until the analysis is complete
    status = result_response.json().get("status")
    while status == "Running":
        time.sleep(1)
        result_response = requests.get(result_url, headers=headers)
        status = result_response.json().get("status")

    # Process the analysis results
    if status == "Succeeded":
        print("Analysis succeeded:\n")
        result_json = result_response.json()
        output_file = "results.json"
        
        # Save the result to a file
        with open(output_file, "w") as json_file:
            json.dump(result_json, json_file, indent=4)
        print(f"Response saved in {output_file}\n")

        # Iterate through the fields and extract the names and type-specific values
        contents = result_json.get("result", {}).get("contents", [])
        for content in contents:
            if "fields" in content:
                fields = content["fields"]
                for field_name, field_data in fields.items():
                    field_type = field_data.get('type')
                    if field_type == "string":
                        print(f"{field_name}: {field_data.get('valueString')}")
                    elif field_type == "number":
                        print(f"{field_name}: {field_data.get('valueNumber')}")
                    elif field_type == "integer":
                        print(f"{field_name}: {field_data.get('valueInteger')}")
                    elif field_type == "date":
                        print(f"{field_name}: {field_data.get('valueDate')}")
                    elif field_type == "time":
                        print(f"{field_name}: {field_data.get('valueTime')}")
                    elif field_type == "array":
                        print(f"{field_name}: {field_data.get('valueArray')}")
    else:
        print("Analysis failed.")
        print(result_response.json())

if __name__ == "__main__":
    main()
