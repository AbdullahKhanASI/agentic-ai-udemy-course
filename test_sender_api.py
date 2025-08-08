import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)

def test_sender_api():
    """Test the Sender API with proper debugging"""
    
    # Get environment variables
    api_token = os.environ.get('SENDER_API_TOKEN')
    from_email = os.environ.get('SENDER_FROM_EMAIL')
    to_email = os.environ.get('SENDER_TO_EMAIL')
    
    print("=== Environment Check ===")
    print(f"API Token: {'✓ Set' if api_token else '✗ Missing'}")
    print(f"From Email: {from_email or '✗ Missing'}")
    print(f"To Email: {to_email or '✗ Missing'}")
    print()
    
    if not all([api_token, from_email, to_email]):
        print("❌ Missing required environment variables")
        return
    
    # Prepare the request
    payload = {
        "from": {"email": from_email, "name": "Test Sender"},
        "to": [{"email": to_email, "name": "Test Recipient"}],
        "subject": "API Test Email",
        "text": "This is a test email from the API",
        "html": "<p>This is a <b>test email</b> from the API</p>",
    }

    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    print("=== API Request ===")
    print(f"URL: https://api.sender.net/v2/transactional")
    print(f"Headers: {headers}")
    print(f"Payload: {payload}")
    print()
    
    try:
        # Make the API call
        response = requests.post(
            "https://api.sender.net/v2/transactional", 
            json=payload, 
            headers=headers, 
            timeout=30
        )
        
        print("=== API Response ===")
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        print(f"Content Type: {response.headers.get('content-type', 'unknown')}")
        print()
        
        # Check if we got HTML (documentation page) or JSON
        content_type = response.headers.get('content-type', '')
        if 'html' in content_type.lower():
            print("❌ Received HTML response (likely redirected to docs)")
            print("First 500 characters of response:")
            print(response.text[:500])
        elif 'json' in content_type.lower():
            print("✅ Received JSON response")
            try:
                json_data = response.json()
                print("Response JSON:", json_data)
            except Exception as e:
                print(f"Error parsing JSON: {e}")
                print("Raw response:", response.text)
        else:
            print("❓ Unknown response type")
            print("Raw response:", response.text[:500])
            
        if response.status_code == 200 or response.status_code == 202:
            print("✅ Email sent successfully!")
        else:
            print(f"❌ API returned error status: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")

if __name__ == "__main__":
    test_sender_api()