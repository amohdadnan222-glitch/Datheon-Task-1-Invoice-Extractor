from main import extract_invoice

try:
    extract_invoice("   ")
    print("FAIL : empty accepted")

except ValueError:
    print("PASS : rejected")