import yaml

def pod_deployment():
    with open('./asis/deployment.yaml', 'r') as file:
        prime_service = yaml.safe_load(file)

    # print("YAML File", prime_service)

    # Cleanup metadata
    metadata = prime_service['metadata']
    metadata.pop('annotations')
    metadata.pop('creationTimestamp')
    metadata.pop('resourceVersion')
    metadata.pop('uid')

    # Cleanup spec
    spec = prime_service['spec']
    spec.pop('progressDeadlineSeconds')
    spec.pop('revisionHistoryLimit')

    meta_2 = prime_service['spec']['template']['metadata']
    meta_2.pop('creationTimestamp')

    cont = prime_service['spec']['template']['spec']['containers'][0]
    cont.pop('resources')
    cont.pop('terminationMessagePath')
    # print(type(cont[0]['terminationMessagePolicy']))
    cont.pop('terminationMessagePolicy')

    spec_2 = prime_service['spec']['template']['spec']
    spec_2.pop('dnsPolicy')
    spec_2.pop('schedulerName')
    spec_2.pop('securityContext')

    # Cleanup status
    prime_service.pop('status')

    print("Your Job is done very well!!!!")
    print("Check your target folder ('tobe')")
    # print('/n')
    # print("YAML File", prime_service)

    print(type(prime_service))
    with open('./tobe/deployment.yaml', 'w') as outfile:
        yaml.dump(prime_service, outfile, default_flow_style=False)

pod_deployment()

def service_deployment():
    with open('./asis/service.yaml', 'r') as file:
        _service = yaml.safe_load(file)

    metadata = _service['metadata']
    metadata.pop('creationTimestamp')
    metadata.pop('finalizers')
    metadata.pop('resourceVersion')
    metadata.pop('uid')

    spec = _service['spec']
    spec.pop('allocateLoadBalancerNodePorts')
    spec.pop('clusterIP')
    spec.pop('clusterIPs')
    spec.pop('externalTrafficPolicy')
    spec.pop('internalTrafficPolicy')
    spec.pop('ipFamilies')
    spec.pop('ipFamilyPolicy')

    _service.pop('status')
    print()
    with open('./tobe/service.yaml', 'w') as outfile:
        yaml.dump(_service, outfile, default_flow_style=False)

service_deployment()