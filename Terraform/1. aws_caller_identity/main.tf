# hashicorp에서 직접 관리하는 provider는 별도 provider 명시하지 않아도,
# 기본 설정을 참고하여 추정 후 동작함. 당연히 명시적으로 기재하는 것이 좋음.
# 참고: https://developer.hashicorp.com/terraform/language/v1.1.x/providers/configuration
provider "aws" {
  region = "ap-northeast-2"
}

data "aws_caller_identity" "current" {}

output "test" {
  value = data.aws_caller_identity.current.account_id
}
