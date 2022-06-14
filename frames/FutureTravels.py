import settings
import tkinter as tk


from tkinter import CENTER, ttk
from frames.const import *
from PIL import ImageTk, Image
from utils.example_drivers import *

class FutureTravelRow(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=50, height=75)
        
        """ ATTRIBUTE """
        self.parent = parent

        self.accepted_str = tk.StringVar()
        self.driver_str = tk.StringVar()
        self.start_travel_time_str = tk.StringVar()
        self.destination_str = tk.StringVar()
        self.number_of_seats_str = tk.StringVar()
        self.cost_eth_str = tk.StringVar()
        
        self.accepted_label = ttk.Label(
            parent,
            textvariable=self.accepted_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)
        )
        self.driver_label = ttk.Label(
            parent,
            textvariable=self.driver_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)
        )
        self.date_label = ttk.Label(
            parent,
            textvariable=self.start_travel_time_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.destination_label = ttk.Label(
            parent,
            textvariable=self.destination_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.seats_label = ttk.Label(
            parent,
            textvariable=self.number_of_seats_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.cost_label = ttk.Label(
            parent,
            textvariable=self.cost_eth_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)
        )
        
        self.driver_label.config(anchor=CENTER)
        self.date_label.config(anchor=CENTER)
        self.destination_label.config(anchor=CENTER)
        self.seats_label.config(anchor=CENTER)
        self.cost_label.config(anchor=CENTER)
        
    def clear_row(self):
        self.accepted_str.set("")
        self.driver_str.set("")
        self.start_travel_time_str.set("")
        self.destination_str.set("")
        self.number_of_seats_str.set("")
        self.cost_eth_str.set("")
        
class FutureTravels(ttk.Frame):

    def __init__(self, parent, controller, style):
        super().__init__(parent, style=style)

        self.controller = controller

        """ ATTRIBUTES """

        """ LAYOUT CONFIGURATION """

        """ FIRST ROW """
        title_frame = ttk.Frame(
            self,
            style="TravelsFrame.TFrame"
        )
        future_travels_label = ttk.Label(
            title_frame,
            text="My Future Travels",
            style="TravelsTitle2.TLabel"
        )
        future_travels_label.grid(row=0, column=0, sticky="EW")

        title_frame.grid(row=0, column=0, columnspan=7, sticky="EW",
                                  padx=(200, 0), pady=(5, 0))

        """ SECOND ROW """
        car_img = ImageTk.PhotoImage(Image.open(self.controller.CAR_PNG_PATH).resize(
            (self.controller.PNG_WIDTH//self.controller.PNG_RESIZE_FACTOR, self.controller.PNG_HEIGHT//self.controller.PNG_RESIZE_FACTOR)))
        car_panel = ttk.Label(self, image=car_img, style="TravelsLabel.TLabel")
        car_panel.image = car_img

        clock_img = ImageTk.PhotoImage(Image.open(self.controller.CLOCK_PNG_PATH).resize(
            (self.controller.PNG_WIDTH//self.controller.PNG_RESIZE_FACTOR, self.controller.PNG_HEIGHT//self.controller.PNG_RESIZE_FACTOR)))
        clock_panel = ttk.Label(self, image=clock_img,
                                style="TravelsLabel.TLabel")
        clock_panel.image = clock_img

        placeholder_img = ImageTk.PhotoImage(Image.open(self.controller.PLACEHOLDER_PNG_PATH).resize(
            (self.controller.PNG_WIDTH//self.controller.PNG_RESIZE_FACTOR, self.controller.PNG_HEIGHT//self.controller.PNG_RESIZE_FACTOR)))
        placeholder_panel = ttk.Label(
            self, image=placeholder_img, style="TravelsLabel.TLabel")
        placeholder_panel.image = placeholder_img

        seats_img = ImageTk.PhotoImage(Image.open(self.controller.SEATS_PNG_PATH).resize(
            (self.controller.PNG_WIDTH//self.controller.PNG_RESIZE_FACTOR, self.controller.PNG_HEIGHT//self.controller.PNG_RESIZE_FACTOR)))
        seats_panel = ttk.Label(self, image=seats_img,
                                style="TravelsLabel.TLabel")
        seats_panel.image = seats_img

        money_img = ImageTk.PhotoImage(Image.open(self.controller.MONEY_PNG_PATH).resize(
            (self.controller.PNG_WIDTH//self.controller.PNG_RESIZE_FACTOR, self.controller.PNG_HEIGHT//self.controller.PNG_RESIZE_FACTOR)))
        money_panel = ttk.Label(self, image=money_img,
                                style="TravelsLabel.TLabel")
        money_panel.image = money_img

        car_panel.grid(row=1, column=1, sticky="NS", pady=(5, 0))
        clock_panel.grid(row=1, column=2, sticky="NS", pady=(5, 0))
        placeholder_panel.grid(row=1, column=3, sticky="NS", pady=(5, 0))
        seats_panel.grid(row=1, column=4, sticky="NS", pady=(5, 0))
        money_panel.grid(row=1, column=5, sticky="NS", pady=(5, 0))
        
        """ THIRD ROW """
        selection_label = ttk.Label(
            self,
            text="Accepted",
            style="TravelsNormalText.TLabel",
            padding=(5, 5, 20, 0)

        )
        driver_label = ttk.Label(
            self,
            text="Driver",
            style="TravelsTitle3.TLabel",
            padding=(10, 5, 5, 0)
        )
        date_time_label = ttk.Label(
            self,
            text="Time",
            style="TravelsTitle3.TLabel",
            padding=(10, 5, 5, 0)
        )
        destination_label = ttk.Label(
            self,
            text="Destination",
            style="TravelsTitle3.TLabel",
            padding=(10, 5, 5, 0)
        )
        seats_number_label = ttk.Label(
            self,
            text="# of seats",
            style="TravelsTitle3.TLabel",
            padding=(10, 5, 5, 0)
        )
        cost_eth_label = ttk.Label(
            self,
            text="Cost Eth",
            style="TravelsTitle3.TLabel",
            padding=(10, 5, 5, 0)
        )

        selection_label.config(anchor=CENTER)
        driver_label.config(anchor=CENTER)
        date_time_label.config(anchor=CENTER)
        destination_label.config(anchor=CENTER)
        seats_number_label.config(anchor=CENTER)
        cost_eth_label.config(anchor=CENTER)

        table_separator = ttk.Separator(self)

        selection_label.grid(row=2, column=0, sticky="EW", padx=(10, 0))
        driver_label.grid(row=2, column=1, sticky="EW")
        date_time_label.grid(row=2, column=2, sticky="EW")
        destination_label.grid(row=2, column=3, sticky="EW")
        seats_number_label.grid(row=2, column=4, sticky="EW")
        cost_eth_label.grid(row=2, column=5, sticky="EW")

        table_separator.grid(row=3, columnspan=6, padx=(10, 10), sticky="EW")

        """ FOURTH ROW """
        self.fourth_row = FutureTravelRow(self)
        
        self.fourth_row.accepted_label.grid(row=4, column=0)
        self.fourth_row.driver_label.grid(row=4, column=1)
        self.fourth_row.date_label.grid(row=4, column=2)
        self.fourth_row.destination_label.grid(row=4, column=3)
        self.fourth_row.seats_label.grid(row=4, column=4)
        self.fourth_row.cost_label.grid(row=4, column=5)

        """ FIFTH ROW """
        self.fifth_row = FutureTravelRow(self)

        self.fifth_row.accepted_label.grid(row=5, column=0)
        self.fifth_row.driver_label.grid(row=5, column=1)
        self.fifth_row.date_label.grid(row=5, column=2)
        self.fifth_row.destination_label.grid(row=5, column=3)
        self.fifth_row.seats_label.grid(row=5, column=4)
        self.fifth_row.cost_label.grid(row=5, column=5)

        """ SIXTH ROW """
        self.sixth_row = FutureTravelRow(self)
        
        self.sixth_row.accepted_label.grid(row=5, column=0)
        self.sixth_row.driver_label.grid(row=5, column=1)
        self.sixth_row.date_label.grid(row=5, column=2)
        self.sixth_row.destination_label.grid(row=5, column=3)
        self.sixth_row.seats_label.grid(row=5, column=4)
        self.sixth_row.cost_label.grid(row=5, column=5)

        """ SEVENTH ROW """
        self.seventh_row = FutureTravelRow(self)

        self.seventh_row.accepted_label.grid(row=7, column=0)
        self.seventh_row.driver_label.grid(row=7, column=1)
        self.seventh_row.date_label.grid(row=7, column=2)
        self.seventh_row.destination_label.grid(row=7, column=3)
        self.seventh_row.seats_label.grid(row=7, column=4)
        self.seventh_row.cost_label.grid(row=7, column=5)

        """ EIGTH ROW """
        self.eigth_row = FutureTravelRow(self)
        
        self.eigth_row.accepted_label.grid(row=7, column=0)
        self.eigth_row.driver_label.grid(row=7, column=1)
        self.eigth_row.date_label.grid(row=7, column=2)
        self.eigth_row.destination_label.grid(row=7, column=3)
        self.eigth_row.seats_label.grid(row=7, column=4)
        self.eigth_row.cost_label.grid(row=7, column=5)

        """ NINTH ROW """
        self.ninth_row = FutureTravelRow(self)
        
        self.ninth_row.accepted_label.grid(row=7, column=0)
        self.ninth_row.driver_label.grid(row=7, column=1)
        self.ninth_row.date_label.grid(row=7, column=2)
        self.ninth_row.destination_label.grid(row=7, column=3)
        self.ninth_row.seats_label.grid(row=7, column=4)
        self.ninth_row.cost_label.grid(row=7, column=5)

        self.rows = [
            self.fourth_row,
            self.fifth_row,
            self.sixth_row,
            self.seventh_row,
            self.eigth_row,
            self.ninth_row,
        ]

        self.update_rideshare_future_travels_rows()

    def clear_rows(self):
        for row in self.rows:
            row.clear_row()


    def update_rideshare_future_travels_rows(self):
        self.clear_rows()
        for index, smart_contract in enumerate(settings.g_rideshare_future_travels):            
            current_row = self.rows[index] 
            current_row.accepted_str.set("✓")
            current_row.driver_str.set(smart_contract.driver)
            current_row.destination_str.set(smart_contract.destination)
            current_row.start_travel_time_str.set(smart_contract.start_travel_time)
            current_row.number_of_seats_str.set(smart_contract.number_of_seats)
            current_row.cost_eth_str.set(smart_contract.cost_eth)
