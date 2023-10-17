def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    prefix_sum = [0] * (n + 1)
    
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]
    
    min_songs = float('inf')
    start_song = -1
    
    for i in range(n):
        j = i + 1
        while j <= n and prefix_sum[j] - prefix_sum[i] < p:
            j += 1
        if j <= n and j - i < min_songs:
            min_songs = j - i
            start_song = i + 1
    
    print(start_song, min_songs)

if __name__ == "__main__":
    main()
