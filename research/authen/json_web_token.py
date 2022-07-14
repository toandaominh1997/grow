import jwt

encoded_jwt = jwt.encode({"toandm2": "admin"}, "secret", algorithm = "HS256")

print("encode :", encoded_jwt)

decode = jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])
print("decode: ", decode)
