# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['DeploymentArgs', 'Deployment']

@pulumi.input_type
class DeploymentArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 node_id: Any,
                 disks: Optional[pulumi.Input[Sequence[pulumi.Input['DiskArgs']]]] = None,
                 network_name: Optional[pulumi.Input[str]] = None,
                 qsfs: Optional[pulumi.Input[Sequence[pulumi.Input['QSFSInputArgs']]]] = None,
                 solution_provider: Optional[pulumi.Input[int]] = None,
                 solution_type: Optional[pulumi.Input[str]] = None,
                 vms: Optional[pulumi.Input[Sequence[pulumi.Input['VMInputArgs']]]] = None,
                 zdbs: Optional[pulumi.Input[Sequence[pulumi.Input['ZDBInputArgs']]]] = None):
        """
        The set of arguments for constructing a Deployment resource.
        :param pulumi.Input[str] name: The name of the deployment, it's required and cannot exceed 50 characters. Only alphanumeric and underscores characters are supported
        :param Any node_id: The node ID to deploy on, required and should match the requested resources
        :param pulumi.Input[Sequence[pulumi.Input['DiskArgs']]] disks: The disks requested to be included in the deployment
        :param pulumi.Input[str] network_name: The name of the network, it's required and cannot exceed 50 characters. Only alphanumeric and underscores characters are supported. Network must exist
        :param pulumi.Input[Sequence[pulumi.Input['QSFSInputArgs']]] qsfs: The qsfs instances requested to be included in the deployment
        :param pulumi.Input[int] solution_provider: ID for the deployed solution which allows the creator of the solution to gain a percentage of the rewards
        :param pulumi.Input[str] solution_type: The name of the solution for created contract to be consistent across threefold tooling (project name in deployment metadata)
        :param pulumi.Input[Sequence[pulumi.Input['VMInputArgs']]] vms: The vms requested to be included in the deployment
        :param pulumi.Input[Sequence[pulumi.Input['ZDBInputArgs']]] zdbs: The zdbs requested to be included in the deployment
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "node_id", node_id)
        if disks is not None:
            pulumi.set(__self__, "disks", disks)
        if network_name is not None:
            pulumi.set(__self__, "network_name", network_name)
        if qsfs is not None:
            pulumi.set(__self__, "qsfs", qsfs)
        if solution_provider is not None:
            pulumi.set(__self__, "solution_provider", solution_provider)
        if solution_type is None:
            solution_type = 'vm/'
        if solution_type is not None:
            pulumi.set(__self__, "solution_type", solution_type)
        if vms is not None:
            pulumi.set(__self__, "vms", vms)
        if zdbs is not None:
            pulumi.set(__self__, "zdbs", zdbs)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the deployment, it's required and cannot exceed 50 characters. Only alphanumeric and underscores characters are supported
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def node_id(self) -> Any:
        """
        The node ID to deploy on, required and should match the requested resources
        """
        return pulumi.get(self, "node_id")

    @node_id.setter
    def node_id(self, value: Any):
        pulumi.set(self, "node_id", value)

    @property
    @pulumi.getter
    def disks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DiskArgs']]]]:
        """
        The disks requested to be included in the deployment
        """
        return pulumi.get(self, "disks")

    @disks.setter
    def disks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DiskArgs']]]]):
        pulumi.set(self, "disks", value)

    @property
    @pulumi.getter
    def network_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the network, it's required and cannot exceed 50 characters. Only alphanumeric and underscores characters are supported. Network must exist
        """
        return pulumi.get(self, "network_name")

    @network_name.setter
    def network_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_name", value)

    @property
    @pulumi.getter
    def qsfs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['QSFSInputArgs']]]]:
        """
        The qsfs instances requested to be included in the deployment
        """
        return pulumi.get(self, "qsfs")

    @qsfs.setter
    def qsfs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['QSFSInputArgs']]]]):
        pulumi.set(self, "qsfs", value)

    @property
    @pulumi.getter
    def solution_provider(self) -> Optional[pulumi.Input[int]]:
        """
        ID for the deployed solution which allows the creator of the solution to gain a percentage of the rewards
        """
        return pulumi.get(self, "solution_provider")

    @solution_provider.setter
    def solution_provider(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "solution_provider", value)

    @property
    @pulumi.getter
    def solution_type(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the solution for created contract to be consistent across threefold tooling (project name in deployment metadata)
        """
        return pulumi.get(self, "solution_type")

    @solution_type.setter
    def solution_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "solution_type", value)

    @property
    @pulumi.getter
    def vms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VMInputArgs']]]]:
        """
        The vms requested to be included in the deployment
        """
        return pulumi.get(self, "vms")

    @vms.setter
    def vms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VMInputArgs']]]]):
        pulumi.set(self, "vms", value)

    @property
    @pulumi.getter
    def zdbs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ZDBInputArgs']]]]:
        """
        The zdbs requested to be included in the deployment
        """
        return pulumi.get(self, "zdbs")

    @zdbs.setter
    def zdbs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ZDBInputArgs']]]]):
        pulumi.set(self, "zdbs", value)


class Deployment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 disks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DiskArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_name: Optional[pulumi.Input[str]] = None,
                 node_id: Optional[Any] = None,
                 qsfs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['QSFSInputArgs']]]]] = None,
                 solution_provider: Optional[pulumi.Input[int]] = None,
                 solution_type: Optional[pulumi.Input[str]] = None,
                 vms: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VMInputArgs']]]]] = None,
                 zdbs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZDBInputArgs']]]]] = None,
                 __props__=None):
        """
        Create a Deployment resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DiskArgs']]]] disks: The disks requested to be included in the deployment
        :param pulumi.Input[str] name: The name of the deployment, it's required and cannot exceed 50 characters. Only alphanumeric and underscores characters are supported
        :param pulumi.Input[str] network_name: The name of the network, it's required and cannot exceed 50 characters. Only alphanumeric and underscores characters are supported. Network must exist
        :param Any node_id: The node ID to deploy on, required and should match the requested resources
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['QSFSInputArgs']]]] qsfs: The qsfs instances requested to be included in the deployment
        :param pulumi.Input[int] solution_provider: ID for the deployed solution which allows the creator of the solution to gain a percentage of the rewards
        :param pulumi.Input[str] solution_type: The name of the solution for created contract to be consistent across threefold tooling (project name in deployment metadata)
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VMInputArgs']]]] vms: The vms requested to be included in the deployment
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZDBInputArgs']]]] zdbs: The zdbs requested to be included in the deployment
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DeploymentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Deployment resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param DeploymentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DeploymentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 disks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DiskArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_name: Optional[pulumi.Input[str]] = None,
                 node_id: Optional[Any] = None,
                 qsfs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['QSFSInputArgs']]]]] = None,
                 solution_provider: Optional[pulumi.Input[int]] = None,
                 solution_type: Optional[pulumi.Input[str]] = None,
                 vms: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VMInputArgs']]]]] = None,
                 zdbs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZDBInputArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DeploymentArgs.__new__(DeploymentArgs)

            __props__.__dict__["disks"] = disks
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["network_name"] = network_name
            if node_id is None and not opts.urn:
                raise TypeError("Missing required property 'node_id'")
            __props__.__dict__["node_id"] = node_id
            __props__.__dict__["qsfs"] = qsfs
            __props__.__dict__["solution_provider"] = solution_provider
            if solution_type is None:
                solution_type = 'vm/'
            __props__.__dict__["solution_type"] = solution_type
            __props__.__dict__["vms"] = vms
            __props__.__dict__["zdbs"] = zdbs
            __props__.__dict__["contract_id"] = None
            __props__.__dict__["ip_range"] = None
            __props__.__dict__["node_deployment_id"] = None
            __props__.__dict__["qsfs_computed"] = None
            __props__.__dict__["vms_computed"] = None
            __props__.__dict__["zdbs_computed"] = None
        super(Deployment, __self__).__init__(
            'threefold:index:Deployment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Deployment':
        """
        Get an existing Deployment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DeploymentArgs.__new__(DeploymentArgs)

        __props__.__dict__["contract_id"] = None
        __props__.__dict__["disks"] = None
        __props__.__dict__["ip_range"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_name"] = None
        __props__.__dict__["node_deployment_id"] = None
        __props__.__dict__["node_id"] = None
        __props__.__dict__["qsfs"] = None
        __props__.__dict__["qsfs_computed"] = None
        __props__.__dict__["solution_provider"] = None
        __props__.__dict__["solution_type"] = None
        __props__.__dict__["vms"] = None
        __props__.__dict__["vms_computed"] = None
        __props__.__dict__["zdbs"] = None
        __props__.__dict__["zdbs_computed"] = None
        return Deployment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def contract_id(self) -> pulumi.Output[int]:
        """
        The deployment ID
        """
        return pulumi.get(self, "contract_id")

    @property
    @pulumi.getter
    def disks(self) -> pulumi.Output[Optional[Sequence['outputs.Disk']]]:
        """
        The disks requested to be included in the deployment
        """
        return pulumi.get(self, "disks")

    @property
    @pulumi.getter
    def ip_range(self) -> pulumi.Output[str]:
        """
        IP range of the node for the wireguard network (e.g. 10.1.2.0/24). Has to have a subnet mask of 24
        """
        return pulumi.get(self, "ip_range")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the deployment, it's required and cannot exceed 50 characters. Only alphanumeric and underscores characters are supported
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def network_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the network, it's required and cannot exceed 50 characters. Only alphanumeric and underscores characters are supported. Network must exist
        """
        return pulumi.get(self, "network_name")

    @property
    @pulumi.getter
    def node_deployment_id(self) -> pulumi.Output[Mapping[str, int]]:
        """
        Mapping from each node to its deployment ID
        """
        return pulumi.get(self, "node_deployment_id")

    @property
    @pulumi.getter
    def node_id(self) -> pulumi.Output[Any]:
        """
        The node ID to deploy on, required and should match the requested resources
        """
        return pulumi.get(self, "node_id")

    @property
    @pulumi.getter
    def qsfs(self) -> pulumi.Output[Optional[Sequence['outputs.QSFSInput']]]:
        """
        The qsfs output instances requested to be included in the deployment
        """
        return pulumi.get(self, "qsfs")

    @property
    @pulumi.getter
    def qsfs_computed(self) -> pulumi.Output[Sequence['outputs.QSFSComputed']]:
        return pulumi.get(self, "qsfs_computed")

    @property
    @pulumi.getter
    def solution_provider(self) -> pulumi.Output[Optional[int]]:
        """
        ID for the deployed solution which allows the creator of the solution to gain a percentage of the rewards
        """
        return pulumi.get(self, "solution_provider")

    @property
    @pulumi.getter
    def solution_type(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the solution for created contract to be consistent across threefold tooling (project name in deployment metadata)
        """
        return pulumi.get(self, "solution_type")

    @property
    @pulumi.getter
    def vms(self) -> pulumi.Output[Optional[Sequence['outputs.VMInput']]]:
        """
        The vms output requested to be included in the deployment
        """
        return pulumi.get(self, "vms")

    @property
    @pulumi.getter
    def vms_computed(self) -> pulumi.Output[Sequence['outputs.VMComputed']]:
        return pulumi.get(self, "vms_computed")

    @property
    @pulumi.getter
    def zdbs(self) -> pulumi.Output[Optional[Sequence['outputs.ZDBInput']]]:
        """
        The zdbs output requested to be included in the deployment
        """
        return pulumi.get(self, "zdbs")

    @property
    @pulumi.getter
    def zdbs_computed(self) -> pulumi.Output[Sequence['outputs.ZDBComputed']]:
        return pulumi.get(self, "zdbs_computed")

