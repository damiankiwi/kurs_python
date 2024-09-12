import pendulum

def find_overlap(start1, end1, start2, end2):
    interval1_start = pendulum.parse(start1)
    interval1_end = pendulum.parse(end1)
    interval2_start = pendulum.parse(start2)
    interval2_end = pendulum.parse(end2)

    overlap_start = max(interval1_start, interval2_start)
    overlap_end = min(interval1_end, interval2_end)

    if overlap_start <= overlap_end:
        return overlap_start, overlap_end
    else:
        return None

start1 = "2024-09-12 10:00:00"
end1 = "2024-09-12 14:00:00"
start2 = "2024-09-12 12:00:00"
end2 = "2024-09-12 16:00:00"

overlap = find_overlap(start1, end1, start2, end2)

if overlap:
    print(f"Overlapping period: {overlap[0]} to {overlap[1]}")
else:
    print("No overlapping period")