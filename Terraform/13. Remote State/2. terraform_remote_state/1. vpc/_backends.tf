# https://developer.hashicorp.com/terraform/language/backend
terraform {
  backend "s3" {
    bucket = "my-backend-s3-bucket-20241222111102706500000001"
    key    = "vpc/terraform.tfstate" # 보통은 폴더 구조에 따라 구성함
    region = "ap-northeast-2"
  }
}
