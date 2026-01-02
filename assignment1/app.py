print("Input 5 angka acak:")

nums = []

for i in range(5):
    nilai = int(input())
    nums.append(nilai)

max = nums[0]
min = nums[0]
for i in range(5):
    max = nums[i] if nums[i] > max else max
    min = nums[i] if nums[i] < min else min

print(f'Nilai maximal yang anda input adalah {max}')
print(f'Nilai minimal yang anda input adalah {min}')
