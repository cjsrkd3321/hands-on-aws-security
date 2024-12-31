data "terraform_remote_state" "vpc" {
  backend = "s3"
  config = {
    bucket = "my-backend-s3-bucket-20241222111102706500000001"
    key    = "vpc/terraform.tfstate"
    region = "ap-northeast-2"
  }
}
