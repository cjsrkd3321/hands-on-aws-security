resource "aws_s3_bucket" "this" {
  bucket = var.name
  force_destroy = true
}

resource "aws_s3_bucket_public_access_block" "this" {
  bucket = aws_s3_bucket.this.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "this" {
  bucket = aws_s3_bucket.this.bucket

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}
resource "aws_s3_bucket_versioning" "this" {
  bucket = aws_s3_bucket.this.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_ownership_controls" "this" {
  bucket = aws_s3_bucket.this.id

  rule {
    object_ownership = "BucketOwnerEnforced"
  }
}

resource "aws_s3_bucket_policy" "this" {
  bucket = aws_s3_bucket.this.id
  policy = data.aws_iam_policy_document.this.json
}

data "aws_iam_policy_document" "default" {
  statement {
    sid    = "BucketOwnerFullControl"
    effect = "Deny"

    principals {
      type        = "*"
      identifiers = ["*"]
    }

    actions = [
      "s3:PutObject",
    ]

    resources = [
      "${aws_s3_bucket.this.arn}/*",
    ]

    # 버킷 소유자에게 모든 권한 부여하는거 아니면 거부
    # Grant or deny all rights to the bucket owner.
    condition {
      test     = "StringNotEquals"
      variable = "s3:x-amz-acl"
      values   = ["bucket-owner-full-control"]
    }
  }

  statement {
    sid    = "SecureTransport"
    effect = "Deny"

    principals {
      type        = "*"
      identifiers = ["*"]
    }

    actions = [
      "s3:*",
    ]

    resources = [
      aws_s3_bucket.this.arn,
      "${aws_s3_bucket.this.arn}/*",
    ]

    # HTTPS 아니면 거부
    # HTTPS or Reject
    condition {
      test     = "Bool"
      variable = "aws:SecureTransport"
      values   = ["false"]
    }
  }

  statement {
    sid    = "TlsVersion1.2"
    effect = "Deny"

    principals {
      type        = "*"
      identifiers = ["*"]
    }

    actions = [
      "s3:*",
    ]

    resources = [
      aws_s3_bucket.this.arn,
      "${aws_s3_bucket.this.arn}/*",
    ]

    # TLS 버전 1.2 미만 거부
    # Reject below TLS version 1.2
    condition {
      test     = "NumericLessThan"
      variable = "s3:TlsVersion"
      values   = ["1.2"]
    }
  }

  # 실제 접근 가능한 사용자 정의
  # Customize real-world accessible
  statement {
    sid    = "PrincipalArns"
    effect = "Deny"

    principals {
      type        = "*"
      identifiers = ["*"]
    }

    actions = [
      "s3:GetObject",
      "s3:PutObject",
      "s3:DeleteObject",
      # "s3:ListBucket"
    ]

    resources = [
      #   aws_s3_bucket.this.arn,
      "${aws_s3_bucket.this.arn}/*",
    ]

    condition {
      test     = "ArnNotEqualsIfExists"
      variable = "aws:PrincipalArn"
      values   = var.principal_arns
    }

    condition {
      test = "BoolIfExists"
      variable = "aws:PrincipalIsAWSService"
      values   = ["false"]
    }

    condition {
      test = "BoolIfExists"
      variable = "aws:ViaAWSService"
      values   = ["false"]
    }
  }

  # UserId
  statement {
    sid    = "UserIds"
    effect = "Deny"

    principals {
      type        = "*"
      identifiers = ["*"]
    }

    actions = [
      "s3:GetObject",
      "s3:PutObject",
      "s3:DeleteObject",
      # "s3:ListBucket"
    ]

    resources = [
      #   aws_s3_bucket.this.arn,
      "${aws_s3_bucket.this.arn}/*",
    ]

    condition {
      test     = "StringNotEquals"
      variable = "aws:userid"
      values   = var.user_ids
    }

    condition {
      test = "BoolIfExists"
      variable = "aws:PrincipalIsAWSService"
      values   = ["false"]
    }

    condition {
      test = "BoolIfExists"
      variable = "aws:ViaAWSService"
      values   = ["false"]
    }
  }

    # 공인 IP 및 사설 IP 제한
    # Restrictions on Public and Private IP restrictions
    statement {
      sid = "PublicIPsAndPrivateIPs"
      effect = "Deny"

      principals {
        type        = "*"
        identifiers = ["*"]
      }

      actions = [
        "s3:GetObject",
        "s3:PutObject",
        # "s3:ListBucket",
      ]

      resources = [
        "${aws_s3_bucket.this.arn}/*",
      ]

      condition {
        test     = "NotIpAddressIfExists"
        variable = "aws:SourceIp"
        values   = var.src_public_ips
      }

      condition {
        test     = "NotIpAddressIfExists"
        variable = "aws:VpcSourceIp"
        values   = var.src_private_ips
      }

      condition {
        test = "BoolIfExists"
        variable = "aws:PrincipalIsAWSService"
        values   = ["false"]
      }

      condition {
      test = "BoolIfExists"
      variable = "aws:ViaAWSService"
      values   = ["false"]
    }
    }

  # 접근 가능한 VPC 제한
  # Restrict accessible VPCs
  # condition {
  #   test     = "StringNotEquals"
  #   variable = "aws:SourceVpc"
  #   values   = var.vpcs
  # }

  # 접근 가능한 VPC Endpoint 제한
  # Restrict accessible VPC Endpoint
  # condition {
  #   test     = "StringNotEquals"
  #   variable = "aws:SourceVpce"
  #   values   = var.vpces
  # }

  # 조직을 사용하는 경우
  # If you use organization
  # condition {
  #   test = "StringNotEquals"
  #   variable = "aws:PrincipalOrgID"
  #   values = "o-xxxxxxxxxxx"
  # }

  # 보안 주체에 연결된 태그 비교
  # Compare tags associated with security principal
  # condition {
  #   test = "StringNotEquals"
  #   variable = "aws:PrincipalTag/태그키"
  #   values = "태그벨류"
  # }
}

data "aws_iam_policy_document" "this" {
  source_policy_documents   = [data.aws_iam_policy_document.default.json]
  override_policy_documents = [var.policy]
}