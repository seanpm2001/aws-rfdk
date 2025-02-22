# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import (
    List,
    Mapping,
    Optional
)

from aws_rfdk.deadline import (
    AwsCustomerAgreementAndIpLicenseAcceptance,
)


class AppConfig:
    """
    Configuration values for the sample app.

    TODO: Fill these in with your own values.
    """
    def __init__(self):
        # By downloading or using the Deadline software, you agree to the AWS Customer Agreement (https://aws.amazon.com/agreement/)
        # and AWS Intellectual Property License (https://aws.amazon.com/legal/aws-ip-license-terms/). You acknowledge that Deadline
        # is AWS Content as defined in those Agreements.
        # To accept these terms, change the value here to AwsCustomerAgreementAndIpLicenseAcceptance.USER_ACCEPTS_AWS_CUSTOMER_AGREEMENT_AND_IP_LICENSE
        self.accept_aws_customer_agreement_and_ip_license: AwsCustomerAgreementAndIpLicenseAcceptance = AwsCustomerAgreementAndIpLicenseAcceptance.USER_REJECTS_AWS_CUSTOMER_AGREEMENT_AND_IP_LICENSE

        # The standard availability zones that the render farm will deploy into. It is recommended to use at least
        # two and they must be from the same region. The default values being provided are two of the four standard
        # zones in us-west-2, located in Oregon.
        self.availability_zones_standard: List[str] = ['us-west-2a', 'us-west-2b']

        # The local availability zones that will hold the worker fleet. They must belong to the same region as the standard
        # zones. The default value being provided here is one of the two local zones in us-west-2, located in Los Angeles.
        self.availability_zones_local: List[str] = ['us-west-2-lax-1a']

        # The version of Deadline to use on the render farm. Leave as None for the latest release or specify a version
        # to pin to. Some examples of pinned version values are "10", "10.1", or "10.1.16"
        # The default value of 10.1.19 is used, to match the worker AMI ID provided below
        self.deadline_version: Optional[str] = '10.1.19'

        # A map of regions to Deadline Client Linux AMIs. As an example, the base Linux Deadline 10.1.19.4 AMI ID
        # from us-west-2 is filled in. It can be used as-is, added to, or replaced. Ideally the version here
        # should match the one used for staging the render queue and usage based licensing recipes.
        self.deadline_client_linux_ami_map: Mapping[str, str] = {'us-west-2': 'ami-04ae356533dc07fb5'}

        # (Optional) The name of the EC2 keypair to associate with the instances.
        self.key_pair_name: Optional[str] = None


config: AppConfig = AppConfig()
