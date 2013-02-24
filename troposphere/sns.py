# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty


class Subscription(AWSProperty):
    props = {
        'Endpoint': (basestring, True),
        'Protocol': (basestring, True),
    }


class TopicPolicy(AWSObject):
    props = {
        'PolicyDocument': (dict, True),
        'Topics': (list, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::SNS::TopicPolicy"
        sup = super(TopicPolicy, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)


class Topic(AWSObject):
    props = {
        'DisplayName': (basestring, False),
        'Subscription': (list, True),
    }

    def __init__(self, name, **kwargs):
        self.type = "AWS::SNS::Topic"
        sup = super(Topic, self)
        sup.__init__(name, self.type, "Properties", self.props, **kwargs)
