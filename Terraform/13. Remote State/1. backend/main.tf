resource "aws_s3_bucket" "this" {
  bucket_prefix = "my-backend-s3-bucket-"
  force_destroy = true # 실무에선 사용 X
}

resource "aws_s3_bucket_versioning" "this" {
  bucket = aws_s3_bucket.this.id
  versioning_configuration {
    status = "Enabled"
  }
}

output "bucket_name" {
  value = aws_s3_bucket.this.bucket
}
