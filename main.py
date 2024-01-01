import tkinter as tk
from tkinter import ttk
from PIL import Image as im
from PIL import Image, ImageTk
from tkinter import *
import Algorthims


# main screen
root = tk.Tk()
root.geometry('1300x800')
root.title('Romania Map Searching Problem')
root.configure(bg = 'white')

# *****************************************
bg_color = 'white'
text_color = 'black'
result_text_color = 'black'
frames_bg = 'white'
controls_label_width = 27

OM_style = ttk.Style()
OM_style.configure('my.TMenubutton', font=('Arial', 16))
# *****************************************

# main lbl
main_lbl = tk.Label(root, text="Romania Map, Searching Algorithms", bg = bg_color, foreground= '#de1b4a', font=('Arial', 30, 'bold'))
main_lbl.pack(pady=10)

# control panal and image frame
cont_img_frame = Frame(root)
cont_img_frame.pack()
cont_img_frame.configure(highlightbackground='black', highlightthickness=2, bg='white')

# Romania map:
path = r'Romanai_map.png'
map_image = im.open(path)
width, height = map_image.size
map_image = map_image.resize((int(width//1.6), int(height//1.6)))

can_img = Canvas(cont_img_frame, width=600, height=400, highlightthickness=2, highlightbackground='black', bg = 'white')
can_img.grid(row=0, column=1)

tk_img = ImageTk.PhotoImage(map_image)

can_img.create_image(20, 20, anchor = NW, image = tk_img) 

# control panal
control_panal_frame = Frame(cont_img_frame)
control_panal_frame.configure(bg = 'white')
control_panal_frame.grid(row=0, column=0)

# controls frame
controls_frame = Frame(control_panal_frame)
controls_frame.configure(bg= 'white')
controls_frame.grid(row=0, column=0)

# controls:
# initial state
init_lbl = tk.Label(controls_frame, text="Initial State", font=('Arial', 18, 'bold'), foreground = text_color , bg = 'white', width=controls_label_width)
init_lbl.grid(column= 0, row= 0)

# initial list
cities = list(Algorthims.romania_graph_with_cost.keys())

init_comb = ttk.Combobox(controls_frame, values= cities, state= "readonly", font=('Arial', 18), style='my.TMenubutton')
init_comb.set("Arad")  # Set default algorithm
init_comb.grid(row=1, column=0, padx=10, pady=10)

# goal state
goal_lbl = tk.Label(controls_frame, text="Goal State", font=('Arial', 18, 'bold'), foreground = text_color , bg = 'white', width=controls_label_width)
goal_lbl.grid(column= 0, row= 2)

goal_comb = ttk.Combobox(controls_frame, values= cities, state= "readonly", font=('Arial', 18), style='my.TMenubutton')
goal_comb.set("Arad")  # Set default algorithm
goal_comb.grid(row=3, column=0, padx=10, pady=10)

# algo state
goal_lbl = tk.Label(controls_frame, text="Algorithms", font=('Arial', 18, 'bold'), foreground = text_color , bg = 'white', width=controls_label_width)
goal_lbl.grid(column= 0, row= 4)

# Create a combobox for selecting the search algorithm
algorithm_combobox = ttk.Combobox(controls_frame, values=["Breadth First Search", "Uniform Cost Search", "Depth Search Search", "Depth Limited Search", "Iterative Deeping DLS", "Bidirectional Search", "Greedy Best First Search","A Star Search"], state="readonly", font=('Arial', 18), style='my.TMenubutton')
algorithm_combobox.set("Breadth First Search")  # Set default algorithm
algorithm_combobox.grid(row=5, column=0, padx=10, pady=10)

# limit entry lbl
limit_lbl = tk.Label(controls_frame, text="Limit", font=('Arial', 18, 'bold'), foreground = text_color , bg = 'white', width=controls_label_width)
limit_lbl.grid(column= 0, row= 6)

# limit enrty
limit_entry = tk.Entry(controls_frame, width=45)
limit_entry.grid(row=7, column=0)

# Create a button to trigger the path finding
find_path_button = tk.Button(controls_frame, text="GOOOOOOOOO", bg='white', font=('Arial', 20, 'bold'))
find_path_button.grid(row=8, column=0, pady=10)

# ---------------------------------------------------------------------------------------
# result label
result_lbl = tk.Label(root, text="Searching Algorithm Result", highlightthickness=2, highlightbackground='black', foreground='orange', bg = 'white', font=('Arial', 20, 'bold'))
result_lbl.pack(ipadx=10, ipady=10, padx=10, pady=10)

# --------------------------------------------------------------------------------------
# ************** Button Function Part *****************************            
def cal_cost(path):
    # Later: edit result font here
    cost = 0
    for city in range(len(path)-1):
        city2 = Algorthims.romania_graph_with_cost[path[city]]
        cost += city2[path[city+1]]
    return cost
            
def view_result(algorthim):
    if (algorthim == "Breadth First Search"):
        result =  Algorthims.breadth_first_search(init_comb.get(), goal_comb.get())
        if result is not None: 
            cost = cal_cost(result)
            res_lbl = f'Path: from {result[0]} to {result[-1]}\n\n {" -> ".join(result)} \n\n Cost: {cost}'
            result_lbl.config(text=res_lbl)

    elif (algorthim == 'Uniform Cost Search'):
        result =  Algorthims.uniform_cost_search(init_comb.get(), goal_comb.get())
        if result is not None:
            cost = result[1]
            res_lbl = f'Path: from {result[0][0]} to {result[0][-1]}\n\n {" -> ".join(result[0])} \n\n Cost: {cost}'
            result_lbl.config(text=res_lbl)
    
    elif (algorthim == 'Depth Search Search'):
        result =  Algorthims.deepth_first_search(init_comb.get(), goal_comb.get())
        if result is not None: 
            cost = cal_cost(result)
            res_lbl = f'Path: from {result[0]} to {result[-1]}\n\n {" -> ".join(result)} \n\n Cost: {cost}'
            result_lbl.config(text=res_lbl)
        else:
            result_lbl.config(text="No Path Found :(")
    
    elif (algorthim == 'Depth Limited Search'):
        result =  Algorthims.deepth_limit_search(init_comb.get(), goal_comb.get(), int(float(limit_entry.get()))) # 3del the limit to enrty.get()
        if result is not None: 
            cost = cal_cost(result)
            res_lbl = f'Path: from {result[0]} to {result[-1]}\n\n {" -> ".join(result)} \n\n Cost: {cost}'
            result_lbl.config(text=res_lbl)
        else:
            result_lbl.config(text="No Path Found :(")
    
    elif (algorthim == 'Iterative Deeping DLS'):
        result =  Algorthims.iterative_deeping_DLS(init_comb.get(), goal_comb.get())
        if result is not None: 
            cost = cal_cost(result)
            res_lbl = f'Path: from {result[0]} to {result[-1]}\n\n {" -> ".join(result)} \n\n Cost: {cost}'
            result_lbl.config(text=res_lbl)
        else:
            result_lbl.config(text="No Path Found :(")
    
    elif (algorthim == 'Bidirectional Search'):
        result =  Algorthims.bidirectional_search(init_comb.get(), goal_comb.get())
        if result is not None: 
            cost = cal_cost(result)
            res_lbl = f'Path: from {result[0]} to {result[-1]}\n\n {" -> ".join(result)} \n\n Cost: {cost}'
            result_lbl.config(text=res_lbl)
        else:
            result_lbl.config(text="No Path Found :(")
    
    elif (algorthim == 'Greedy Best First Search'):
        heuristic_values = Algorthims.calculate_huristic(goal_comb.get())
        result =  Algorthims.greedy_best_first_search(init_comb.get(), goal_comb.get(), heuristic_values)
        if result is not None: 
            cost = cal_cost(result)
            res_lbl = f'Path: from {result[0]} to {result[-1]}\n\n {" -> ".join(result)} \n\n Cost: {cost}'
            result_lbl.config(text=res_lbl)
        else:
            result_lbl.config(text="No Path Found :(")
    
    elif (algorthim == 'A Star Search'):
        heuristic_values = Algorthims.calculate_huristic(goal_comb.get())
        result =  Algorthims.a_start_search(init_comb.get(), goal_comb.get(), heuristic_values)
        if result is not None: 
            cost = cal_cost(result)
            res_lbl = f'Path: from {result[0]} to {result[-1]}\n\n {" -> ".join(result)} \n\n Cost: {cost}'
            result_lbl.config(text=res_lbl)
        else:
            result_lbl.config(text="No Path Found :(")
        
# *****************************************************************
# --------------------------------------------------------------------------------------
find_path_button.config(command=lambda: view_result(algorithm_combobox.get()))
# main loop
root.mainloop()




