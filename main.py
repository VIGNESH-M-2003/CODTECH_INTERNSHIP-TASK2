import sql_injection
import xss
import auth_bypass

if __name__ == "__main__":
    # Target URLs
    target_sql_injection_url = "http://example.com/login"
    target_xss_url = "http://example.com/search"
    target_auth_bypass_url = "http://example.com/login"
    
    # Parameters for SQL Injection and XSS
    sql_injection_params = {"username": "admin", "password": "password"}
    xss_params = {"query": "test"}

    # Perform the tests
    sql_injection.test_sql_injection(target_sql_injection_url, sql_injection_params)
    xss.test_xss(target_xss_url, xss_params)
    auth_bypass.test_auth_bypass(target_auth_bypass_url)
