
size = int(input())
box_width = int(input())
box_height = int(input())

head = "   o "
body = "  ooo"
legs = "  o o"
box = "x"

head_list=[]
for i in head:
    head_list.append(i)
body_list=[]
for i in body:
    body_list.append(i)
legs_list=[]
for i in legs:
    legs_list.append(i)

if box_width <= len(head):

    for i in range(1, 2*size+2):
        if i == 1:  # Head
            if box_height == 2*size+1:
                for headprint1 in range(box_width):
                    print(box, end="")
                for headprint2 in range(box_width, 5):
                    print(head_list[headprint2], end="")
                print()
            else:
                print(head)
                continue

        elif i > 1 and i < ( (2 * size + 1 ) / 2 ) + 1:   # Body
            if box_height >= 2 * size:
                body_height_difference = 0
            elif box_height > size:
                body_height_difference = 2*size - box_height

            else:
                print(body)
                continue
            if i -1 <= body_height_difference:
                print(body)
            else:
                for bodyprint1 in range(box_width):
                    print(box, end="")
                for bodyprint2 in range(box_width, 5):
                    print(body_list[bodyprint2], end="")
                print()

        else: # Legs
            if box_height >= size:
                legs_height_difference = 0
            else:
                legs_height_difference = size - box_height

            if i - size - 1 <= legs_height_difference:
                print(legs)
            else:
                for legsprint1 in range(box_width):
                    print(box, end="")
                for legsprint2 in range(box_width, 5):
                    print(legs_list[legsprint2], end="")
                print()
else:  # box_width > 5
    for i in range(1, 2 * size + 2):
        if i == 1:  # Head
            if box_height == 2 * size + 1:
                for headprint1 in range(box_width):
                    print(box, end="")
                print()
            else:
                print(head)
                continue

        elif i > 1 and i < ((2 * size + 1) / 2) + 1:  # Body
            if box_height >= 2 * size:
                body_height_difference = 0
            elif box_height > size:
                body_height_difference = 2 * size - box_height

            else:
                print(body)
                continue
            if i - 1 <= body_height_difference:
                print(body)
            else:
                for bodyprint1 in range(box_width):
                    print(box, end="")
                print()

        else:  # Legs
            if box_height >= size:
                legs_height_difference = 0
            else:
                legs_height_difference = size - box_height

            if i - size - 1 <= legs_height_difference:
                print(legs)
            else:
                for legsprint1 in range(box_width):
                    print(box, end="")
                print()




