from pydantic import ValidationError
from main import InvoiceData

try:
    InvoiceData(total_amount=-100)
    print("Fail : negative amount accepted")

except ValidationError:
    print ("PASS : negative rejected")