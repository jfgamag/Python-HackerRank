# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

st = []
scores = set()
second_l_name = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        st.append([name, score])
        scores.add(score)

    second_lowest = sorted(scores)[1]

    for name, score in st:
        if score == second_lowest:
            second_l_name.append(name)

    for name in sorted(second_l_name):
        print(name)

