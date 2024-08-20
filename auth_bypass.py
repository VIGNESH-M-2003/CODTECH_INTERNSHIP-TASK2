from utils import send_request, print_response

def test_auth_bypass(url):
    print("\n[+] Testing for Authentication Bypass...")

    common_usernames = ["admin", "administrator", "root"]
    common_passwords = ["admin", "password", "123456"]

    for username in common_usernames:
        for password in common_passwords:
            response = send_request(url, data={"username": username, "password": password})
            print(f"\nTesting with username: {username}, password: {password}")
            print_response(response)

            if "Login successful" in response.text:
                print("[!] Authentication Bypass Successful!")
                return

    print("[-] Authentication Bypass Failed.")

if __name__ == "__main__":
    target_url = "http://example.com/login"
    test_auth_bypass(target_url)
