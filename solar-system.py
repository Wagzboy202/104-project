import cv2

solarsystem = cv2.imread("solar-system.jpg")

cv2.putText(solarsystem,
            "Sun",
             (100,80),
             cv2.FONT_HERSHEY_COMPLEX,
             2,
             (0,0,255)
             )

cv2.putText(solarsystem,
            "Mercury",
             (110,180),
             cv2.FONT_HERSHEY_COMPLEX,
             0.3,
             (255,255,255)
             )
cv2.putText(solarsystem,
            "Mercury",
             (110,180),
             cv2.FONT_HERSHEY_COMPLEX,
             0.3,
             (255,255,255)
             )
cv2.imshow('display window', solarsystem)
cv2.waitKey(0)
#cv2.imwrite(“Solar_systemwithname.jpg”, solarsystem)