variable "bucket_name" {
  description = "The name of the S3 bucket to create."
}

variable "function_name" {
  description = "The name of the Lambda function to create."
}

variable "role_name" {
  description = "The name of the IAM role to create for the Lambda function."
}

variable "environment" {
  description = "The environment tag to apply to the S3 bucket."
}
