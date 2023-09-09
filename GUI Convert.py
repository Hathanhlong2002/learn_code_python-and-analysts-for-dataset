import tkinter as tk
dictionary = {
   "a": "o", "à": "ò", "á": "ó", "ã": "õ", "ả": "ỏ", "ạ": "ọ", 
    "ă":"ô" , "ằ":"ờ" ,"ắ":"ớ" ,"ẵ":"ỡ" ,"ẳ":"ở" ,"ặ":"ợ" ,
    "â":"ô" , "ầ":"ồ" ,"ấ":"ố" ,"ẫ":"ỗ" ,"ẩ":"ổ" ,"ậ":"ộ" ,
    "b": "p", 
    "c":"q" ,
    "d": "r",
    "đ": "s", 
    "e": "u", "è": "ù","é": "ú","ẽ": "ũ","ẻ": "ủ","ẹ": "ụ",
    "ê": "ư", "ề": "ừ", "ế": "ứ", "ễ": "ữ", "ể": "ử", "ệ": "ự", 
    "g": "t", 
    "h": "v", 
    "i": "i","ì": "ì","í": "í","ĩ": "ĩ","ỉ": "ỉ","ị": "ị",
    "k": "x", 
    "l": "y", 
    "m": "z", 
    "n": "w", 
    "o": "a", "ò": "à","ó": "á","õ": "ã","ỏ": "ả","ọ": "ạ",
    "ô": "â", "ồ": "ầ","ố": "ấ","ỗ": "ẫ","ổ": "ẩ","ộ": "ậ",
    "ơ": "ă", "ờ": "ằ","ớ": "ắ","ỡ": "ẵ","ở": "ẳ","ợ": "ặ",
    "p": "b", 
    "q": "c", 
    "r": "d", 
    "s": "đ", 
    "t": "g", 
    "u": "e","ù": "è", "ú": "é","ũ": "ẽ","ủ": "ẻ","ụ": "ẹ",
    "ư": "ê","ừ": "ề","ứ": "ế","ữ": "ễ","ử": "ể","ự": "ệ", 
    "v": "h", 
    "x": "k", 
    "y": "l",
    "z": "m",
    "w":" n",
    " ":" "
}#bảng chữ cái dịch
def translate():#hàm dịch chữ
    input_text = input_entry.get() # phần nhập chữ
    # Xử lý việc dịch văn bản tại đây
    output_text_tmp=" "
    for i in input_text:
        output_text_tmp+=dictionary.get(i, "Từ này không có trong từ điển.")
    output_text.config(text=output_text_tmp)# phần kết quả
    
def swap():
    input_text = input_entry.get()
    output_text.config(text=input_text)
    input_entry.delete(0, "end")


root = tk.Tk() # Tạo cửa số chính của giao diện GUI
root.title("Translator MY CODE") # tên tiêu đề
root.geometry("500x350")    # đặt kích thước cửa sổ 400*250

input_frame = tk.Frame(root, bg="green", relief="sunken", bd=15)
#tạo một khung (frame) trong cửa sổ GUI, với root là thẻ cha, 
#màu sắc nền là "green", kiểu relief là "sunken" và độ rộng viền là 2.
input_frame.pack(fill="both", expand=True)
# cho khung vô GUI vừa tạo, tính năng điền đầy đủ ô và tự động mở rộng cho phù hợp

input_label = tk.Label(input_frame, text="Input:", font=("Tahoma", 12), bg="LightGreen")
#tao môt nhãn trong khung input_frame, tên là Input,font chữ, màu background
input_label.pack(pady=10)# xếp vào khung và có khoảng trắng trên dưới 10 pixels

input_entry = tk.Entry(input_frame, font=("Tahoma", 14), bd=5)
# tao một mục nhâp trong khung( input_frame),có font cỡ chữ 14, độ rộng viền 5
input_entry.pack(fill="x", padx=10, pady=10)
# xếp input_entry với fill=x, khoảng trống theo chiều x,y=10
output_frame = tk.Frame(root, bg="green yellow", relief="sunken", bd=10)
# tạo tiếp một frame trong GUI gốc, giống input
output_frame.pack(fill="both", expand=True)
# như trên, cho vô khung
output_label = tk.Label(output_frame, text="Output:", font=("Tahoma", 12), bg="LightGreen")
# tạo nhãn output, trong khung ouput_frame
output_label.pack(pady=10)# thêm vào và có khoảng trắng bằng 10

output_text = tk.Label(output_frame, font=("Tahoma", 14), bg="white")
# Tạo một nhãn ouput trong khung output_frame
output_text.pack(fill="x", padx=10, pady=10)#thêm nó vào có fill=x, khoảng trắng theo chiều x,y=10
output_entry = tk.Entry(output_text, font=("Tahoma", 14), bd=5)
# tao một mục nhâp trong khung( input_frame),có font cỡ chữ 14, độ rộng viền 5
output_entry.pack(fill="x", padx=10, pady=10)
# xếp input_entry với fill=x, khoảng trống theo chiều x,y=10


translate_button_frame=tk.Frame(root,bg='gray',bd=0,pady=5)
translate_button_frame.pack(fill="both", expand=True)
translate_button = tk.Button(translate_button_frame, text="Translate", command=translate, font=("Tahoma", 14), bg="LightSeaGreen")
# tạo nút Button, trong GUI gốc, với tên translate, gọi hàm translate,có font và cỡ 14,bg
translate_button.pack(pady=10)# thêm vào GUI và có khoảng trắng =10

swap_button = tk.Button(root, text="Swap", command=swap, font=("Tahoma", 14), bg="red")
swap_button.pack(pady=10)

def on_closing():
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.bind('<Escape>', lambda e: root.destroy())

root.mainloop()
