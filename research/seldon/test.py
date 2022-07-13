from seldon_core.seldon_client import SeldonClient

sc = SeldonClient(deployment_name="seldon-deployment-example", namespace="seldon")
res = sc.predict(
    gateway="istio",
    gateway_endpoint="localhost:9005",
    transport="rest",
    raw_data={"data": {"ndarray": [[5.964, 4.006, 2.081, 1.031]]}},
)
print(res.response)
assert res.success == True
