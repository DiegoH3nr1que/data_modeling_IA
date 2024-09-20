import json
import requests
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

NGROK_URL = "(NGROK_LINK FREE APP)"

def query_ollama(prompt):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False  
    }
    try:
        response = requests.post(f"{NGROK_URL}/api/generate", headers=headers, json=data, stream=True)
        response.raise_for_status()
        
        full_response = ""
        for line in response.iter_lines(decode_unicode=True):
            if line:
                try:
                    json_response = json.loads(line)
                    if 'response' in json_response:
                        full_response += json_response['response']
                except json.JSONDecodeError as e:
                    logging.error(f"Failed to decode JSON line: {e}")
                    logging.error(f"Problematic line: {line}")
        
        logging.debug(f"Full response: {full_response}")
        return full_response
    except requests.RequestException as e:
        logging.error(f"Request failed: {e}")
        return f"Error making request: {e}"

def generate_data_model(input_data):
    prompt = f"""
    Given the following data structure:
    {input_data}
    
    Generate a data model that represents this structure efficiently. 
    Include table names, column names, data types, and relationships.
    Return the result as a JSON string.
    """
    return query_ollama(prompt)

def optimize_data_structure(current_model):
    prompt = f"""
    Given the following data model:
    {current_model}
    
    Identify any redundancies or inefficiencies in the structure.
    Suggest improvements to optimize the model.
    Return the result as a JSON string with "suggestions" and "optimized_model" keys.
    """
    return query_ollama(prompt)

def adapt_to_changes(current_model, new_requirements):
    prompt = f"""
    Given the current data model:
    {current_model}
    
    And the new requirements:
    {new_requirements}
    
    Adapt the model to incorporate these changes.
    Return the updated model as a JSON string.
    """
    return query_ollama(prompt)

def main():
    while True:
        print("\nAI Data Modeling Tool")
        print("1. Generate Data Model")
        print("2. Optimize Data Structure")
        print("3. Adapt to Changes")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            input_data = input("Enter your data structure (e.g., JSON or description): ")
            result = generate_data_model(input_data)
            print("Generated Data Model:")
            print(result)
        
        elif choice == '2':
            current_model = input("Enter your current data model: ")
            result = optimize_data_structure(current_model)
            print("Optimization Suggestions:")
            print(result)
        
        elif choice == '3':
            current_model = input("Enter your current data model: ")
            new_requirements = input("Enter new requirements: ")
            result = adapt_to_changes(current_model, new_requirements)
            print("Updated Data Model:")
            print(result)
        
        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()