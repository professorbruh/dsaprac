import statistics
arr = input()
arr.strip()
nums1 = list(map(int,arr.split(' ')))

arr = input()
arr.strip()
nums2 = list(map(int,arr.split(' ')))

joint_arr = nums1+nums2

joint_arr.sort()
joint_arr1 = []
for i in range(0,len(joint_arr)):
    if joint_arr[i] not in joint_arr1:
        joint_arr1.append(joint_arr[i])

n = (len(joint_arr1)-1) // 2

if len(joint_arr1)%2==0:
    median = joint_arr1[n] + joint_arr1[n+1] // 2
else:
    median = joint_arr1[n]

print(median)
print(statistics.median(joint_arr1))