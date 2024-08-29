from constructs import Construct
from aws_cdk import (
    Stack,
    aws_iam as iam,
    RemovalPolicy,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy
)


class S3Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        UnleashBucket = s3.Bucket(self, 
                                "MyCdkBucket",
                                bucket_name="yuvalunleashbucket432",
                                removal_policy=RemovalPolicy.DESTROY,
                                auto_delete_objects=True,
                                block_public_access=s3.BlockPublicAccess.BLOCK_ACLS)
        
        full_access_policy = iam.PolicyStatement(
            actions=["s3:*"],
            resources=[f"{UnleashBucket.bucket_arn}", f"{UnleashBucket.bucket_arn}/*"],
            principals=[iam.AnyPrincipal()]
        )

        UnleashBucket.add_to_resource_policy(full_access_policy)
        
        s3deploy.BucketDeployment(self,
                                  'DeployFiles',
                                  sources=[s3deploy.Source.asset('./files/s3')],
                                  destination_bucket=UnleashBucket)
