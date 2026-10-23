import os
import json

from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, Field, ValidationError

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is missing from .env")

print ("API key Successfull")

client = genai.Client(api_key=api_key)
print("Successfull")

class InvoiceData(BaseModel):
    invoice_number: str | None=None
    customer_name: str | None=None
    invoice_date: str | None=None
    total_amount: float | None= Field(default=None, ge=0)
    currency: str | None=None
    payment_status: str | None=None


PROMPT_TEMPLATE = """
You are an information extraction assistant.

Extract the following information from the invoice text:
- Invoice number
- Customer name
- Invoice date
- Total amount
- Currency
- Payment status

Rules:
1. Extract only information supported by the invoice.
2. Do not invent missing information.
3. Use null for missing or unknown values.
4. Return only valid JSON.
5. Format the date as YYYY-MM-DD when possible.

Invoice text:
{invoice_text}
"""


def extract_invoice(invoice_text: str) -> InvoiceData:
    if not invoice_text.strip():
        raise ValueError("Invoice text cannot be empty.")

    prompt = PROMPT_TEMPLATE.format(invoice_text=invoice_text)

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": InvoiceData,
        },
    )

    if not response.text:
        raise ValueError("The AI model Returned an empty response.")

    invoice = InvoiceData.model_validate_json(response.text)

    return invoice
 


if __name__ == "__main__":
    sample_invoice = """
    Invoice number: INV-101
    Customer Name: Adnan
    Date: 15 October 2026
    Total Amount: INR 5000
    Payment Status: Paid    
    """

    result = extract_invoice(sample_invoice)

    print("\nExtracted Invoice Data:")
    print(json.dumps(result.model_dump(), indent=4, ensure_ascii=False))



