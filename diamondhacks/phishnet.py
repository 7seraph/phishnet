import kagglehub
import pandas as pd

# Download latest version
path = kagglehub.dataset_download("naserabdullahalam/phishing-email-dataset")

#print("Path to dataset files:", path)

df = 