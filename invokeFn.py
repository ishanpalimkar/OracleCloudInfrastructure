import oci
import requests

# Using the boilder plate function deployed in OCI FN

# Get the Instance Principals Security Token Signer
signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()

# Define the OCI Function endpoint URL
function_endpoint = "https://<your_function_endpoint>"

# Define the request payload
payload = {
    "name": "World"
}

# Make the POST request to the OCI Function endpoint
response = requests.post(
    url=function_endpoint,
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json"
    },
    json=payload,
    auth=signer
)

# Print the response
print(response.status_code)
print(response.text)
