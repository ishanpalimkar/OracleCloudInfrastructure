import oci
import requests

# Get the Instance Principals Security Token Signer
signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()

# Define the OCI Function endpoint URL
function_endpoint = "https://wn6qtwv6s4a.us-phoenix-1.functions.oci.oraclecloud.com/20181201/functions/ocid1.fnfunc.oc1.phx.aaaaaaaaq7kzj5yem2wlxpqrmzomm5yhv7hcjvpdkb6g3gijlsaup42fgnra/actions/invoke"

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
