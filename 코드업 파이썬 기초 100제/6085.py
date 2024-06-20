w, h, b = map(int, input().split())

# 총 비트 수를 구한 후 바이트로 변환, 그 다음 MB로 변환
total_bits = w * h * b
total_bytes = total_bits / 8
total_MB = total_bytes / (2 ** 20)

print(f"{total_MB:.2f} MB")
