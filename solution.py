def find_missing_ranges(frames: list[int]) -> dict:
    """
    Time Complexity: O(N) where `N` is the maximum frame number in the input list.
    Space Complexity: O(M) where `M` is the number of frames in the input list. max_frame
    """
    frames = set(frames)
    max_frame = max(frames, default=0)

    gaps, missing_count = [], 0
    longest_gap_start = 0
    longest_gap_end = 0

    gap_start = 0
    for frame in range(1, max_frame + 2):  # Add an imaginary frame at max_frame + 1
        if frame not in frames:
            missing_count += 1
            if gap_start == 0:
                gap_start = frame
        elif gap_start != 0:
            gap_end = frame - 1
            gaps.append([gap_start, gap_end])

            if gap_end - gap_start >= longest_gap_end - longest_gap_start:
                longest_gap_start = gap_start
                longest_gap_end = gap_end

            gap_start = 0
            gap_end = 0

    return {
        "gaps": gaps,
        "longest_gap": [longest_gap_start, longest_gap_end],
        "missing_count": missing_count - 1,  # Exclude the imaginary frame at max_frame + 1
    }


""" 
# some test cases
frames = [1, 3]
# 2
print(find_missing_ranges(frames))
frames = [1, 3, 6]
# 2
# 4, 5
print(find_missing_ranges(frames))
frames = [1, 2, 3, 5, 6, 10, 11, 16]
# 4
# 7,8,9
# 12,13,14,15
print(find_missing_ranges(frames))
frames = [5, 1, 2, 3, 6, 16, 11, 10]
print(find_missing_ranges(frames))
frames = [5, 1, 2, 3, 6, 16, 11, 20]
# 4
# 7 ,8 ,9 ,10
# 12,13,14,15
# 17,18,19
print(find_missing_ranges(frames))
# frames = [i for i in range(1, 10010000) if i % 6000 == 0]
# print(find_missing_ranges(frames))
"""
