# resource "aws_cloudtrail" "cloudtrail" {
#   name                       = "all-events"
#   s3_bucket_name             = aws_s3_bucket.this.id
#   is_multi_region_trail      = true
#   enable_log_file_validation = true
#   #   is_organization_trail = true

#   event_selector {
#     exclude_management_event_sources = ["kms.amazonaws.com", "rdsdata.amazonaws.com"]
#   }
# }

# resource "aws_s3_bucket" "this" {
#   bucket_prefix = "aws-cloudtrail-logs-${local.account_id}-"
#   force_destroy = true
# }

# resource "aws_s3_bucket_public_access_block" "this" {
#   bucket = aws_s3_bucket.this.id

#   block_public_acls       = true
#   block_public_policy     = true
#   ignore_public_acls      = true
#   restrict_public_buckets = true
# }

# resource "aws_s3_bucket_server_side_encryption_configuration" "this" {
#   bucket = aws_s3_bucket.this.bucket

#   rule {
#     apply_server_side_encryption_by_default {
#       sse_algorithm = "AES256"
#     }
#   }
# }

# resource "aws_s3_bucket_lifecycle_configuration" "s3_lifecycle" {
#   bucket = aws_s3_bucket.this.bucket

#   rule {
#     id = "cloudtrail-log"

#     expiration {
#       days                         = 365
#       expired_object_delete_marker = false
#     }

#     noncurrent_version_expiration {
#       noncurrent_days = 1
#     }

#     abort_incomplete_multipart_upload {
#       days_after_initiation = 1
#     }

#     status = "Enabled"
#   }
# }

# resource "aws_s3_bucket_policy" "s3_policy" {
#   bucket = aws_s3_bucket.this.id
#   policy = <<POLICY
# {
#     "Version": "2012-10-17",
#     "Statement": [
#         {
#             "Sid": "AWSCloudTrailAclCheck",
#             "Effect": "Allow",
#             "Principal": {
#               "Service": "cloudtrail.amazonaws.com"
#             },
#             "Action": "s3:GetBucketAcl",
#             "Resource": "${aws_s3_bucket.this.arn}"
#         },
#         {
#             "Sid": "AWSCloudTrailWrite",
#             "Effect": "Allow",
#             "Principal": {
#               "Service": "cloudtrail.amazonaws.com"
#             },
#             "Action": "s3:PutObject",
#             "Resource": "${aws_s3_bucket.this.arn}/AWSLogs/${local.account_id}/*",
#             "Condition": {
#                 "StringEquals": {
#                     "s3:x-amz-acl": "bucket-owner-full-control"
#                 }
#             }
#         }
#     ]
# }
# POLICY
# }

# resource "aws_s3_bucket_ownership_controls" "this" {
#   bucket = aws_s3_bucket.this.id

#   rule {
#     object_ownership = "BucketOwnerEnforced"
#   }
# }
