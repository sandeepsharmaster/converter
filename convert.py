import yaml

with open('deployment.yml', 'r') as file:
  prime_service = yaml.safe_load(file)

print("YAML File", prime_service)

#print("URL", prime_service['spec']['selector']['app'])
print("API version", prime_service['apiVersion'])
print("API kind", prime_service['kind'])
prime_service['kind'] = "Service"
print("API meta", prime_service['metadata'])
print("API spec", prime_service['spec'])
prime_service['metadata']['labels'] = None
print(type(prime_service['metadata']))
metadata = prime_service['metadata']
metadata.pop('labels')
print("END!!")
print("YAML File", prime_service)

print(type(prime_service))
