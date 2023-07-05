from collections import deque


def gather_credits(needed_credits, *courses):
    enrolled_courses = set()
    gathered_credits = 0
    course_queue = deque(courses)
    while course_queue:
        course_name, course_credits = course_queue.popleft()
        if course_name in enrolled_courses:
            continue
        gathered_credits += course_credits
        enrolled_courses.add(course_name)
        if gathered_credits >= needed_credits:
            break
    if gathered_credits >= needed_credits:
        sorted_courses = sorted(enrolled_courses)
        courses_str = ', '.join(sorted_courses)
        return f"Enrollment finished! Maximum credits: {gathered_credits}." \
               f"Courses: {courses_str}"
    else:
        credits_shortage = needed_credits - gathered_credits
        return f"You need to enroll in more courses! You have to gather {credits_shortage} credits more."


# Example usage
# print(gather_credits(
#     80,
#     ("Basics", 27),
# ))