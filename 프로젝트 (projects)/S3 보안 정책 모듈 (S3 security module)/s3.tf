data "aws_caller_identity" "me" {}

data "http" "myip" {
  url = "http://ipv4.icanhazip.com"
}

module "s3" {
  source          = "./s3"
  name            = "rex-chun-s3-bucket-with-security-policy"
  src_public_ips  = ["${trimspace(data.http.myip.body)}/32"]
  src_private_ips = []
  principal_arns  = [data.aws_caller_identity.me.arn]
  user_ids        = [data.aws_caller_identity.me.user_id]
  policy          = data.aws_iam_policy_document.this.json
}

data "aws_iam_policy_document" "this" {
  statement {
    sid    = "BucketOwnerFullControl1"
    effect = "Allow"

    principals {
      type        = "AWS"
      identifiers = ["arn:aws:iam::000663531752:root"]
    }

    actions = [
      "s3:PutObject",
    ]

    resources = [
      "${module.s3.arn}/*",
    ]
  }
}