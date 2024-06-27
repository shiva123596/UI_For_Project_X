import pyodbc
import tkinter as tk
from tkinter import Canvas, PhotoImage, messagebox, Toplevel, ttk
from pathlib import Path

# Database connection details
conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-QP1JEL3;"
    "Database=littleking;"
    "UID=Siva;"
    "PWD=2525;"
)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Siva_Koritela\OneDrive - University of Houston-Clear Lake\Desktop\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Define positions for each column
COLUMN_POSITIONS = {
    1: (725.0, 272.0),
    3: (150.9000244140625, 585.406494140625),
    4: (500.0, 585.0),
    5: (950.124755859375, 585.406494140625),
    6: (120.0499267578125, 459.49951171875),
    7: (525.0, 462.0),
    8: (915.0, 462.0)
}

# Declare global variables for images
image_button_1 = None
image_image_1 = None
image_image_2 = None
image_image_3 = None
image_image_4 = None
image_image_5 = None
image_image_6 = None
image_image_7 = None
image_image_8 = None
image_image_9 = None
image_image_10 = None
image_Rupee_1 = None

# Global variable to store FarmerID
FarmerID = None

entry_12 = None
entry_13 = None
entry_14 = None
entry_15 = None
entry_16 = None
entry_17 = None
entry_18 = None
dropdown_values_4 = {"Placeholder1": "Value1", "Placeholder2": "Value2"}  # Placeholder values

# Function to execute stored procedure with input values
def run_stored_procedure(canvas, entry_widget, display_columns):
    global FarmerID
    try:
        input_value1 = entry_widget.get()

        for item in canvas.find_withtag("output_text"):
            canvas.delete(item)

        with conn.cursor() as cursor:
            cursor.execute("EXEC p_Dashboard ?", (input_value1,))
            output_values = cursor.fetchall()
            FarmerID = output_values[0][8]
            print("Farmer ID:", FarmerID)

            for row_index, row in enumerate(output_values):
                for col_index, value in enumerate(row):
                    if col_index + 1 in display_columns:
                        position = COLUMN_POSITIONS.get(col_index + 1)
                        if position:
                            x, y = position
                            canvas.create_text(x, y + row_index * 50, anchor="nw", text=value, fill="#000000",
                                               font=("LexendZetta Regular", 28 * -1), tags="output_text")

        messagebox.showinfo("Success", "Stored procedure executed successfully!")
        execute_loan_procedure(FarmerID, entry_12, entry_13, entry_14, entry_15, entry_16, entry_17, entry_18)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to create content for Page 1
def create_page1_content(parent):
    canvas = tk.Canvas(parent, bg="#FFFFFF", height=709, width=1116)
    canvas.pack()

    entry_1 = tk.Entry(parent, bd=0, bg="#D9D9D9", fg="#000716", font=('Arial', 25), highlightthickness=0)
    entry_1.place(x=25.0, y=234.0,    width=294.0, height=64.0)

    def button_1_command():
        run_stored_procedure(canvas, entry_1, [1,3,4,5,6,7,8])

    button_image_1 = tk.PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = tk.Button(
        parent,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=button_1_command,
        relief="flat"
    )
    button_1.image = button_image_1
    button_1.place(x=121.0, y=321.0, width=94.0, height=94.0)

    image_button_1 = tk.PhotoImage(file=relative_to_assets("button_1.png"))
    canvas.button_1 = image_button_1

    image_star_1 = tk.PhotoImage(file=relative_to_assets("star_1.png"))
    canvas.star_1 = image_star_1

    # Load other images...

    # Rest of the code remains unchanged
    
    image_image_1 = tk.PhotoImage(file=relative_to_assets("image_1.png"))
    canvas.image_1 = image_image_1

    image_image_2 = tk.PhotoImage(file=relative_to_assets("image_2.png"))
    canvas.image_2 = image_image_2

    image_image_3 = tk.PhotoImage(file=relative_to_assets("image_3.png"))
    canvas.image_3 = image_image_3

    image_image_4 = tk.PhotoImage(file=relative_to_assets("image_4.png"))
    canvas.image_4 = image_image_4

    image_image_5 = tk.PhotoImage(file=relative_to_assets("image_5.png"))
    canvas.image_5 = image_image_5

    image_image_6 = tk.PhotoImage(file=relative_to_assets("image_6.png"))
    canvas.image_6 = image_image_6

    image_image_7 = tk.PhotoImage(file=relative_to_assets("image_7.png"))
    canvas.image_7 = image_image_7

    image_image_8 = tk.PhotoImage(file=relative_to_assets("image_8.png"))
    canvas.image_8 = image_image_8

    image_image_9 = tk.PhotoImage(file=relative_to_assets("image_9.png"))
    canvas.image_9 = image_image_9

    image_image_10 = tk.PhotoImage(file=relative_to_assets("image_10.png"))
    canvas.image_10 = image_image_10
    
    image_Rupee_1 = tk.PhotoImage(file=relative_to_assets("Rupee_1.png"))
    canvas.Rupee_1 = image_Rupee_1

    # Create images on canvas
    canvas.create_image(558.0, 85.0, image=image_image_1)
    canvas.create_image(157.0, 83.0, image=image_image_2)
    canvas.create_image(506.824951171875, 434.6396484375, image=image_image_3)
    canvas.create_image(909.0, 300.0, image=image_image_4)
    canvas.create_image(176.0, 490.0, image=image_image_5)
    canvas.create_image(568.0, 491.0, image=image_image_6)
    canvas.create_image(960.0, 491.0, image=image_image_7)
    canvas.create_image(171.925048828125, 609.7978515625, image=image_image_8)
    canvas.create_image(559.4249267578125, 609.7978515625, image=image_image_9)
    canvas.create_image(946.925048828125, 609.7978515625, image=image_image_10)

    canvas.create_text(426.0, 42.0, anchor="nw", text="My_Madness", fill="#000000",
                       font=("Frijole", 64 * -1))

    canvas.create_text(
        38.0,
        196.0,
        anchor="nw",
        text="Phone number:",
        fill="#000000",
        font=("Lemon Regular", 20 * -1)
    )

    canvas.create_text(
        735.0,
        233.0,
        anchor="nw",
        text="Name",
        fill="#000000",
        font=("LexendZetta Regular", 20 * -1)
    )

    canvas.create_text(
        48.0,
        441.0,
        anchor="nw",
        text="Total_Lone",
        fill="#000000",
        font=("LexendZetta Regular", 15 * -1)
    )

    canvas.create_text(
        48.0,
        560.0,
        anchor="nw",
        text="Number of Bags",
        fill="#000000",
        font=("LexendZetta Regular", 15 * -1)
    )

    canvas.create_text(
        442.0,
        442.0,
        anchor="nw",
        text="Rent",
        fill="#000000",
        font=("LexendZetta Regular", 15 * -1)
    )

    canvas.create_text(
        836.0,
        445.0,
        anchor="nw",
        text="Asset_Value",
        fill="#000000",
        font=("LexendZetta Regular", 15 * -1)
    )

    canvas.create_text(
        435.0,
        560.0,
        anchor="nw",
        text="Item",
        fill="#000000",
        font=("LexendZetta Regular", 15 * -1)
    )

    canvas.create_text(
        822.0,
        560.0,
        anchor="nw",
        text="Year’s",
        fill="#000000",
        font=("LexendZetta Regular", 15 * -1)
    )
    
    button_open_popup_Star_1 = tk.PhotoImage(file=relative_to_assets("Star_1.png"))
    button_open_popup = tk.Button(
        parent,
        image=button_open_popup_Star_1,
        borderwidth=0,
        highlightthickness=0,
        background="#FFEBA3",
        command=lambda: open_popup(parent,FarmerID),
        relief="flat"
    )
    button_open_popup.image = button_open_popup_Star_1
    button_open_popup.place(x=46.0, y=458.0,width=42, height=45)

# Function to create a popup
def open_popup(parent, FarmerID):
    if FarmerID is not None:
        popup = Toplevel(parent)
        popup.title("Popup Window")
        #popup.geometry("400x300")
        canvas = tk.Canvas(popup, bg="#FFFFFF", height=550, width=1200)
        canvas.pack()
        label = tk.Label(popup, text="This is a popup window")
        label.pack()
        popup.transient(parent)  # Set the popup to be transient to the parent window
        popup.grab_set()  # Prevent interaction with the parent window while the popup is open
        
         # Create a canvas in the popup
        #canvas = tk.Canvas(popup, bg="#FFFFFF", height=400, width=400)
        #canvas.pack()

    # Use global images in the popup
        canvas.create_image(50, 10, anchor="nw", image=image_image_1)
        canvas.create_image(55, 13, anchor="nw", image=image_image_2)
        #canvas.create_image(60, 150, anchor="nw", image=image_Rupee_1)
        
        # Create content for loan procedure
        create_loan_content(popup, FarmerID)  # Pass FarmerID as an argument

# Function to execute LoanI procedure
def execute_loan_procedure(FarmerID, entry_12, entry_13, entry_14, entry_15, entry_16, entry_17, entry_18):
    try:
        BondNumber = entry_12.get()
        AvgBagWeight = entry_13.get()
        MarketPrise = entry_14.get()
        LoanForBag = entry_15.get()
        AmountSanctioned = entry_16.get()
        RequestDate = entry_17.get()
        ApproveDate = entry_18.get()
        BankID = dropdown_values_4[dropdown_var_4.get()]
        
        with conn.cursor() as cursor:
            cursor.execute("EXEC LoanI @BankID=?, @BondNumber=?, @AvgBagWeight=?, @MarketPrise=?, @LoanForBag=?, @AmountSanctioned=?, @RequestDate=?, @ApproveDate=?, @FarmerID=?", 
                           (BankID, BondNumber, AvgBagWeight, MarketPrise, LoanForBag, AmountSanctioned, RequestDate, ApproveDate, FarmerID))
        
        conn.commit()  # Commit the transaction
        messagebox.showinfo("Success", "Loan procedure executed successfully!")
    
    except Exception as e:
        conn.rollback()  # Rollback the transaction in case of error
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to create content for loan procedure
def create_loan_content(popup, FarmerID):
    label_dropdown_21 = tk.Label(popup, text="Bank:", font=('Arial', 14), background='#05d7ff')
    label_dropdown_21.place(x=650, y=135)  # Adjusted coordinates

    global dropdown_var_4
    dropdown_var_4 = tk.StringVar()
    dropdown_4 = ttk.Combobox(popup, textvariable=dropdown_var_4, state='readonly')
    dropdown_4["values"] = list(dropdown_values_4.keys())
    dropdown_4.current(0)  # Set default selection
    dropdown_4.config(font=('Arial', 25, 'bold'), foreground='BLACK')
    dropdown_4.place(x=650, y=160, width=250, height=50)  # Adjusted coordinates
    dropdown_4.bind('<<ComboboxSelected>>', dropdown_changed)
    
    create_loan_entry_fields(popup)

# Function to create entry fields for loan procedure
def create_loan_entry_fields(popup):
    # Create a label for the bond number
    label_dropdown_14 = tk.Label(popup, text="బాండ్_సంఖ్య:", font=('Arial', 14), background='#8DF8D2')
    label_dropdown_14.place(x=60, y=135)  # Adjusted coordinates
    
    global entry_12
    entry_12 = tk.Entry(popup, bd=0, bg="#8DF8D2", fg="#000716", font=('Arial', 25), highlightthickness=0)
    entry_12.place(x=60.0, y=160.0, width=194.0, height=64.0)
    
    # Create a label for the average bag weight
    label_dropdown_15 = tk.Label(popup, text="సగటు_బస్తా_బరువు:", font=('Arial', 14), background='#8DF8D2')
    label_dropdown_15.place(x=360, y=135)  # Adjusted coordinates
    
    global entry_13
    entry_13 = tk.Entry(popup, bd=0, bg="#8DF8D2", fg="#000716", font=('Arial', 25), highlightthickness=0)
    entry_13.place(x=360.0, y=160.0, width=194.0, height=64.0)

    # Create a label for the market price
    label_dropdown_16 = tk.Label(popup, text="మార్కెట్_ధర/క్వింటా:", font=('Arial', 14), background='#8DF8D2')
    label_dropdown_16.place(x=48, y=313)  # Adjusted coordinates
    
    global entry_14
    entry_14 = tk.Entry(popup, bd=0, bg="#8DF8D2", fg="#000716", font=('Arial', 25), highlightthickness=0)
    entry_14.place(x=48.0, y=340.0, width=170.0, height=50.0)

    # Create a label for the loan type
    label_dropdown_17 = tk.Label(popup, text="రుణం/బస్తా:", font=('Arial', 14), background='#8DF8D2')
    label_dropdown_17.place(x=360, y=313)  # Adjusted coordinates
    
    global entry_15
    entry_15 = tk.Entry(popup, bd=0, bg="#8DF8D2", fg="#000716", font=('Arial', 25), highlightthickness=0)
    entry_15.place(x=360.0, y=340.0, width=170.0, height=50.0)

    # Create a label for the sanctioned amount
    label_dropdown_18 = tk.Label(popup, text="రుణం మంజూరైన మొత్తం:", font=('Arial', 14), background='#8DF8D2')
    label_dropdown_18.place(x=660, y=313)  # Adjusted coordinates
    
    global entry_16
    entry_16 = tk.Entry(popup, bd=0, bg="#8DF8D2", fg="#000716", font=('Arial', 25), highlightthickness=0)
    entry_16.place(x=660.0, y=340.0, width=170.0, height=50.0)

    # Create a label for the request date
    label_dropdown_19 = tk.Label(popup, text="అభ్యర్థన తేదీ:", font=('Arial', 14), background='#8DF8D2')
    label_dropdown_19.place(x=240, y=413)  # Adjusted coordinates
    
    global entry_17
    entry_17 = tk.Entry(popup, bd=0, bg="#8DF8D2", fg="#000716", font=('Arial', 25), highlightthickness=0)
    entry_17.place(x=240.0, y=440.0, width=170.0, height=50.0)

    # Create a label for the approve date
    label_dropdown_20 = tk.Label(popup, text="ఆమోదించబడిన తేదీ:", font=('Arial', 14), background='#8DF8D2')
    label_dropdown_20.place(x=628, y=413)  # Adjusted coordinates
    
    global entry_18
    entry_18 = tk.Entry(popup, bd=0, bg="#8DF8D2", fg="#000716", font=('Arial', 25), highlightthickness=0)
    entry_18.place(x=628.0, y=440.0, width=170.0, height=50.0)

    # Create button to execute LoanI procedure
    button_execute = tk.Button(popup, text="Execute Loan", font=('Arial', 18), command=lambda: execute_loan_procedure(FarmerID, entry_12, entry_13, entry_14, entry_15, entry_16, entry_17, entry_18))
    button_execute.place(x=950, y=160, width=170.0, height=50.0)

    # Create button to close popup window
    button_close_popup = tk.Button(popup, text="Close Popup", font=('Arial', 18), command=popup.destroy)
    button_close_popup.place(x=950, y=300, width=170.0, height=50.0)

# Function to handle dropdown selection change
def dropdown_changed(event):
    if str(event.widget) == str(dropdown_var_4):
        selected_text = dropdown_var_4.get()
        code_value = dropdown_values_4[selected_text]
        print(f"The selected code value for '{selected_text}' is: {code_value}")
        
#=============================================================================================================================================================================

# Function to create content for Page 2
def create_page2_content(parent):
    canvas = tk.Canvas(parent, bg="#FFFFFF", height=709, width=1116)
    canvas.pack()

def run_stored_procedure_2(canvas, entry_widget, transaction_type_id=None, first_name=None, phone=None, item_id=None, variety_id=None, kana_block_map_id=None, no_of_bags=None):
    try:
        # Get values from entry fields
        first_name = first_name or entry_2.get()
        phone = phone or entry_3.get()
        no_of_bags = no_of_bags or entry_4.get()

        # Get selected values from dropdowns
        item_id = dropdown_values[dropdown_var_1.get()]  # Corrected line
        variety_id = dropdown_values_2[dropdown_var_2.get()]  # Corrected line
        kana_block_map_id = dropdown_values_3[dropdown_var_3.get()]  # Corrected line

        # Execute stored procedure
        with conn.cursor() as cursor:
            cursor.execute("EXEC dbo.TransactionI @FirstName=?, @Phone=?, @TransactionTypeID=?, @ItemID=?, @VarietyID=?, @KanaBlockMapID=?, @NoOfBags=?", 
                           (first_name, phone, transaction_type_id, item_id, variety_id, kana_block_map_id, 
                            no_of_bags))

        messagebox.showinfo("Success", "Stored procedure executed successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# Define the options for the dropdown menus

dropdown_values = {
    "MIRCHI": "8",
    "SENAGALU": "9",
    "MOKKAJONNA": "13",
    "Kandulu": "10",
    "Pasupu": "11",
    "Chintapandu": "12",
    "Bellam": "14"
}

dropdown_values_2 = {
    "Nellurisannalu": "1",
    "talu kayalu": "2",
    "delux": "3",
    "popcorn": "4",
    "Black": "5",
    "22": "6"
}

dropdown_values_3 = {
   "100(A)":"2", "101(A)":"3", "102(A)":"4", "103(A)":"5", "104(A)":"6", "105(A)":"7", "106(A)":"8", "107(A)":"9", "108(A)":"10", "109(A)":"11", "110(A)":"12", "111(A)":"13", "112(A)":"14", "113(A)":"15", "114(A)":"16", "115(A)":"17", "116(A)":"18", "117(A)":"19", "118(A)":"20", "119(A)":"21", 
"120(A)":"22", "121(A)":"23", "122(A)":"24", "123(A)":"25", "124(A)":"26", "125(A)":"27", "126(A)":"28", "127(A)":"29", "128(A)":"30", "129(A)":"31", "130(A)":"32", "131(A)":"33", "132(A)":"34", "133(A)":"35", "134(A)":"36", "135(A)":"37", "136(A)":"38", "137(A)":"39", "138(A)":"40", "139(A)":"41", 
"140(A)":"42", "141(A)":"43", "142(A)":"44", "143(A)":"45", "144(A)":"46", "145(A)":"47", "146(A)":"48", "147(A)":"49", "148(A)":"50", "149(A)":"51", "150(A)":"52", "300(A)":"53", "301(A)":"54", "302(A)":"55", "303(A)":"56", "304(A)":"57", "305(A)":"58", "306(A)":"59", "307(A)":"60", "308(A)":"61", 
"309(A)":"62", "310(A)":"63", "311(A)":"64", "312(A)":"65", "313(A)":"66", "314(A)":"67", "315(A)":"68", "316(A)":"69", "317(A)":"70", "318(A)":"71", "319(A)":"72", "320(A)":"73", "321(A)":"74", "322(A)":"75", "323(A)":"76", "324(A)":"77", "325(A)":"78", "326(A)":"79", "327(A)":"80", "328(A)":"81", 
"329(A)":"82", "330(A)":"83", "331(A)":"84", "332(A)":"85", "333(A)":"86", "334(A)":"87", "335(A)":"88", "336(A)":"89", "337(A)":"90", "338(A)":"91", "339(A)":"92", "340(A)":"93", "341(A)":"94", "342(A)":"95", "343(A)":"96", "344(A)":"97", "345(A)":"98", "346(A)":"99", "347(A)":"100", "348(A)":"101", 
"349(A)":"102", "350(A)":"103", "400(A)":"104", "401(A)":"105", "402(A)":"106", "403(A)":"107", "404(A)":"108", "405(A)":"109", "406(A)":"110", "407(A)":"111", "408(A)":"112", "409(A)":"113", "410(A)":"114", "411(A)":"115", "412(A)":"116", "413(A)":"117", "414(A)":"118", "415(A)":"119", "416(A)":"120", 
"417(A)":"121", "418(A)":"122", "419(A)":"123", "420(A)":"124", "421(A)":"125", "422(A)":"126", "423(A)":"127", "424(A)":"128", "425(A)":"129", "426(A)":"130", "427(A)":"131", "428(A)":"132", "429(A)":"133", "430(A)":"134", "431(A)":"135", "432(A)":"136", "433(A)":"137", "434(A)":"138", "435(A)":"139", 
"436(A)":"140", "437(A)":"141", "438(A)":"142", "439(A)":"143", "440(A)":"144", "441(A)":"145", "442(A)":"146", "443(A)":"147", "444(A)":"148", "445(A)":"149", "446(A)":"150", "447(A)":"151", "448(A)":"152", "449(A)":"153", "450(A)":"154", "500(A)":"155", "501(A)":"156", "502(A)":"157", "503(A)":"158", 
"504(A)":"159", "505(A)":"160", "506(A)":"161", "507(A)":"162", "508(A)":"163", "509(A)":"164", "510(A)":"165", "511(A)":"166", "512(A)":"167", "513(A)":"168", "514(A)":"169", "515(A)":"170", "516(A)":"171", "517(A)":"172", "518(A)":"173", "519(A)":"174", "520(A)":"175", "521(A)":"176", "522(A)":"177", 
"523(A)":"178", "524(A)":"179", "525(A)":"180", "526(A)":"181", "527(A)":"182", "528(A)":"183", "529(A)":"184", "530(A)":"185", "531(A)":"186", "532(A)":"187", "533(A)":"188", "534(A)":"189", "535(A)":"190", "536(A)":"191", "537(A)":"192", "538(A)":"193", "539(A)":"194", "540(A)":"195", "541(A)":"196", 
"542(A)":"197", "543(A)":"198", "544(A)":"199", "545(A)":"200", "546(A)":"201", "547(A)":"202", "548(A)":"203", "549(A)":"204", "550(A)":"205", "600(A)":"206", "601(A)":"207", "602(A)":"208", "603(A)":"209", "604(A)":"210", "605(A)":"211", "606(A)":"212", "607(A)":"213", "608(A)":"214", "609(A)":"215", 
"610(A)":"216", "611(A)":"217", "612(A)":"218", "613(A)":"219", "614(A)":"220", "615(A)":"221", "616(A)":"222", "617(A)":"223", "618(A)":"224", "619(A)":"225", "620(A)":"226", "621(A)":"227", "622(A)":"228", "623(A)":"229", "624(A)":"230", "625(A)":"231", "626(A)":"232", "627(A)":"233", "628(A)":"234", 
"629(A)":"235", "630(A)":"236", "631(A)":"237", "632(A)":"238", "633(A)":"239", "634(A)":"240", "635(A)":"241", "636(A)":"242", "637(A)":"243", "638(A)":"244", "639(A)":"245", "640(A)":"246", "641(A)":"247", "642(A)":"248", "643(A)":"249", "644(A)":"250", "645(A)":"251", "646(A)":"252", "647(A)":"253", 
"648(A)":"254", "649(A)":"255", "650(A)":"256", "201(A)":"257", "202(A)":"258", "203(A)":"259", "204(A)":"260", "205(A)":"261", "206(A)":"262", "207(A)":"263", "208(A)":"264", "209(A)":"265", "210(A)":"266", "211(A)":"267", "212(A)":"268", "213(A)":"269", "214(A)":"270", "215(A)":"271", "216(A)":"272", 
"217(A)":"273", "218(A)":"274", "219(A)":"275", "220(A)":"276", "221(A)":"277", "222(A)":"278", "223(A)":"279", "224(A)":"280", "225(A)":"281", "226(A)":"282", "227(A)":"283", "228(A)":"284", "229(A)":"285", "230(A)":"286", "231(A)":"287", "232(A)":"288", "233(A)":"289", "234(A)":"290", "235(A)":"291", 
"236(A)":"292", "237(A)":"293", "238(A)":"294", "239(A)":"295", "240(A)":"296", "241(A)":"297", "242(A)":"298", "243(A)":"299", "404(A)":"300", "448(B)":"451", "449(B)":"452", "450(B)":"453", "500(B)":"454", "501(B)":"455",
"502(B)":"456", "503(B)":"457", "504(B)":"458", "505(B)":"459", "506(B)":"460",
"507(B)":"461", "508(B)":"462", "509(B)":"463", "510(B)":"464", "511(B)":"465",
"512(B)":"466", "513(B)":"467", "514(B)":"468", "515(B)":"469", "516(B)":"470",
"517(B)":"471", "518(B)":"472", "519(B)":"473", "520(B)":"474", "521(B)":"475",
"522(B)":"476", "523(B)":"477", "524(B)":"478", "525(B)":"479", "526(B)":"480",
"527(B)":"481", "528(B)":"482", "529(B)":"483", "530(B)":"484", "531(B)":"485",
"532(B)":"486", "533(B)":"487", "534(B)":"488", "535(B)":"489", "536(B)":"490",
"537(B)":"491", "538(B)":"492", "539(B)":"493", "540(B)":"494", "541(B)":"495",
"542(B)":"496", "543(B)":"497", "544(B)":"498", "545(B)":"499", "546(B)":"500",
"547(B)":"501", "548(B)":"502", "549(B)":"503", "550(B)":"504", "600(B)":"505",
"601(B)":"506", "602(B)":"507", "603(B)":"508", "604(B)":"509", "605(B)":"510",
"606(B)":"511", "607(B)":"512", "608(B)":"513", "609(B)":"514", "610(B)":"515",
"611(B)":"516", "612(B)":"517", "613(B)":"518", "614(B)":"519", "615(B)":"520",
"616(B)":"521", "617(B)":"522", "618(B)":"523", "619(B)":"524", "620(B)":"525",
"621(B)":"526", "622(B)":"527", "623(B)":"528", "624(B)":"529", "625(B)":"530",
"626(B)":"531", "627(B)":"532", "628(B)":"533", "629(B)":"534", "630(B)":"535",
"631(B)":"536", "632(B)":"537", "633(B)":"538", "634(B)":"539", "635(B)":"540",
"636(B)":"541", "637(B)":"542", "638(B)":"543", "639(B)":"544", "640(B)":"545",
"641(B)":"546", "642(B)":"547", "643(B)":"548", "644(B)":"549", "645(B)":"550",
"646(B)":"551", "647(B)":"552", "648(B)":"553", "649(B)":"554", "650(B)":"555",
"201(B)":"556", "202(B)":"557", "203(B)":"558", "204(B)":"559", "205(B)":"560",
"206(B)":"561", "207(B)":"562", "208(B)":"563", "209(B)":"564", "210(B)":"565",
"211(B)":"566", "212(B)":"567", "213(B)":"568", "214(B)":"569", "215(B)":"570",
"216(B)":"571", "217(B)":"572", "218(B)":"573", "219(B)":"574", "220(B)":"575",
"221(B)":"576", "222(B)":"577", "223(B)":"578", "224(B)":"579", "225(B)":"580",
"226(B)":"581", "227(B)":"582", "228(B)":"583", "229(B)":"584", "230(B)":"585",
"231(B)":"586", "232(B)":"587", "233(B)":"588", "234(B)":"589", "235(B)":"590",
"236(B)":"591", "237(B)":"592", "238(B)":"593", "239(B)":"594", "240(B)":"595",
"241(B)":"596", "242(B)":"597", "243(B)":"598", "244(B)":"599", "100(C)":"600",
"101(C)":"601", "102(C)":"602", "103(C)":"603", "104(C)":"604", "105(C)":"605",
"106(C)":"606", "107(C)":"607", "108(C)":"608", "109(C)":"609", "110(C)":"610",
"111(C)":"611", "112(C)":"612", "113(C)":"613", "114(C)":"614", "115(C)":"615",
"116(C)":"616", "117(C)":"617", "118(C)":"618", "119(C)":"619", "120(C)":"620",
"121(C)":"621", "122(C)":"622", "123(C)":"623", "124(C)":"624", "125(C)":"625",
"126(C)":"626", "127(C)":"627", "128(C)":"628", "129(C)":"629", "130(C)":"630",
"131(C)":"631", "132(C)":"632", "133(C)":"633", "134(C)":"634", "135(C)":"635",
"136(C)":"636", "137(C)":"637", "138(C)":"638", "139(C)":"639", "140(C)":"640",
"141(C)":"641", "142(C)":"642", "143(C)":"643", "144(C)":"644", "145(C)":"645",
"146(C)":"646", "147(C)":"647", "148(C)":"648", "149(C)":"649", "150(C)":"650",
"300(C)":"651", "301(C)":"652", "302(C)":"653", "303(C)":"654", "304(C)":"655",
"305(C)":"656", "306(C)":"657", "307(C)":"658", "308(C)":"659", "309(C)":"660",
"310(C)":"661", "311(C)":"662", "312(C)":"663", "313(C)":"664", "314(C)":"665",
"315(C)":"666", "316(C)":"667", "317(C)":"668", "318(C)":"669", "319(C)":"670",
"320(C)":"671", "321(C)":"672", "322(C)":"673", "323(C)":"674", "324(C)":"675",
"325(C)":"676", "326(C)":"677", "327(C)":"678", "328(C)":"679", "329(C)":"680",
"330(C)":"681", "331(C)":"682", "332(C)":"683", "333(C)":"684", "334(C)":"685",
"335(C)":"686", "336(C)":"687", "337(C)":"688", "338(C)":"689", "339(C)":"690",
"340(C)":"691", "341(C)":"692", "342(C)":"693", "343(C)":"694", "344(C)":"695",
"345(C)":"696", "346(C)":"697", "347(C)":"698", "348(C)":"699", "349(C)":"700",
"350(C)":"701", "400(C)":"702", "401(C)":"703", "402(C)":"704", "403(C)":"705",
"404(C)":"706", "405(C)":"707", "406(C)":"708", "407(C)":"709", "408(C)":"710",
"409(C)":"711", "410(C)":"712", "411(C)":"713", "412(C)":"714", "413(C)":"715",
"414(C)":"716", "415(C)":"717", "416(C)":"718", "417(C)":"719", "418(C)":"720",
"419(C)":"721", "420(C)":"722", "421(C)":"723", "422(C)":"724", "423(C)":"725",
"424(C)":"726", "425(C)":"727", "426(C)":"728", "427(C)":"729", "428(C)":"730",
"429(C)":"731", "430(C)":"732", "431(C)":"733", "432(C)":"734", "433(C)":"735",
"434(C)":"736", "435(C)":"737", "436(C)":"738", "437(C)":"739", "438(C)":"740",
"439(C)":"741", "440(C)":"742", "441(C)":"743", "442(C)":"744", "443(C)":"745",
"444(C)":"746", "445(C)":"747", "446(C)":"748", "447(C)":"749", "448(C)":"750",
"449(C)":"751", "450(C)":"752", "500(C)":"753", "501(C)":"754", "502(C)":"755",
"503(C)":"756", "504(C)":"757", "505(C)":"758", "506(C)":"759", "507(C)":"760",
"508(C)":"761", "509(C)":"762", "510(C)":"763", "511(C)":"764", "512(C)":"765",
"513(C)":"766", "514(C)":"767", "515(C)":"768", "516(C)":"769", "517(C)":"770",
"518(C)":"771", "519(C)":"772", "520(C)":"773", "521(C)":"774", "522(C)":"775",
"523(C)":"776", "524(C)":"777", "525(C)":"778", "526(C)":"779", "527(C)":"780",
"528(C)":"781", "529(C)":"782", "530(C)":"783", "531(C)":"784", "532(C)":"785",
"533(C)":"786", "534(C)":"787", "535(C)":"788", "536(C)":"789", "537(C)":"790",
"538(C)":"791", "539(C)":"792", "540(C)":"793", "541(C)":"794", "542(C)":"795",
"543(C)":"796", "544(C)":"797", "545(C)":"798", "546(C)":"799", "547(C)":"800",
"548(C)":"801", "549(C)":"802", "550(C)":"803", "600(C)":"804", "601(C)":"805",
"602(C)":"806", "603(C)":"807", "604(C)":"808", "605(C)":"809", "606(C)":"810",
"607(C)":"811", "608(C)":"812", "609(C)":"813", "610(C)":"814", "611(C)":"815",
"612(C)":"816", "613(C)":"817", "614(C)":"818", "615(C)":"819", "616(C)":"820",
"617(C)":"821", "618(C)":"822", "619(C)":"823", "620(C)":"824", "621(C)":"825",
"622(C)":"826", "623(C)":"827", "624(C)":"828", "625(C)":"829", "626(C)":"830",
"627(C)":"831", "628(C)":"832", "629(C)":"833", "630(C)":"834", "631(C)":"835",
"632(C)":"836", "633(C)":"837", "634(C)":"838", "635(C)":"839", "636(C)":"840",
"637(C)":"841", "638(C)":"842", "639(C)":"843", "640(C)":"844", "641(C)":"845",
"642(C)":"846", "643(C)":"847", "644(C)":"848", "645(C)":"849", "646(C)":"850",
"647(C)":"851", "648(C)":"852", "649(C)":"853", "650(C)":"854", "201(C)":"855",
"202(C)":"856", "203(C)":"857", "204(C)":"858", "205(C)":"859", "206(C)":"860",
"207(C)":"861", "208(C)":"862", "209(C)":"863", "210(C)":"864", "211(C)":"865",
"212(C)":"866", "213(C)":"867", "214(C)":"868", "215(C)":"869", "216(C)":"870",
"217(C)":"871", "218(C)":"872", "219(C)":"873", "220(C)":"874", "221(C)":"875",
"222(C)":"876", "223(C)":"877", "224(C)":"878", "225(C)":"879", "226(C)":"880",
"227(C)":"881", "228(C)":"882", "229(C)":"883", "230(C)":"884", "231(C)":"885",
"232(C)":"886", "233(C)":"887", "234(C)":"888", "235(C)":"889", "236(C)":"890",
"237(C)":"891", "238(C)":"892", "239(C)":"893", "240(C)":"894", "241(C)":"895",
"242(C)":"896", "243(C)":"897", "244(C)":"898"}


#dropdown_options_1 = ['MIRCHY', 'SAMAGALU', 'MOKKAJONNA', 'Kandulu', 'Pasapu', 'Chintapandu', 'Bellam']
#dropdown_options_2 = ['Nallurisannalu', 'talu kayalu', 'delux', 'popcorn', 'Black', 'Teja', '22']
#dropdown_options_3 = ['100', '200', '300', '400', '500', '600', '700']

# Import statements...

# Define your functions...

def dropdown_changed(event):
    if str(event.widget) == str(dropdown_var_1):
        selected_text = dropdown_var_1.get()
        code_value = dropdown_values[selected_text]
        print(f"The selected code value for '{selected_text}' is: {code_value}")


def create_page2_content(parent):
    canvas = tk.Canvas(parent, bg="#FFFFFF", height=709, width=1116)
    canvas.pack()

    # Define button colors
    color1 = '#020f12'
    color2 = '#05d7ff'
    color3 = '#65e7ff'
    color4 = 'BLACK'

    # Rest of your code...

    # Existing code...

    def button1_command():
        # Get the value from entry_8 widget
        input_value_8 = 1
        
        # Call the run_stored_procedure function with appropriate parameters for Page 2
        selected_item_id = dropdown_values[dropdown_var_1.get()]
        selected_variety_id = dropdown_values_2[dropdown_var_2.get()]
        selected_kana_block_id = dropdown_values_3[dropdown_var_3.get()]
        run_stored_procedure_2(canvas, entry_2, transaction_type_id="1", first_name=entry_2.get(), phone=entry_3.get(), item_id=selected_item_id, variety_id=selected_variety_id, kana_block_map_id=selected_kana_block_id, no_of_bags=entry_4.get())


    def button2_command():
        # Get the value from entry_8 widget
        input_value_8 = 2
        
        # Call the run_stored_procedure function with appropriate parameters for Page 2
        selected_item_id = dropdown_values[dropdown_var_1.get()]
        selected_variety_id = dropdown_values_2[dropdown_var_2.get()]
        selected_kana_block_id = dropdown_values_3[dropdown_var_3.get()]
        run_stored_procedure_2(canvas, entry_2, transaction_type_id="2", first_name=entry_2.get(), phone=entry_3.get(), item_id=selected_item_id, variety_id=selected_variety_id, kana_block_map_id=selected_kana_block_id, no_of_bags=entry_4.get())


    # Rest of your code...

    # Create buttons with appropriate commands
    button1 = tk.Button(
        parent,
        background=color2,
        foreground=color4,
        activebackground=color3,
        activeforeground=color4,
        highlightthickness=2,
        highlightbackground=color2,
        highlightcolor='WHITE',
        width=13,
        height=2,
        bd=0,
        cursor='hand2',
        text='Checkin',
        font=('Arial', 16, 'bold'),
        command=button1_command
    )
    button1.place(x=400, y=600)

    button2 = tk.Button(
        parent,
        background=color1,
        foreground=color2,
        activebackground=color3,
        activeforeground=color4,
        highlightthickness=2,
        highlightbackground=color2,
        highlightcolor='WHITE',
        width=13,
        height=2,
        bd=0,
        cursor='hand2',
        text='Checkout',
        font=('Arial', 16, 'bold'),
        command=button2_command
    )
    button2.place(x=600, y=600)


    # Existing code...

# Create main window and other widgets...


    
   # Create images on canvas
    global image_image_1,image_image_2,image_image_3
    
    # Load images
    image_image_1 = tk.PhotoImage(file=relative_to_assets("image_1.png"))
    image_image_2 = tk.PhotoImage(file=relative_to_assets("image_2.png"))
    image_image_3 = tk.PhotoImage(file=relative_to_assets("image_3.png"))
    
    canvas.create_image(558.0, 85.0, image=image_image_1)
    canvas.create_image(157.0, 83.0, image=image_image_2)
    canvas.create_image(506.824951171875, 434.6396484375, image=image_image_3)


    # Create a label for the dropdown
    label_dropdown = tk.Label(parent, text="Item:", font=('Arial', 14), background='#05d7ff')
    label_dropdown.place(x=750, y=247)  # Adjusted coordinates

    # Create a dropdown menu
    global dropdown_var_1
    dropdown_var_1 = tk.StringVar()
    dropdown_1 = ttk.Combobox(parent, textvariable=dropdown_var_1, state='readonly')
    dropdown_1["values"] = list(dropdown_values.keys())
    dropdown_1.current(0)  # Set default selection
    dropdown_1.config(font=('Arial', 25, 'bold'), foreground='BLACK')  # Change font size and color
    dropdown_1.place(x=750.0, y=272.0, width=250, height=50)  # Adjust the coordinates and size
    dropdown_1.bind('<<ComboboxSelected>>', dropdown_changed)

    # Create a label for the dropdown
    label_dropdown_2 = tk.Label(parent, text="Variety:", font=('Arial', 14), background='#05d7ff')
    label_dropdown_2.place(x=750, y=375)  # Adjusted coordinates

    # Create 2nd dropdown menu for Variety
    global dropdown_var_2
    dropdown_var_2 = tk.StringVar()
    dropdown_2 = ttk.Combobox(parent, textvariable=dropdown_var_2, state='readonly')
    dropdown_2["values"] = list(dropdown_values_2.keys())
    dropdown_2.current(0)  # Set default selection
    dropdown_2.config(font=('Arial', 25, 'bold'), foreground='BLACK')
    dropdown_2.place(x=750, y=400, width=250, height=50)  # Adjusted coordinates and size
    dropdown_2.bind('<<ComboboxSelected>>', dropdown_changed)

    # Create a label for the dropdown
    label_dropdown_3 = tk.Label(parent, text="KanaBlock:", font=('Arial', 14), background='#05d7ff')
    label_dropdown_3.place(x=750, y=475)  # Adjusted coordinates

    # Create 2nd dropdown menu for KanaBlock
    global dropdown_var_3
    dropdown_var_3 = tk.StringVar()
    dropdown_3 = ttk.Combobox(parent, textvariable=dropdown_var_3, state='readonly')
    dropdown_3["values"] = list(dropdown_values_3.keys())
    dropdown_3.current(0)  # Set default selection
    dropdown_3.config(font=('Arial', 25, 'bold'), foreground='BLACK')
    dropdown_3.place(x=750, y=500, width=250, height=50)  # Adjusted coordinates and size
    dropdown_3.bind('<<ComboboxSelected>>', dropdown_changed)
    
    # Existing code...

  
 
    # Create a label for the dropdown
    label_dropdown_4 = tk.Label(parent, text="Name:", font=('Arial', 14), background='#05d7ff')
    label_dropdown_4.place(x=25, y=205)  # Adjusted coordinates
    
    global entry_2
    entry_2 = tk.Entry(parent, bd=0, bg="#D9D9D9", fg="#000716", font=('Arial', 25), highlightthickness=0)
    entry_2.place(x=25.0, y=234.0, width=294.0, height=64.0)
    
    # Create a label for the dropdown
    label_dropdown_5 = tk.Label(parent, text="Phone Number:", font=('Arial', 14), background='#05d7ff')
    label_dropdown_5.place(x=25, y=308)  # Adjusted coordinates
    
    global entry_3
    entry_3 = tk.Entry(parent, bd=0, bg="#D9D9D9", fg="#000716", font=('Arial', 25), highlightthickness=0)
    entry_3.place(x=25.0, y=334.0, width=294.0, height=64.0)
    
    # Create a label for the dropdown
    label_dropdown_6 = tk.Label(parent, text="Number of Bags:", font=('Arial', 14), background='#05d7ff')
    label_dropdown_6.place(x=25, y=408)  # Adjusted coordinates
    
    global entry_4
    entry_4 = tk.Entry(parent, bd=0, bg="#D9D9D9", fg="#000716", font=('Arial', 25), highlightthickness=0)
    entry_4.place(x=25.0, y=434.0, width=294.0, height=64.0)


#==========================================================================================================================

def run_stored_procedure_3(canvas, entry_widget, FirstName=None, LastName=None, Village=None, Mandal=None, PANNumber=None, Phone=None, Aadhar=None):
    try:
        # Get values from entry fields
        FirstName = entry_5.get()
        LastName = entry_6.get()
        Village = entry_7.get()
        Mandal = entry_8.get()
        PANNumber = entry_9.get()
        Phone = entry_10.get()
        Aadhar = entry_11.get()

        
        # Execute stored procedure
        with conn.cursor() as cursor:
            cursor.execute("EXEC dbo.FarmerI @FirstName=?, @LastName=?, @Village=?, @Mandal=?, @PANNumber=?, @Phone=?, @Aadhar=?", 
                           (FirstName, LastName, Village, Mandal, PANNumber, Phone, 
                            Aadhar))

        messagebox.showinfo("Success", "Stored procedure executed successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

   
def create_page3_content(parent):
    canvas = tk.Canvas(parent, bg="#FFFFFF", height=709, width=1116)
    canvas.pack()
    
    def button_command():
        run_stored_procedure_3 (canvas, entry_6, FirstName=entry_5.get(),LastName = entry_6.get(),
        Village = entry_7.get(),
        Mandal = entry_8.get(),
        PANNumber = entry_9.get(),
        Phone = entry_10.get(),
        Aadhar = entry_11.get())
        
     # Create button_1 with the defined command
    button_image_1 = tk.PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = tk.Button(
        parent,
        background="#F5F5F5",
        activebackground="#F5F5F5",
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=button_command,
        relief="flat"
    )
    button_1.image = button_image_1
    button_1.place(x=990.0, y=230.0, width=94.0, height=94.0)

    
   # Load and store the images
    image_button_1 = tk.PhotoImage(file=relative_to_assets("button_1.png"))
    canvas.button_1 = image_button_1
    
    image_image_1 = tk.PhotoImage(file=relative_to_assets("image_1.png"))
    canvas.image_1 = image_image_1

    image_image_2 = tk.PhotoImage(file=relative_to_assets("image_2.png"))
    canvas.image_2 = image_image_2

    image_image_3 = tk.PhotoImage(file=relative_to_assets("image_3.png"))
    canvas.image_3 = image_image_3

    image_image_4 = tk.PhotoImage(file=relative_to_assets("image_4.png"))
    canvas.image_4 = image_image_4

    image_image_5 = tk.PhotoImage(file=relative_to_assets("image_5.png"))
    canvas.image_5 = image_image_5

    image_image_6 = tk.PhotoImage(file=relative_to_assets("image_6.png"))
    canvas.image_6 = image_image_6

    image_image_7 = tk.PhotoImage(file=relative_to_assets("image_7.png"))
    canvas.image_7 = image_image_7

    image_image_8 = tk.PhotoImage(file=relative_to_assets("image_8.png"))
    canvas.image_8 = image_image_8

    image_image_9 = tk.PhotoImage(file=relative_to_assets("image_9.png"))
    canvas.image_9 = image_image_9


    # Create images on canvas
    canvas.create_image(558.0, 85.0, image=image_image_1)
    canvas.create_image(157.0, 83.0, image=image_image_2)
    canvas.create_image(506.824951171875, 434.6396484375, image=image_image_3)
    canvas.create_image(750.0, 300.0, image=image_image_4)
    canvas.create_image(250.0, 300.0, image=image_image_4)
    canvas.create_image(171.0, 490.0, image=image_image_5)
    canvas.create_image(559.0, 491.0, image=image_image_6)
    canvas.create_image(946.0, 491.0, image=image_image_7)
    canvas.create_image(370.0, 609.7978515625, image=image_image_8)
    canvas.create_image(759.0, 609.7978515625, image=image_image_9)
    

    canvas.create_text(426.0, 42.0, anchor="nw", text="రైతు", fill="#000000",
                       font=("Frijole", 64 * -1))
    
    
     # Create a label for the First_Name
    label_dropdown_7 = tk.Label(parent, text="పేరు:", font=('Arial', 14), background='#A1F3FE')
    label_dropdown_7.place(x=60, y=207)  # Adjusted coordinates
    
    global entry_5
    entry_5 = tk.Entry(parent, bd=0, bg="#A1F3FE", fg="#000716", font=('Arial', 25), highlightthickness=0)
    entry_5.place(x=60.0, y=250.0, width=394.0, height=64.0)
    
     # Create a label for the Sir_Name
    label_dropdown_8 = tk.Label(parent, text="ఇంటిపేరు:", font=('Arial', 14), background='#A1F3FE')
    label_dropdown_8.place(x=560, y=207)  # Adjusted coordinates
    
    global entry_6
    entry_6 = tk.Entry(parent, bd=0, bg="#A1F3FE", fg="#000716", font=('Arial', 25), highlightthickness=0)
    entry_6.place(x=560.0, y=250.0, width=394.0, height=64.0)
    
    
    # Create a label for the Village
    label_dropdown_9 = tk.Label(parent, text="గ్రామం:", font=('Arial', 14), background='#FFEBA3')
    label_dropdown_9.place(x=48, y=410)  # Adjusted coordinates
    
    global entry_7
    entry_7 = tk.Entry(parent, bd=0, bg="#FFEBA3", fg="#000716", font=('Arial', 25), highlightthickness=0)
    entry_7.place(x=40.0, y=448.0, width=270.0, height=50.0)
    
     # Create a label for the Mandal or District
    label_dropdown_10 = tk.Label(parent, text="జిల్లా:", font=('Arial', 14), background='#F4A0E1')
    label_dropdown_10.place(x=433, y=413)  # Adjusted coordinates
    
    global entry_8
    entry_8 = tk.Entry(parent, bd=0, bg="#F4A0E1", fg="#000716", font=('Arial', 25), highlightthickness=0)
    entry_8.place(x=425.0, y=445.0, width=270.0, height=50.0)
    
     # Create a label for the PAN
    label_dropdown_11 = tk.Label(parent, text="PAN:", font=('Arial', 14), background='#A1F3FE')
    label_dropdown_11.place(x=813, y=413)  # Adjusted coordinates
    
    global entry_9
    entry_9 = tk.Entry(parent, bd=0, bg="#A1F3FE", fg="#000716", font=('Arial', 25), highlightthickness=0)
    entry_9.place(x=815.0, y=445.0, width=270.0, height=50.0)    
    
     # Create a label for the Phone_Number
    label_dropdown_12 = tk.Label(parent, text="ఫోన్ నంబర్:", font=('Arial', 14), background='#6EF16B')
    label_dropdown_12.place(x=240, y=530)  # Adjusted coordinates
    
    global entry_10
    entry_10 = tk.Entry(parent, bd=0, bg="#6EF16B", fg="#000716", font=('Arial', 25), highlightthickness=0)
    entry_10.place(x=240.0, y=568.0, width=270.0, height=50.0)
    
    # Create a label for the Aadhar
    label_dropdown_13 = tk.Label(parent, text="ఆధార్:", font=('Arial', 14), background='#8DF8D2')
    label_dropdown_13.place(x=628, y=530)  # Adjusted coordinates
    
    global entry_11
    entry_11 = tk.Entry(parent, bd=0, bg="#8DF8D2", fg="#000716", font=('Arial', 25), highlightthickness=0)
    entry_11.place(x=628.0, y=568.0, width=270.0, height=50.0)
    
    
#======================================================================================================    

# Function to create content for Page 4
def create_page4_content(parent):
    canvas = tk.Canvas(parent, bg="#FFFFFF", height=709, width=1116)
    canvas.pack()

    # Your content for Page 4 goes here
    pass

# Create main window
window = tk.Tk()
window.geometry("1116x709")
window.title("My Application")
window.configure(bg="#FFFFFF")

# Notebook widget to hold multiple pages
notebook = ttk.Notebook(window)
notebook.pack(expand=True, fill="both")

# Page 1
page1 = tk.Frame(notebook)
notebook.add(page1, text="Page 1")
create_page1_content(page1)

# Page 2
page2 = tk.Frame(notebook)
notebook.add(page2, text="Page 2")
create_page2_content(page2)

# Page 3
page3 = tk.Frame(notebook)
notebook.add(page3, text="Page 3")
create_page3_content(page3)

# Page 4
page4 = tk.Frame(notebook)
notebook.add(page4, text="Page 4")
create_page4_content(page4)

# Run the application
window.mainloop()
