# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class StartTaskInformation(Model):
    """Information about a start task running on a compute node.

    :param state: The state of the start task on the compute node. Values are:
     running - The start task is currently running.
     completed - The start task has exited with exit code 0, or the start task
     has failed and the retry limit has reached, or the start task process did
     not run due to task preparation errors (such as resource file download
     failures). Possible values include: 'running', 'completed'
    :type state: str or ~azure.batch.models.StartTaskState
    :param start_time: The time at which the start task started running. This
     value is reset every time the task is restarted or retried (that is, this
     is the most recent time at which the start task started running).
    :type start_time: datetime
    :param end_time: The time at which the start task stopped running. This is
     the end time of the most recent run of the start task, if that run has
     completed (even if that run failed and a retry is pending). This element
     is not present if the start task is currently running.
    :type end_time: datetime
    :param exit_code: The exit code of the program specified on the start task
     command line. This property is set only if the start task is in the
     completed state. In general, the exit code for a process reflects the
     specific convention implemented by the application developer for that
     process. If you use the exit code value to make decisions in your code, be
     sure that you know the exit code convention used by the application
     process. However, if the Batch service terminates the start task (due to
     timeout, or user termination via the API) you may see an operating
     system-defined exit code.
    :type exit_code: int
    :param container_info: Information about the container under which the
     task is executing. This property is set only if the task runs in a
     container context.
    :type container_info:
     ~azure.batch.models.TaskContainerExecutionInformation
    :param failure_info: Information describing the task failure, if any. This
     property is set only if the task is in the completed state and encountered
     a failure.
    :type failure_info: ~azure.batch.models.TaskFailureInformation
    :param retry_count: The number of times the task has been retried by the
     Batch service. Task application failures (non-zero exit code) are retried,
     pre-processing errors (the task could not be run) and file upload errors
     are not retried. The Batch service will retry the task up to the limit
     specified by the constraints.
    :type retry_count: int
    :param last_retry_time: The most recent time at which a retry of the task
     started running. This element is present only if the task was retried
     (i.e. retryCount is nonzero). If present, this is typically the same as
     startTime, but may be different if the task has been restarted for reasons
     other than retry; for example, if the compute node was rebooted during a
     retry, then the startTime is updated but the lastRetryTime is not.
    :type last_retry_time: datetime
    :param result: The result of the task execution. If the value is 'failed',
     then the details of the failure can be found in the failureInfo property.
     Possible values include: 'success', 'failure'
    :type result: str or ~azure.batch.models.TaskExecutionResult
    """

    _validation = {
        'state': {'required': True},
        'start_time': {'required': True},
        'retry_count': {'required': True},
    }

    _attribute_map = {
        'state': {'key': 'state', 'type': 'StartTaskState'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'exit_code': {'key': 'exitCode', 'type': 'int'},
        'container_info': {'key': 'containerInfo', 'type': 'TaskContainerExecutionInformation'},
        'failure_info': {'key': 'failureInfo', 'type': 'TaskFailureInformation'},
        'retry_count': {'key': 'retryCount', 'type': 'int'},
        'last_retry_time': {'key': 'lastRetryTime', 'type': 'iso-8601'},
        'result': {'key': 'result', 'type': 'TaskExecutionResult'},
    }

    def __init__(self, state, start_time, retry_count, end_time=None, exit_code=None, container_info=None, failure_info=None, last_retry_time=None, result=None):
        self.state = state
        self.start_time = start_time
        self.end_time = end_time
        self.exit_code = exit_code
        self.container_info = container_info
        self.failure_info = failure_info
        self.retry_count = retry_count
        self.last_retry_time = last_retry_time
        self.result = result
