#*************************************************************************************
#
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector


# **************************Function to validate login and open the dashboard window************************
def login():
    username = entryu.get()
    password = entryp.get()
    if username == "Admin@123" and password == "3476":
        win.destroy()  
        open_dashboard()  
    else:
        error_label.config(text="Invalid credentials, please try again.")

#********************************************************************************************************************


# **********************************Function to open the main dashboard window********************************
def open_dashboard():
    # Main application window
    dashboard_win = Tk()
    dashboard_win.state("zoomed")
    dashboard_win.config(background="#f7f7f7") 
    dashboard_win.title("MedTrust Hospital Management System") 
#*****************************************************************************************************************




# **************************************************Header Frame with hospital name********************************
    header = Frame(dashboard_win, bg="#34495e", height=90)
    header.pack(fill="x")

    subheading = Label(header, text="(Your Trusted Partner in Healthcare Management)",
                        font=("Arial", 14), fg="white", bg="#34495e")
    subheading.place(relx=0.5,y=70, anchor="center")
    header_label = Label(header, text="MedTrust Hospital Management System",
                         font=("Helvetica", 24, "bold"), fg="white", bg="#34495e")
    header_label.place(relx=0.5, rely=0.4, anchor="center")
#*******************************************************************************************************
   



#***************************Frame container for switching between sections******************************
    container = Frame(dashboard_win, bg="white", relief=FLAT)
    container.place(x=150, y=150, height=850, width=1550)

#********************************************************************************************






#************************************************** Sidebar frame***************************
    sidebar = Frame(dashboard_win, bg="#2c3e50", width=150, relief=FLAT)
    sidebar.pack(side="left", fill="y")


#**************************************************************************************************


# ***********************************************functions to switch frames*****************************
   
    def show_patients():
        patients_frame.tkraise()

    def show_appointments():
        appointments_frame.tkraise()

    def show_prescription():
        prescription_frame.tkraise()

#***********************************************************************************************************




# ********************************************************Nevigation buttons**********************************************

    Button(sidebar, text="Patients", font=("Helvetica", 14, "bold"), fg='white', bg="#2c3e50",
           activebackground="#1abc9c", activeforeground="white", cursor="hand2", command=show_patients).pack(fill="x", pady=5, padx=5)

    Button(sidebar, text="Appointments", font=("Helvetica", 14, "bold"), fg='white', bg="#2c3e50",
           activebackground="#1abc9c", activeforeground="white", cursor="hand2", command=show_appointments).pack(fill="x", pady=5, padx=5)

    Button(sidebar, text="Prescription", font=("Helvetica", 14, "bold"), fg='white', bg="#2c3e50",
           activebackground="#1abc9c", activeforeground="white", cursor="hand2", command=show_prescription).pack(fill="x", pady=5, padx=5)

#**************************************************************************************************************************



#******************************************************Frames for each section********************************************
    
    patients_frame = Frame(container, bg="#ecf0f1")
    patients_frame.place(x=0, y=0, relwidth=1, relheight=1)

    appointments_frame = Frame(container, bg="#ecf0f1")
    appointments_frame.place(x=0, y=0, relwidth=1, relheight=1)

    prescription_frame = Frame(container, bg="#ecf0f1")
    prescription_frame.place(x=0, y=0, relwidth=1, relheight=1)

#******************************************************************************************************************

    






#**************************************************Patient frame content**********************************************
#**********************************************************************************************************************


#************************************************Patient_button_function**********************************************
    def patients_btn1_fn():

        if (PAV1.get()=="" or PAV2.get()=="" or PAV3.get()=="" or PAV4.get()=="" or PAV5.get()=="" or PAV6.get()=="" or PAV7.get()=="" or PAV8.get()=="" or PAV9.get()=="" or PAV10.get()=="" or PAV11.get()=="" or PAV12.get()==""):
            messagebox.showerror("Error","All fields are required")
        else:
            
            con_=mysql.connector.connect(host="localhost",
                            user= "root",
                            password="Soumyajit",
                            database="mydata")
            cursor = con_.cursor()
            cursor.execute("INSERT INTO patient VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s)", (
                PAV1.get(),
                PAV2.get(),
                PAV3.get(),
                PAV4.get(),
                PAV5.get(),
                PAV6.get(),
                PAV7.get(),
                PAV8.get(),
                PAV9.get(),
                PAV10.get(),
                PAV11.get(),
                PAV12.get()
                
            ))
            con_.commit()
            fetch_data_patients()
            con_.close()
            messagebox.showinfo("Success", "Record Inserted")
   
    def fetch_data_patients():
          

          con_=mysql.connector.connect(host="localhost",
                            user= "root",
                            password="Soumyajit",
                            database="mydata")
          cursor = con_.cursor()
          cursor.execute("SELECT * FROM patient")
          rows = cursor.fetchall()
          if len(rows)!=0:
                Table_Patients.delete(* Table_Patients.get_children())
                for iteams in rows:
                      Table_Patients.insert('',END,values=iteams)
                con_.commit()
          con_.close()

    def get_data_paa(event=''):

        cursor_row_PAA = Table_Patients.focus()
        PAA_data = Table_Patients.item(cursor_row_PAA)
        row_PAA = PAA_data["values"]
        PAV1.set(row_PAA[0])
        PAV2.set(row_PAA[1])
        PAV3.set(row_PAA[2])
        PAV4.set(row_PAA[3])
        PAV5.set(row_PAA[4])
        PAV6.set(row_PAA[5])
        PAV7.set(row_PAA[6])
        PAV8.set(row_PAA[7])
        PAV9.set(row_PAA[8])
        PAV10.set(row_PAA[9])
        PAV11.set(row_PAA[10])
        PAV12.set(row_PAA[11])

    def patients_btn2_fn():
          
          con_ = mysql.connector.connect(
          host="localhost",
          user="root",
          password="Soumyajit",
          database="mydata")
          cursor = con_.cursor()
          cursor.execute('''UPDATE patient SET 
          `Full Name` = %s, `Gender` = %s, `Blood Group` = %s, `Phone No.` = %s, `Address` = %s, `Blood Pressure` = %s, `Weight` = %s, `Glucose Levels` = %s ,`Medical History` = %s, `Allergies` = %s, `Current Medications` = %s  WHERE `Medical No.` = %s''', (
          
          PAV2.get(),
          PAV3.get(),
          PAV4.get(),
          PAV5.get(),
          PAV6.get(),
          PAV7.get(),
          PAV8.get(),
          PAV9.get(),
          PAV10.get(),
          PAV11.get(),
          PAV12.get(),
          PAV1.get()
          ))
          con_.commit()
          con_.close()
          fetch_data_patients()
          messagebox.showinfo("Success", "Record Updated")

    def patients_btn3_fn():

        
        con_ = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Soumyajit",
        database="mydata"
        )
        cursor = con_.cursor()
        query = "DELETE FROM patient WHERE `Medical No.` = %s"
        value = (PAV1.get(),)
        cursor.execute(query, value)
        con_.commit()
        fetch_data_patients()
        con_.close()
        messagebox.showinfo("Success", "Record Deleted")   

    def patients_btn4_fn():
        PAV1.set('')
        PAV2.set('')
        PAV3.set('')
        PAV4.set('')
        PAV5.set('')
        PAV6.set('')
        PAV7.set('')
        PAV8.set('')
        PAV9.set('')
        PAV10.set('')
        PAV11.set('')
        PAV12.set('')
        messagebox.showinfo("Success", "Reset Success")
          
#**********************************************************************************************************************
#**********************************************************************************************************************
          

#********************************Patient_Labels***********************************************************************
    
    Label(patients_frame, text="Patient Management", font=("Helvetica", 24, "bold"), bg="#ecf0f1").place(x=50, y=20)

    patient_info = LabelFrame(patients_frame,text="Patient's Informations", font=("Helvetica", 14, "bold"), bg="white", bd=2, relief=RIDGE)
    patient_info.place(x=50, y=80, width=945, height=360)

    patients_dtls = LabelFrame(patient_info,text="Patients Details", font=("Helvetica", 14, "bold"), bg="white", bd=2, relief=RIDGE)
    patients_dtls.place(x=15, y=10, width=450, height=300)

    patients_mifo = LabelFrame(patient_info,text="Medical Information", font=("Helvetica", 14, "bold"), bg="white", bd=2, relief=RIDGE)
    patients_mifo.place(x=475, y=10, width=450, height=300)


    dtl1_frame = LabelFrame(patients_frame,text="Patient Records", font=("Helvetica", 14, "bold"), bg="white", bd=2, relief=RIDGE)
    dtl1_frame.place(x=50, y=450, width=1480, height=400)

   
#Text_variables
    PAV1 = StringVar()
    PAV2 = StringVar()
    PAV3 = StringVar()
    PAV4 = StringVar()
    PAV5 = StringVar()
    PAV6 = StringVar()
    PAV7 = StringVar()
    PAV8 = StringVar()
    PAV9 = StringVar()
    PAV10 = StringVar()
    PAV11 = StringVar()
    PAV12 = StringVar()



                                  #******************PatientaTabEntries***************

    Label(patients_dtls, text="Medical No.:", font=("Arial", 13), bg="white").place(x=20, y=20)
    PAE1 = Entry(patients_dtls, font=("Arial", 12),bd=1.5 , width=30, relief=GROOVE, textvariable=PAV1)
    PAE1.place(x=150, y=20, height=20)

    Label(patients_dtls, text="Full Name:", font=("Arial", 13), bg="white").place(x=20, y=60)
    PAE2 = Entry(patients_dtls,font=("Arial", 12),bd=1.5, width=30,  relief=GROOVE,textvariable=PAV2)
    PAE2.place(x=150, y=60, height=20)

    Label(patients_dtls, text="Gender:", font=("Arial", 13), bg="white").place(x=20, y=100)
    PAE3 =Entry(patients_dtls, font=("Arial", 12), width=30, bd=2, relief=GROOVE,textvariable=PAV3)
    PAE3.place(x=150, y=100, height=20)

    Label(patients_dtls, text="Blood Group:", font=("Arial", 13), bg="white").place(x=20, y=140)
    PAE4 = Entry(patients_dtls, font=("Arial", 12), width=30, bd=2, relief=GROOVE,textvariable=PAV4)
    PAE4.place(x=150, y=140, height=20)

    Label(patients_dtls, text="Phone No.:", font=("Arial", 13), bg="white").place(x=20, y=180)
    PAE5 =Entry(patients_dtls, font=("Arial", 12), width=30 , bd=2, relief=GROOVE,textvariable=PAV5)
    PAE5.place(x=150, y=180, height=20)

    Label(patients_dtls, text="Address:", font=("Arial", 13), bg="white").place(x=20, y=220)
    PAE6 =Entry(patients_dtls, font=("Arial", 12), width=30 , bd=2, relief=GROOVE,textvariable=PAV6)
    PAE6.place(x=150, y=220, height=40)

                                        #***************************

    Label(patients_mifo, text="Blood Pressure:", font=("Arial", 13), bg="white").place(x=20, y=20)
    PAE7 = Entry(patients_mifo, font=("Arial", 12), width=30, bd=2, relief=GROOVE,textvariable=PAV7)
    PAE7.place(x=180, y=20, height=20)


    Label(patients_mifo, text="Weight:", font=("Arial", 13), bg="white").place(x=20, y=60)
    PAE8 = Entry(patients_mifo, font=("Arial", 12), width=30, bd=2, relief=GROOVE,textvariable=PAV8)
    PAE8.place(x=180, y=60, height=20)

    Label(patients_mifo, text="Glucose Levels:", font=("Arial", 13), bg="white").place(x=20, y=100)
    PAE9 = Entry(patients_mifo, font=("Arial", 12), width=30, bd=2, relief=GROOVE,textvariable=PAV9)
    PAE9.place(x=180, y=100, height=20)

    Label(patients_mifo, text="Medical History:", font=("Arial", 13), bg="white").place(x=20, y=140)
    PAE10 =Entry(patients_mifo, font=("Arial", 12), width=30, bd=2, relief=GROOVE,textvariable=PAV10)
    PAE10.place(x=180, y=140, height=20)

    Label(patients_mifo, text="Allergies:", font=("Arial", 13), bg="white").place(x=20, y=180)
    PAE11 =Entry(patients_mifo, font=("Arial", 12), width=30, bd=2, relief=GROOVE,textvariable=PAV11)
    PAE11.place(x=180, y=180, height=20)

    Label(patients_mifo, text="Current Medications:", font=("Arial", 13), bg="white").place(x=20, y=221)
    PAE12 =Entry(patients_mifo, font=("Arial", 11), width=30, bd=2, relief=GROOVE,textvariable=PAV12)
    PAE12.place(x=180, y=221, height=30)
#**********************************************************************************************************************

                          #***********************Patient_Buttons***************************

    btns_frame = LabelFrame(patients_frame, bg="#ecf0f1")
    btns_frame.place(x=1015, y=100, width=130, height=300)


    patients_btn1 =Button(btns_frame, text="Save", font=("Arial", 13), bg="#28a745", fg="white",
       width=10, height=2, relief=RAISED, cursor="hand2",command=patients_btn1_fn)
    patients_btn1.grid(row=0, column=0, padx=10, pady=10)


    patients_btn2 =Button(btns_frame, text="Update", font=("Arial", 13), bg="#17a2b8", fg="white",
       width=10, height=2, relief=RAISED, cursor="hand2",command=patients_btn2_fn)
    patients_btn2.grid(row=1, column=0, padx=10, pady=10)

    patients_btn3 =Button(btns_frame, text="Delete", font=("Arial", 13), bg="#dc3545", fg="white",
       width=10, height=2, relief=RAISED, cursor="hand2",command=patients_btn3_fn)
    patients_btn3.grid(row=2, column=0, padx=10, pady=10)

    patients_btn4 =Button(btns_frame, text="Reset", font=("Arial", 13), bg="#6c757d", fg="white",
       width=10, height=2, relief=RAISED, cursor="hand2",command=patients_btn4_fn)
    patients_btn4.grid(row=3, column=0, padx=10,pady=10)

  

#*************************************************************************************************
    
    Scrollbar_x = ttk.Scrollbar(dtl1_frame,orient=HORIZONTAL)
    Scrollbar_x.pack(side="bottom",fill=X)

    Scrollbar_y = ttk.Scrollbar(dtl1_frame,orient=VERTICAL)
    Scrollbar_y.pack(side="right",fill=Y)
    
    Table_Patients = ttk.Treeview(dtl1_frame,columns=('mno','pnm','gen','bg','pno','add','bp','wt','glvl','mhist','allg','cmdn'),xscrollcommand=Scrollbar_y.set,yscrollcommand=Scrollbar_x.set)
    Scrollbar_x = ttk.Scrollbar(command=Table_Patients.xview)
    Scrollbar_y = ttk.Scrollbar(command=Table_Patients.yview)
#headings
    Table_Patients.heading('mno',text="Medical No.")
    Table_Patients.heading('pnm',text="Full Name")
    Table_Patients.heading('gen',text="Gender")
    Table_Patients.heading('bg',text="Blood Group")
    Table_Patients.heading('pno',text="Phone No.")
    Table_Patients.heading('add',text="Address")
    Table_Patients.heading('bp',text="Blood Pressure")
    Table_Patients.heading('wt',text="Weight")
    Table_Patients.heading('glvl',text="Glucose Level")
    Table_Patients.heading('mhist',text="Medical History")
    Table_Patients.heading('allg',text="Allergies")
    Table_Patients.heading('cmdn',text="Current Medications")
    Table_Patients['show']='headings'
    Table_Patients.pack(fill=BOTH,expand=1)


    Table_Patients.column('mno',width=20)
    Table_Patients.column('pnm',width=45)
    Table_Patients.column('gen',width=10)
    Table_Patients.column('bg',width=30)
    Table_Patients.column('pno',width=30)
    Table_Patients.column('add',width=200)
    Table_Patients.column('bp',width=40)
    Table_Patients.column('wt',width=40)
    Table_Patients.column('glvl',width=10)
    Table_Patients.column('mhist',width=40)
    Table_Patients.column('allg',width=40)
    Table_Patients.column('cmdn',width=60)
    






#***************************************************************************************************************
#********************************************** Appointment frame content***************************************
#***************************************************************************************************************


#********************************************** Appointmrnt Button Function***************************************


    def appointment_btn1_fn():
        if (AV1.get()=="" or AV2.get()=="" or AV3.get()=="" or AV4.get()=="" or AV5.get()=="" or AV6.get()=="" or AV7.get()=="" or AV8.get()=="" or AV9.get()==""):
            messagebox.showerror("Error","All fields are required")
        else:
            con_=mysql.connector.connect(host="localhost",
                            user= "root",
                            password="Soumyajit",
                            database="mydata")
            cursor = con_.cursor()
            cursor.execute("INSERT INTO appointment VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                AV1.get(),
                AV2.get(),
                AV3.get(),
                AV4.get(),
                AV5.get(),
                AV6.get(),
                AV7.get(),
                AV8.get(),
                AV9.get(),
                
            ))
            con_.commit()
            fetch_data_appointment()
            con_.close()
            messagebox.showinfo("Success", "Record Inserted")
   
    def fetch_data_appointment():

          con_=mysql.connector.connect(host="localhost",
                            user= "root",
                            password="Soumyajit",
                            database="mydata")
          cursor = con_.cursor()
          cursor.execute("SELECT * FROM appointment")
          rows = cursor.fetchall()
          if len(rows)!=0:
                Table_Appointment.delete(* Table_Appointment.get_children())
                for iteams in rows:
                      Table_Appointment.insert('',END,values=iteams)
                con_.commit()
          con_.close()

    def get_data_app(event=''):
        cursor_row_APP = Table_Appointment.focus()
        app_data = Table_Appointment.item(cursor_row_APP)
        row_APP = app_data["values"]
        AV1.set(row_APP[0])
        AV2.set(row_APP[1])
        AV3.set(row_APP[2])
        AV4.set(row_APP[3])
        AV5.set(row_APP[4])
        AV6.set(row_APP[5])
        AV7.set(row_APP[6])
        AV8.set(row_APP[7])
        AV9.set(row_APP[8])

    def appointment_btn2_fn():
          con_ = mysql.connector.connect(
          host="localhost",
          user="root",
          password="Soumyajit",
          database="mydata")
          cursor = con_.cursor()
          cursor.execute('''UPDATE appointment SET 
          `Patient's Name` = %s, `Status` = %s, `Gender` = %s, `Email` = %s, `Date Time` = %s, `Appointment Type` = %s, `Doctor Name` = %s, `Purpose of Appointment` = %s  WHERE `Medical No.` = %s''', (
          AV1.get(),
          AV9.get(),
          AV3.get(),
          AV4.get(),
          AV5.get(),
          AV6.get(),
          AV7.get(),
          AV8.get(),
          AV2.get()
          ))
          con_.commit()
          con_.close()
          fetch_data_appointment()
          messagebox.showinfo("Success", "Record Updated")

    def appointment_btn3_fn():
        
        con_ = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Soumyajit",
        database="mydata"
        )
        cursor = con_.cursor()
        query = "DELETE FROM appointment WHERE `Medical No.` = %s"
        value = (AV2.get(),)
        cursor.execute(query, value)
        con_.commit()
        fetch_data_appointment()
        con_.close()
        messagebox.showinfo("Success", "Record Deleted")   

    def appointment_btn4_fn():
         
          AV1.set('')
          AV2.set('')
          AV3.set('')
          AV4.set('')
          AV5.set('')
          AV6.set('')
          AV7.set('')
          AV8.set('')
          AV9.set('')
          messagebox.showinfo("Success", "Reset Success")
          
          
#********************************************** Appointment Label ***********************************************************

    Label(appointments_frame, text="Appointment Scheduling", font=("Helvetica", 24, "bold"), bg="#ecf0f1").place(x=50, y=20)
   

   
    appointment_info = LabelFrame(appointments_frame,text="Patient Info",font=("Helvetica", 14, "bold"), bg="white", bd=2, relief=RIDGE)
    appointment_info.place(x=50, y=80, width=570, height=700)


    appointment_record = LabelFrame(appointments_frame,text="Appointment Records",font=("Helvetica", 14, "bold"), bg="white", bd=2, relief=RIDGE)
    appointment_record.place(x=640, y=80, width=880, height=700)

#text variables
    AV1 = StringVar()
    AV2 = StringVar()
    AV3 = StringVar()
    AV4 = StringVar()
    AV5 = StringVar()
    AV6 = StringVar()
    AV7 = StringVar()
    AV8 = StringVar()
    AV9 = StringVar()
    
    

#**********************************************Appointment Entries ******************************************************


    Label(appointment_info, text="Patient's Name:", font=("Arial", 12),bg="white").place(x=20, y=20)
    AE1 =Entry(appointment_info, font=("Arial", 12),bd=1.5,textvariable=AV1 )
    AE1.place(x=20,y=50,width=500)

    Label(appointment_info, text="Medical No.:", font=("Arial", 12),bg="white").place(x=20, y=80)
    AE2 =Entry(appointment_info, font=("Arial", 12),bd=1.5 ,textvariable=AV2)
    AE2.place(x=20,y=110,width=500)

    Label(appointment_info, text="Gender:", font=("Arial", 12),bg="white").place(x=20, y=140)
    AE3 =Entry(appointment_info, font=("Arial", 12),bd=1.5 ,textvariable=AV3)
    AE3.place(x=20,y=170,width=500)

    Label(appointment_info, text="Email:", font=("Arial", 12),bg="white").place(x=20, y=200)
    AE4 =Entry(appointment_info, font=("Arial", 12),bd=1.5 ,textvariable=AV4)
    AE4.place(x=20,y=230,width=500)

    Label(appointment_info, text="Date Time:", font=("Arial", 12),bg="white").place(x=20, y=260)
    AE5 =Entry(appointment_info, font=("Arial", 12),bd=1.5,textvariable=AV5)
    AE5.place(x=20,y=290,width=500)

    Label(appointment_info, text="Appointment Type:", font=("Arial", 12),bg="white").place(x=20, y=320)
    AE6 =Entry(appointment_info, font=("Arial", 12),bd=1.5,textvariable=AV6 )
    AE6.place(x=20,y=350,width=500)

    Label(appointment_info, text="Doctor Name:", font=("Arial", 12),bg="white").place(x=20, y=380)
    AE7 =Entry(appointment_info, font=("Arial", 12),bd=1.5,textvariable=AV7 )
    AE7.place(x=20,y=410,width=500)

    Label(appointment_info, text="Purpose of Appointment:", font=("Arial", 12),bg="white").place(x=20, y=440)
    AE8 =Entry(appointment_info, font=("Arial", 12),bd=1.5,textvariable=AV8)
    AE8.place(x=20,y=470,width=500)

    Label(appointment_info, text="Status:", font=("Arial", 12),bg="white").place(x=20, y=500)
    AE8 =Entry(appointment_info, font=("Arial", 12),bd=1.5,textvariable=AV9)
    AE8.place(x=20,y=530,width=500)  



                     #*********************Appointment buttons********************



    btns_frame_app = Label(appointment_info, bg="White",bd=2)
    btns_frame_app.place(x=50, y=580, width=500, height=80)



    appointment_btn1 = Button(btns_frame_app, text="Save", font=("Arial", 13), bg="#28a745", fg="white",
       width=10, height=2, relief=RAISED, cursor="hand2",command=appointment_btn1_fn)
    appointment_btn1.grid(row=0, column=0, padx=10, pady=10)

    appointment_btn2 = Button(btns_frame_app, text="Update", font=("Arial", 13), bg="#17a2b8", fg="white",
       width=10, height=2, relief=RAISED, cursor="hand2",command=appointment_btn2_fn)
    appointment_btn2.grid(row=0, column=1, padx=10, pady=10)

    appointment_btn3 = Button(btns_frame_app, text="Delete", font=("Arial", 13), bg="#dc3545", fg="white",
       width=10, height=2, relief=RAISED, cursor="hand2",command=appointment_btn3_fn)
    appointment_btn3.grid(row=0, column=2, padx=10, pady=10)

    appointment_btn4 = Button(btns_frame_app, text="Reset", font=("Arial", 13), bg="#6c757d", fg="white",
       width=10, height=2, relief=RAISED, cursor="hand2",command=appointment_btn4_fn)
    appointment_btn4.grid(row=0, column=3, padx=10,pady=10)







  
    Scrollbar_x = ttk.Scrollbar(appointment_record,orient=HORIZONTAL)
    Scrollbar_x.pack(side="bottom",fill=X)

    Scrollbar_y = ttk.Scrollbar(appointment_record,orient=VERTICAL)
    Scrollbar_y.pack(side="right",fill=Y)
    
    Table_Appointment = ttk.Treeview(appointment_record,columns=('ptn','mno','gen','em','dt','at','dnam','pur','sta'),xscrollcommand=Scrollbar_y.set,yscrollcommand=Scrollbar_x.set)
    Scrollbar_x = ttk.Scrollbar(command=Table_Appointment.xview)
    Scrollbar_y = ttk.Scrollbar(command=Table_Appointment.yview)
#headings
    Table_Appointment.heading('ptn',text="Patient's Name")
    Table_Appointment.heading('mno',text="Medical No.")
    Table_Appointment.heading('gen',text="Gender")
    Table_Appointment.heading('em',text="Email")
    Table_Appointment.heading('dt',text="Date Time")
    Table_Appointment.heading('at',text="Appointment Type")
    Table_Appointment.heading('dnam',text="Doctor Name")
    Table_Appointment.heading('pur',text="Purpose of Appointment")
    Table_Appointment.heading('sta',text="Status")
    Table_Appointment['show']='headings'
    Table_Appointment.pack(fill=BOTH,expand=1)



    Table_Appointment.column('ptn',width=40)
    Table_Appointment.column('mno',width=40)
    Table_Appointment.column('gen',width=15)
    Table_Appointment.column('em',width=100)
    Table_Appointment.column('dt',width=60)
    Table_Appointment.column('at',width=60)
    Table_Appointment.column('dnam',width=50)
    Table_Appointment.column('pur',width=80)
    Table_Appointment.column('sta',width=30)





#***************************************************************************************************************
# ***************************************Prescription frame content******************************************************
#***************************************************************************************************************
    def prescription_btn2_fn():
        if (PV1.get()=="" or PV2.get()=="" or PV3.get()=="" or PV4.get()=="" or PV5.get()=="" or PV6.get()=="" or PV7.get()=="" or PV8.get()=="" or PV9.get()==""):
            messagebox.showerror("Error","All fields are required")
        else:
            
            con_=mysql.connector.connect(host="localhost",
                            user= "root",
                            password="Soumyajit",
                            database="mydata")
            cursor = con_.cursor()
            cursor.execute("INSERT INTO prescription VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                PV1.get(),
                PV2.get(),
                PV3.get(),
                PV4.get(),
                PV5.get(),
                PV6.get(),
                PV7.get(),
                PV8.get(),
                PV9.get()
            ))
            con_.commit()
            fetch_data()
            con_.close()
            messagebox.showinfo("Success", "Record Inserted")
   
    def fetch_data():
          con_=mysql.connector.connect(host="localhost",
                            user= "root",
                            password="Soumyajit",
                            database="mydata")
          cursor = con_.cursor()
          cursor.execute("SELECT * FROM prescription")
          rows = cursor.fetchall()
          if len(rows)!=0:
                Table_prescription.delete(* Table_prescription.get_children())
                for iteams in rows:
                      Table_prescription.insert('',END,values=iteams)
                con_.commit()
          con_.close()

    def get_data_pres(event=''):
          cursor_row_pres = Table_prescription.focus()
          pres_data = Table_prescription.item(cursor_row_pres)
          row_pres = pres_data["values"]
          PV1.set(row_pres[0])
          PV2.set(row_pres[1])
          PV3.set(row_pres[2])
          PV4.set(row_pres[3])
          PV5.set(row_pres[4])
          PV6.set(row_pres[5])
          PV7.set(row_pres[6])
          PV8.set(row_pres[7])
          PV9.set(row_pres[8])


    def prescription_btn1_fn():
          prescription_txt.insert(END,"\nPatient's Name:\t\t"+PV1.get()+"\n")
          prescription_txt.insert(END,"Medical No. :\t\t"+PV2.get()+"\n")
          prescription_txt.insert(END,"Age:\t\t"+PV3.get()+"\n")
          prescription_txt.insert(END,"Gender:\t\t"+PV4.get()+"\n")
          prescription_txt.insert(END,"Date:\t\t"+PV5.get()+"\n")
          prescription_txt.insert(END,"Doctor Name:\t\t"+PV6.get()+"\n")
          prescription_txt.insert(END,"Drug Name:\t\t"+PV7.get()+"\n")
          prescription_txt.insert(END,"Dosage:\t\t"+PV8.get()+"\n")
          prescription_txt.insert(END,"Clinical Note:\t\t"+PV9.get()+"\n")

        
    def prescription_btn3_fn():
          con_ = mysql.connector.connect(
          host="localhost",
          user="root",
          password="Soumyajit",
          database="mydata")
          cursor = con_.cursor()
          cursor.execute('''UPDATE prescription SET 
          `Patient's Name` = %s, `Clinical Note` = %s, `Age` = %s, `Gender` = %s, `Date` = %s, `Doctor Name` = %s, `Drug name` = %s, `Dosage` = %s  WHERE `Medical No.` = %s''', (
          PV1.get(),
          PV9.get(),
          PV3.get(),
          PV4.get(),
          PV5.get(),
          PV6.get(),
          PV7.get(),
          PV8.get(),
          PV2.get()
          ))
          con_.commit()
          con_.close()
          fetch_data()
          messagebox.showinfo("Success", "Record Updated")
    def prescription_btn4_fn():
          
          con_ = mysql.connector.connect(
          host="localhost",
          user="root",
          password="Soumyajit",
          database="mydata"
          )
          cursor = con_.cursor()
          query = "DELETE FROM prescription WHERE `Medical No.` = %s"
          value = (PV2.get(),)
          cursor.execute(query, value)
          con_.commit()
          fetch_data()
          con_.close()
          messagebox.showinfo("Success", "Record Deleted")   

    def prescription_btn5_fn():
          prescription_txt.delete(1.0,END)
          
          PV1.set('')
          PV2.set('')
          PV3.set('')
          PV4.set('')
          PV5.set('')
          PV6.set('')
          PV7.set('')
          PV8.set('')
          PV9.set('')
          messagebox.showinfo("Success", "Reset Success")
          
          
          
          



    Label(prescription_frame, text="Generate Prescription", font=("Helvetica", 24, "bold"), bg="#ecf0f1").place(x=50, y=20)

    prescriprion_content = LabelFrame(prescription_frame,text="Patients Info", font=("Helvetica", 14, "bold"), bg="white", bd=2, relief=RIDGE)
    prescriprion_content.place(x=50, y=80, width=600, height=420)

    pres_frame = LabelFrame(prescription_frame,text="Prescription", font=("Helvetica", 14, "bold"), bg="white", bd=2, relief=RIDGE)
    pres_frame.place(x=850, y=80, width=500, height=400)

    dtl_frame = LabelFrame(prescription_frame,text="Prescription Records",font=("Helvetica", 14, "bold"), bg="white", bd=2, relief=RIDGE)
    dtl_frame.place(x=40, y=510, width=1500, height=330)


    prescription_txt= Text(pres_frame, font=("Helvetica", 15,"bold" ),bg="yellow")
    prescription_txt.pack(fill=BOTH)
    

   

#text variables
    PV1 = StringVar()
    PV3 = StringVar()
    PV5 = StringVar()
    PV2 = StringVar()
    PV4 = StringVar()
    PV6 = StringVar()
    PV7 = StringVar()
    PV8 = StringVar()
    PV9 = StringVar()



    
#                              ***************PrescriptionEntries**************
    PL1=Label(prescriprion_content, text="Patient's Name:", font=("Arial", 14), bg="white")
    PL1.place(x=20, y=20)
    PE1=Entry(prescriprion_content, font=("Arial", 14), width=30, bd=2, relief=GROOVE,textvariable=PV1)
    PE1.place(x=180, y=20)

    PL2=Label(prescriprion_content, text="Medical No. :", font=("Arial", 14), bg="white")
    PL2.place(x=20, y=60)
    PE2=Entry(prescriprion_content, font=("Arial", 14), width=30, bd=2, relief=GROOVE,textvariable=PV2)
    PE2.place(x=180, y=60)

    PL3=Label(prescriprion_content, text="Age:", font=("Arial", 14), bg="white")
    PL3.place(x=20, y=100)
    PE3=Entry(prescriprion_content, font=("Arial", 14), width=30, bd=2, relief=GROOVE,textvariable=PV3)
    PE3.place(x=180, y=100)

    PL4=Label(prescriprion_content, text="Gender:", font=("Arial", 14), bg="white")
    PL4.place(x=20, y=140)
    PE4=Entry(prescriprion_content, font=("Arial", 14), width=30, bd=2, relief=GROOVE ,textvariable=PV4)
    PE4.place(x=180, y=140)


    PL5=Label(prescriprion_content, text="Date:", font=("Arial", 14), bg="white")
    PL5.place(x=20, y=180)
    PE5=Entry(prescriprion_content, font=("Arial", 14), width=30, bd=2, relief=GROOVE ,textvariable=PV5)
    PE5.place(x=180, y=180)


    PL6=Label(prescriprion_content, text="Doctor Name:", font=("Arial", 14), bg="white")
    PL6.place(x=20, y=220)
    PE6=Entry(prescriprion_content, font=("Arial", 14), width=30, bd=2, relief=GROOVE ,textvariable=PV6)
    PE6.place(x=180, y=220)


    PL7=Label(prescriprion_content, text="Drug Name:", font=("Arial", 14), bg="white")
    PL7.place(x=20, y=260)
    PE7=Entry(prescriprion_content, font=("Arial", 14), width=30, bd=2, relief=GROOVE,textvariable=PV7)
    PE7.place(x=180, y=260)


    PL8=Label(prescriprion_content, text="Dosage:", font=("Arial", 14), bg="white")
    PL8.place(x=20, y=300)
    PE8=Entry(prescriprion_content, font=("Arial", 14), width=30, bd=2, relief=GROOVE,textvariable=PV8)
    PE8.place(x=180, y=300)


    PL9=Label(prescriprion_content, text="Clinical Note:", font=("Arial", 14), bg="white")
    PL9.place(x=20, y=340)
    PE9=Entry(prescriprion_content, font=("Arial", 14), width=30, bd=2, relief=GROOVE,textvariable=PV9)
    PE9.place(x=180, y=340)



                                  #*********************Prescription buttons********************

    prescription_btns_frame =  Frame(prescription_frame, bg="#ecf0f1")
    prescription_btns_frame.place(x=670, y=100, width=180, height=400)

    prescription_btns1=Button(prescription_btns_frame, text="Show Prescription", font=("Arial", 13), bg="#1abc9c", fg="white",
       width=15, height=2, relief=RAISED, cursor="hand2",command=prescription_btn1_fn)
    prescription_btns1.grid(row=0, column=0, padx=10, pady=10)

    prescription_btns2=Button(prescription_btns_frame, text="Save Prescription", font=("Arial", 13), bg="#007bff", fg="white",
       width=15, height=2, relief=RAISED, cursor="hand2",command=prescription_btn2_fn)
    prescription_btns2.grid(row=1, column=0, padx=10, pady=10)

    prescription_btns3=Button(prescription_btns_frame, text="Update", font=("Arial", 13), bg="#ffc107", fg="black",
       width=15, height=2, relief=RAISED, cursor="hand2",command=prescription_btn3_fn)
    prescription_btns3.grid(row=2, column=0, padx=10, pady=10)

    prescription_btns4=Button(prescription_btns_frame, text="Delete", font=("Arial", 13), bg="#dc3545", fg="white",
       width=15, height=2, relief=RAISED, cursor="hand2",command=prescription_btn4_fn)
    prescription_btns4.grid(row=3, column=0, padx=10, pady=10)

    prescription_btns5=Button(prescription_btns_frame, text="Reset", font=("Arial", 13), bg="#6c757d", fg="white",
       width=15, height=2, relief=RAISED, cursor="hand2",command=prescription_btn5_fn)
    prescription_btns5.grid(row=4, column=0, padx=10, pady=10)

#***************************************************************************************************************
    Scrollbar_x = ttk.Scrollbar(dtl_frame,orient=HORIZONTAL)
    Scrollbar_x.pack(side="bottom",fill=X)

    Scrollbar_y = ttk.Scrollbar(dtl_frame,orient=VERTICAL)
    Scrollbar_y.pack(side="right",fill=Y)
    
    Table_prescription = ttk.Treeview(dtl_frame,columns=('ptn','mno','age','gdr','dte','dme','drname','dg','cn'),xscrollcommand=Scrollbar_y.set,yscrollcommand=Scrollbar_x.set)
    Scrollbar_x = ttk.Scrollbar(command=Table_prescription.xview)
    Scrollbar_y = ttk.Scrollbar(command=Table_prescription.yview)
#headings
    Table_prescription.heading('ptn',text="Patient's Name")
    Table_prescription.heading('mno',text="Medical No.")
    Table_prescription.heading('age',text="Age")
    Table_prescription.heading('gdr',text="Gender")
    Table_prescription.heading('dte',text="Date")
    Table_prescription.heading('dme',text="Doctor Name")
    Table_prescription.heading('drname',text="Drug Name")
    Table_prescription.heading('dg',text="Dosage")
    Table_prescription.heading('cn',text="Clinical Note")
    Table_prescription['show']='headings'
    Table_prescription.pack(fill=BOTH,expand=1)



    Table_prescription.column('ptn',width=150)
    Table_prescription.column('mno',width=100)
    Table_prescription.column('age',width=100)
    Table_prescription.column('gdr',width=100)
    Table_prescription.column('dte',width=120)
    Table_prescription.column('dme',width=150)
    Table_prescription.column('drname',width=150)
    Table_prescription.column('dg',width=200)
    Table_prescription.column('cn',width=250)
    

#***************************************************************************************************************
#***************************************************************************************************************
#***************************************************************************************************************
#***************************************************************************************************************

    
  
    show_patients()  # Show the default section
    Table_Patients.bind('<ButtonRelease-1>',get_data_paa)
    Table_Appointment.bind('<ButtonRelease-1>',get_data_app)
    Table_prescription.bind('<ButtonRelease-1>',get_data_pres)
    fetch_data_patients()
    fetch_data_appointment()
    fetch_data()
    show_patients.mainloop()
    
    

# Initial login window
win = Tk()
win.title("LOGIN")
win.geometry("400x500")
win.config(bg="#2c3e50")  



frame1 = Frame(win, bg="#34495e", bd=5, relief=RIDGE)
frame1.place(relx=0.5, rely=0.5, anchor="center", width=300, height=400)

# Login labels and entry fields
label1 = Label(frame1, text="Login", bg="#34495e", fg="white", font=("Helvetica", 24, "bold"))
label1.pack(pady=30)

label2 = Label(frame1, text="Username", bg="#34495e", fg="white", font=("Arial", 14))
label2.pack(pady=10)

entryu = Entry(frame1, font=("Arial", 14), width=25)
entryu.pack(pady=10)

label3 = Label(frame1, text="Password", bg="#34495e", fg="white", font=("Arial", 14))
label3.pack(pady=10)

entryp = Entry(frame1, show="*", font=("Arial", 14), width=25)
entryp.pack(pady=10)

error_label = Label(frame1, text="", fg="red", bg="#34495e", font=("Arial", 10))
error_label.pack()

# Login button
button1 = Button(frame1, text="Login", font=("Arial", 14), bg="#1abc9c", fg="white", activebackground="#16a085",
                 activeforeground="white", command=login)
button1.pack(pady=20)


win.mainloop()
