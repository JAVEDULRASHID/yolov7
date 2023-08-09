import cv2
import os

path = os.getcwd()

full_path = os.path.join(path, "test_image")
lis = os.listdir(full_path)
length = len(lis)//2


for i in range(0, length, 2):
    img = cv2.imread(os.path.join(full_path,lis[i]))
    w, h, _ = img.shape
    img_path = os.path.join(full_path, lis[i])
    txt_path = os.path.join(full_path, lis[i+1])
    print(img_path)
    print(txt_path)

    # img = cv2.imread(img_path)

    with open(txt_path, "r") as file:
        content = file.read()
        values = content.split()
        no_box = len(values)//5
        float_lis = [float(j) for j in values]

        for k in range(0, no_box, 1):
            x = float_lis[5*k+1]
            y = float_lis[5*k+2]
            width = float_lis[5*k+3]
            height = float_lis[5*k+4]

            x1 = int((x - width / 2) * w)
            y1 = int((y - height / 2) * h)
            x2 = int((x + width / 2) * w)
            y2 = int((y + height / 2) * h)

            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 4)
    cv2.imwrite(f"./output_image/{i}.jpg", img)

cv2.waitKey(0)
