t = int(input())
result = 0
for _ in range(t):
    result += sum(list(map(int,input().split())))
print(result//2)
    

# faster
# #include <iostream>
# using namespace std;

# int main()
# {
#     int n, a, result = 0;
#     cin >> n;
#     int x = n;
#     while (x--) {
#         int m = n;
#         while (m--) {
#             cin >> a;
#             result += a;
#         }
#     }
#     cout << result / 2 << endl;
#     return 0;
# }
