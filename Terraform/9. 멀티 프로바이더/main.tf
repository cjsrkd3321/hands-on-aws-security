provider "aws" {
  region = "us-east-1"
}

resource "aws_vpc" "use1" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "use1-dynamic-block-vpc"
  }
}

provider "aws" {
  region = "ap-northeast-2"
  alias  = "apne2"
}

# 멀티 프로바이더 사용 시,
# provider를 꼭!! 확인할 것
# 배포 후 변경하면 상태가 덮어씌워져서 비정상 동작 가능!
# terraform destroy -target=aws_vpc.apne2
resource "aws_vpc" "apne2" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "apne2-dynamic-block-vpc"
  }

  provider = aws.apne2
}
