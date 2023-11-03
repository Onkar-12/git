import tkinter as tk
import tkinter.ttk as ttk

class SearchableTreeview(ttk.Treeview):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Create a variable to store the current search query
        self.search_query = tk.StringVar()
        
        # Create an entry widget to enter search queries
        self.search_entry = ttk.Entry(self, textvariable=self.search_query)
        self.search_entry.pack(side=tk.TOP, fill=tk.X)
        
        # Create a search button to start the search
        self.search_button = ttk.Button(self, text="Search", command=self.search)
        self.search_button.pack(side=tk.TOP, fill=tk.X)
    
    def search(self):
        # Get the search query from the entry widget
        query = self.search_query.get()
        
        # Iterate over all the items in the tree and compare the search query with the text in each item
        for item in self.get_children():
            if query in self.item(item, "text"):
                # If the search query is found, expand the item and highlight it
                self.item(item, open=True)
                self.selection_set(item)
                return
    
        # If the search query is not found, display an error message
        tk.messagebox.showinfo("Search", "No results found for '{}'".format(query))
