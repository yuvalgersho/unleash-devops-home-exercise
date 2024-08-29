#!/usr/bin/env python3

import aws_cdk as cdk

from infrastructure.s3_stack import S3Stack

app = cdk.App()
S3Stack(app, "UnleashS3Bucket")

app.synth()
