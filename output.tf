output "s3_bucket_id" {
  value = aws_s3_bucket.s3_bucket.id
}

output "lambda_function_arn" {
  value = aws_lambda_function.lambda_function.arn
}
