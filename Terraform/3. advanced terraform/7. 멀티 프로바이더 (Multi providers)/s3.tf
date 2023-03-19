# resource "aws_s3_bucket" "apne2" {
#   force_destroy = true
# }

# resource "aws_s3_bucket" "use1" {
#   provider      = aws.use1
#   force_destroy = true
# }

resource "aws_vpc" "apne2" {
  cidr_block = "10.3.0.0/16"
}

resource "aws_vpc" "use1" {
  cidr_block = "10.3.0.0/16"
  provider   = aws.use1
}