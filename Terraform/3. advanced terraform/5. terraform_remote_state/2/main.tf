provider "aws" {
  region = "ap-northeast-2"
}

data "terraform_remote_state" "this" {
  backend = "local"
  config = {
    path = "../1/terraform.tfstate"
  }
}

output "test" {
  value = data.terraform_remote_state.this.outputs.role_arn
}