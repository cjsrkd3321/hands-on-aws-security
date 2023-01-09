data "aws_caller_identity" "me" {}

data "http" "myip" {
  url = "http://ipv4.icanhazip.com"
}

module "s3" {
  source          = "./s3"
  name            = "rex-chun-s3-bucket-with-security-policy"
  src_public_ips  = ["${data.http.myip.body}/32"]
  src_private_ips = []
  principal_arns  = [data.aws_caller_identity.me.arn]
}