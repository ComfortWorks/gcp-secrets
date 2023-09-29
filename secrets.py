from google.cloud import secretmanager
import os
import requests
#from settings import GCP_PROJECT_ID, currentSubdomain, user, pwd, branch


def loadSecret(secret):
	try:
		GCP_PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
		if not GCP_PROJECT_ID:
			GCP_PROJECT_ID = requests.get("http://metadata.google.internal/computeMetadata/v1/project/project-id")
		name = f"projects/{GCP_PROJECT_ID}/secrets/{secret}/versions/latest"
		print("project:" + name)
		client = secretmanager.SecretManagerServiceClient()
		account = client.access_secret_version(request={"name":name}).payload.data.decode("UTF-8")
		#print(account)
		#print(type(account))
		#return client.access_secret_version(request={"name":name}).payload.data.decode("UTF-8")
		return account
	except Exception as e:
		print(e)
		return None


def getSecret(secretName):
	return loadSecret(secretName)

"""
def serviceAccount():
	return loadSecret("serviceAccount")
	
def googleProject():
	return loadSecret("googleProject")
	
def shopifyApiCred():
	return loadSecret("shopifyApiCred")
	
def myshopifySubdomain():
	return loadSecret("myshopifySubdomain")
"""
	

