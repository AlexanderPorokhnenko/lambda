<h2><b>Lambda function, which collect facts about cats and store in S3</b></h2>
<p>To install Lambda function, package should be created and deployed on AWS.</p>

### Deployment
1. cd /path-to-project
2. pip install --target ./package -r requirements.txt
3. cd package 
zip -r ../my_deployment_package.zip .
4. cd ..
zip my_deployment_package.zip lambda_function.py
5. Load zip-file to AWS Lambda.
6. Specify event values in format:
   ```json
   { "bucket_name": "bucket_name",
  "filename": "output_filename.csv"}
   ```
7. Execute function.

