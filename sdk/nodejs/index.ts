// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export { DeploymentArgs } from "./deployment";
export type Deployment = import("./deployment").Deployment;
export const Deployment: typeof import("./deployment").Deployment = null as any;
utilities.lazyLoad(exports, ["Deployment"], () => require("./deployment"));

export { GatewayFQDNArgs } from "./gatewayFQDN";
export type GatewayFQDN = import("./gatewayFQDN").GatewayFQDN;
export const GatewayFQDN: typeof import("./gatewayFQDN").GatewayFQDN = null as any;
utilities.lazyLoad(exports, ["GatewayFQDN"], () => require("./gatewayFQDN"));

export { GatewayNameArgs } from "./gatewayName";
export type GatewayName = import("./gatewayName").GatewayName;
export const GatewayName: typeof import("./gatewayName").GatewayName = null as any;
utilities.lazyLoad(exports, ["GatewayName"], () => require("./gatewayName"));

export { KubernetesArgs } from "./kubernetes";
export type Kubernetes = import("./kubernetes").Kubernetes;
export const Kubernetes: typeof import("./kubernetes").Kubernetes = null as any;
utilities.lazyLoad(exports, ["Kubernetes"], () => require("./kubernetes"));

export { NetworkArgs } from "./network";
export type Network = import("./network").Network;
export const Network: typeof import("./network").Network = null as any;
utilities.lazyLoad(exports, ["Network"], () => require("./network"));

export { ProviderArgs } from "./provider";
export type Provider = import("./provider").Provider;
export const Provider: typeof import("./provider").Provider = null as any;
utilities.lazyLoad(exports, ["Provider"], () => require("./provider"));

export { SchedulerArgs } from "./scheduler";
export type Scheduler = import("./scheduler").Scheduler;
export const Scheduler: typeof import("./scheduler").Scheduler = null as any;
utilities.lazyLoad(exports, ["Scheduler"], () => require("./scheduler"));


// Export sub-modules:
import * as config from "./config";
import * as types from "./types";

export {
    config,
    types,
};

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "threefold:index:Deployment":
                return new Deployment(name, <any>undefined, { urn })
            case "threefold:index:GatewayFQDN":
                return new GatewayFQDN(name, <any>undefined, { urn })
            case "threefold:index:GatewayName":
                return new GatewayName(name, <any>undefined, { urn })
            case "threefold:index:Kubernetes":
                return new Kubernetes(name, <any>undefined, { urn })
            case "threefold:index:Network":
                return new Network(name, <any>undefined, { urn })
            case "threefold:index:Scheduler":
                return new Scheduler(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("threefold", "index", _module)
pulumi.runtime.registerResourcePackage("threefold", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:threefold") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});
