

def tournament_winner(competitions, results):
    lead = ''
    scores = { lead: 0 }

    for i, competition in enumerate(competitions):
        home, away = competition
        HOME_TEAM_WON = results[i] == 1
        winner = home if HOME_TEAM_WON else away
        score = scores.setdefault(winner, 0)
        scores[winner] = score + 3
        if scores[winner] > scores[lead]:
            lead = winner

    return lead


def three_number_sum(array, targetSum):
    results = []
    for i, value in enumerate(array):
        store = {}
        new_target = targetSum - value
        for j, new_value in enumerate(array):
            if j == i: continue
            if new_value in store:
                result = [value, store[new_value], new_value]
                if result[0] < result[1] < result[2]:
                    results.append(result)
            store[new_target - new_value] = array[j]
    results.sort()
    return results


def spiralTraverse(array):
    spiral = []
    z = 1
    x, y = 0, 0
    x_start, x_end = 0, len(array[0])
    y_start, y_end = 1, len(array)
    while len(spiral) < len(array) * len(array[0]):
        for x in range(x_start - 1 if z == -1 else x_start, x_end - 1 if z == -1 else x_end, z):
            spiral.append(array[y][x])
        x_end -= 1 * z

        for y in range(y_start - 1 if z == -1 else y_start, y_end -1 if z == -1 else y_end, z):
            spiral.append(array[y][x])
        y_end -= 1 * z

        z *= -1
        x_start, x_end = x_end, x_start
        y_start, y_end = y_end, y_start

    return spiral


def longestPeak(array):
    if len(array) < 3: return 0
    longest_peak = 0
    i = 1
    while i < len(array) - 1:
        if array[i - 1] < array[i] > array[i + 1]:
            peak = i
            l = peak - 1
            r = peak + 1
            current_peak_length = 1
            while l >= 0 and array[l] < array[l + 1]:
                current_peak_length += 1
                l -= 1
            while r <= len(array) - 1 and array[r] < array[r - 1]:
                current_peak_length += 1
                r += 1
            if current_peak_length > longest_peak:
                longest_peak = current_peak_length
            i = r
            continue

        i += 1
