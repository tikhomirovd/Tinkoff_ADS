def filter_recommendations(stop_list: list, recommendations: list) -> list:
    stop_ptr, rec_ptr = 0, 0
    filtered_recommendations = []

    while stop_ptr < len(stop_list) and rec_ptr < len(recommendations):
        if recommendations[rec_ptr] < stop_list[stop_ptr]:
            filtered_recommendations.append(recommendations[rec_ptr])
            rec_ptr += 1
        elif recommendations[rec_ptr] > stop_list[stop_ptr]:
            stop_ptr += 1
        else:
            rec_ptr += 1

    filtered_recommendations.extend(recommendations[rec_ptr:])

    return filtered_recommendations


stop_list = list(map(int, input().split()))
recommendations = list(map(int, input().split()))

filtered_recommendations = filter_recommendations(stop_list, recommendations)

print(' '.join(map(str, filtered_recommendations)))
