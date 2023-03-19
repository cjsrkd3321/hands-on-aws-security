provider "aws" {
  region = "ap-northeast-2"
}

provider "aws" {
  alias  = "use1"
  region = "us-east-1"
}
