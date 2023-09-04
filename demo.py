from tkinter import ttk, Tk, PhotoImage,Canvas,filedialog

# root = Tk()
# frame_header =ttk.Frame(root)
# frame_header.pack()
# ttk.Label(frame_header, text="This is text label").pack()

# canvas = Canvas(root,bg="gray",width=300,height=400)
# canvas.pack()
# logo = PhotoImage(file="giphy.gif")
# canvas.create_image(200,200,image=logo)

# root.mainloop()

#save file
# root = Tk()
# filename =filedialog.asksave()
# # filename =filedialog.askopenfilename()
# print(filename)
# root.mainloop()
import cv2
# image = cv2.imread("car-1.gif")
# image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# cv2.imshow("This is processed image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
image = cv2.imread("car-1.gif")
image = cv2.bitwise_not(image)
cv2.imshow("This is processed image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()