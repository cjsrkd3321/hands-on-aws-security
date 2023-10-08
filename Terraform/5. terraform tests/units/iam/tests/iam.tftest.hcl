variables {
  role_name = "test_rex"
}

run "test_var_role_name_length" {
  command = plan

  variables {
    role_name = "rextestrextestrextestrextestrextestrextestrextest"
  }

  expect_failures = [
    var.role_name,
  ]
}

run "test_aws_iam_role_id" {
  // command = plan

  assert {
    condition     = aws_iam_role.this.id == "${var.role_name}_role"
    error_message = "Role name did not match expected"
  }
}

run "test_aws_iam_role_policy" {
  command = plan

  assert {
    condition     = jsondecode(aws_iam_role.this.assume_role_policy)["Statement"][0]["Action"] == "sts:AssumeRole"
    error_message = "NOPE"
  }
}