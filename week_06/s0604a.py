n = int(input())
n_dist = list(map(int, input().split()))
n_list = []
for i in range(n):
    n_list.append((n_dist[i], i + 1))
n_sort_list = sorted(n_list)
m = int(input())
m_dist = list(map(int, input().split()))
m_list = []
for i in range(m):
    m_list.append((m_dist[i], i + 1))
m_sort_list = sorted(m_list)
saved_index = 0
i = 0
j = 0
n_m_list = []
for i in range(n):
    for j in range(saved_index, m-1):
        distance_i_j = abs(n_sort_list[i][0] - m_sort_list[j][0])
        distance_i_j1 = abs(n_sort_list[i][0] - m_sort_list[j+1][0])
        if distance_i_j <= distance_i_j1:
            saved_index = j
            break
        else:
            if j + 2 == m:
                j += 1
                saved_index += 1
                break
            else:
                saved_index += 1
    new_point = (n_sort_list[i][1], m_sort_list[j][1])
    n_m_list.append(new_point)
n_m_list_sort = sorted(n_m_list)
final_list = []
for i in range(n):
    final_list.append(n_m_list_sort[i][1])
print(*final_list)
