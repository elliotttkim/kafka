#!/usr/bin/env python3

import aws_cdk as cdk

from cdk.my_cdk_vpc_stack import MyVpcStack


app = cdk.App()
MyVpcStack(app, "MyVpcStack")

app.synth()
