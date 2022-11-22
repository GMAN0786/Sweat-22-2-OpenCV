import cv2
img_file = "./book.jpg" # 표시할 이미지의 경로를 변수에 저장
img = cv2.imread(img_file) #opencv의 메서드를 활용해 이미지를 읽은 뒤 변수에 저장

if img is not None: # 만약 img가 비어있지 않다면
    cv2.imshow('IMG',img) #'IMG'라는 이미지를 표시한다
    cv2.waitKey() # 키가 입력될 때 까지 대기함. (변수 입력시 N msec 까지 대기)
    cv2.destroyAllWindows() # 모든 창을 닫기
    cv2.watiKey(1) #Mac용 Exit Code
else:
    print("No image file")