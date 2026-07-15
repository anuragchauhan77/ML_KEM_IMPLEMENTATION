import oqs

print("Available KEM Algorithms:\n")

for alg in oqs.get_enabled_kem_mechanisms():
    print(alg)